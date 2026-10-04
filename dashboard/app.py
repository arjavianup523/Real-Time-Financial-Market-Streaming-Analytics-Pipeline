import pandas as pd
import pymysql
import streamlit as st

from src.config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_NAME


st.set_page_config(
    page_title="Real-Time Financial Market Analytics",
    page_icon="📈",
    layout="wide",
)


def create_database_connection():
    return pymysql.connect(
        host=DB_HOST,
        port=int(DB_PORT),
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
    )


def load_data(query):
    connection = create_database_connection()

    try:
        return pd.read_sql(query, connection)
    finally:
        connection.close()


def main():
    st.title("📈 Real-Time Financial Market Analytics")

    st.caption(
        "Twelve Data → Python Producer → Kafka → "
        "Python Consumer → MySQL → Streamlit"
    )

    latest = load_data(
        """
        SELECT
            id,
            symbol,
            company_name,
            exchange_name,
            currency,
            market_datetime,
            close_price,
            volume,
            price_change,
            percent_change,
            received_at
        FROM market_data
        ORDER BY id DESC
        LIMIT 1
        """
    )

    if latest.empty:
        st.warning("No market data available.")
        return

    latest = latest.iloc[0]

    symbol = latest["symbol"]
    latest_price = float(latest["close_price"])
    price_change = float(latest["price_change"])
    percent_change = float(latest["percent_change"])
    volume = int(latest["volume"])

    st.subheader("Latest Market Data")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Symbol",
            symbol,
        )

    with col2:
        st.metric(
            "Latest Price",
            f"${latest_price:,.2f}",
        )

    with col3:
        st.metric(
            "Price Change",
            f"{price_change:+.2f}",
        )

    with col4:
        st.metric(
            "Percent Change",
            f"{percent_change:+.2f}%",
        )

    st.subheader("Market Details")

    details = pd.DataFrame(
        {
            "Metric": [
                "Company",
                "Exchange",
                "Currency",
                "Market Date",
                "Volume",
                "Received At",
            ],
            "Value": [
                latest["company_name"],
                latest["exchange_name"],
                latest["currency"],
                latest["market_datetime"],
                f"{volume:,}",
                latest["received_at"],
            ],
        }
    )

    st.dataframe(
        details,
        use_container_width=True,
        hide_index=True,
    )

    events = load_data(
        """
        SELECT
            id,
            symbol,
            close_price,
            volume,
            price_change,
            percent_change,
            received_at
        FROM market_data
        ORDER BY id ASC
        """
    )

    st.subheader("Price History")

    if not events.empty:
        chart_data = events[
            ["received_at", "close_price"]
        ].copy()

        chart_data["received_at"] = pd.to_datetime(
            chart_data["received_at"]
        )

        chart_data = chart_data.set_index(
            "received_at"
        )

        st.line_chart(
            chart_data["close_price"]
        )

    st.subheader("Recent Market Events")

    st.dataframe(
        events.sort_values(
            "id",
            ascending=False,
        ).head(20),
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Market Summary")

    summary = load_data(
        """
        SELECT
            symbol,
            COUNT(*) AS total_events,
            MIN(close_price) AS lowest_price,
            MAX(close_price) AS highest_price,
            AVG(close_price) AS average_price,
            SUM(volume) AS total_volume,
            MAX(received_at) AS latest_received_at
        FROM market_data
        GROUP BY symbol
        """
    )

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True,
    )


if __name__ == "__main__":
    main()