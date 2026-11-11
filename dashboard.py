
import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------
# PAGE CONFIGURATION
# -------------------------------
st.set_page_config(
    page_title="SWYNEX Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Sales Analytics Dashboard")
st.caption("SWYNEX Internship | Interactive Business Intelligence Dashboard")

# -------------------------------
# LOAD DATASET
# -------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("cleaned_dataset.csv")

    df.columns = df.columns.str.strip()

    df["purchase_amount"] = pd.to_numeric(
        df["purchase_amount"], errors="coerce"
    )

    df["age"] = pd.to_numeric(df["age"], errors="coerce")

    df["purchase_date"] = pd.to_datetime(
        df["purchase_date"], errors="coerce"
    )

    df = df.dropna(subset=[
        "purchase_amount", "purchase_date"
    ])

    return df

try:
    df = load_data()
except Exception as e:
    st.error("Unable to load cleaned_dataset.csv.")
    st.info("Place cleaned_dataset.csv in the same folder as app.py.")
    st.stop()

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.header("🔎 Dashboard Filters")

cities = sorted(df["city"].dropna().unique())
selected_cities = st.sidebar.multiselect(
    "Select City",
    cities,
    default=cities
)

genders = sorted(df["gender"].dropna().unique())
selected_genders = st.sidebar.multiselect(
    "Select Gender",
    genders,
    default=genders
)

payments = sorted(df["payment_method"].dropna().unique())
selected_payments = st.sidebar.multiselect(
    "Payment Method",
    payments,
    default=payments
)

min_date = df["purchase_date"].min().date()
max_date = df["purchase_date"].max().date()

date_range = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# -------------------------------
# APPLY FILTERS
# -------------------------------
filtered_df = df[
    df["city"].isin(selected_cities) &
    df["gender"].isin(selected_genders) &
    df["payment_method"].isin(selected_payments)
].copy()

if isinstance(date_range, (tuple, list)) and len(date_range) == 2:
    start_date, end_date = date_range

    filtered_df = filtered_df[
        (filtered_df["purchase_date"].dt.date >= start_date) &
        (filtered_df["purchase_date"].dt.date <= end_date)
    ]

# -------------------------------
# KPI METRICS
# -------------------------------
st.subheader("📌 Key Performance Indicators")

total_sales = filtered_df["purchase_amount"].sum()
total_orders = len(filtered_df)
average_order = (
    total_sales / total_orders if total_orders else 0
)
unique_customers = filtered_df["customer_id"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"₹{total_sales:,.2f}")
col2.metric("Total Orders", f"{total_orders:,}")
col3.metric("Average Order Value", f"₹{average_order:,.2f}")
col4.metric("Unique Customers", f"{unique_customers:,}")

st.divider()

if filtered_df.empty:
    st.warning("No records match the selected filters.")
    st.stop()

# -------------------------------
# SALES ANALYSIS CHARTS
# -------------------------------
st.subheader("📈 Sales Analysis")

col1, col2 = st.columns(2)

with col1:
    city_sales = (
        filtered_df.groupby("city", as_index=False)
        ["purchase_amount"].sum()
        .sort_values("purchase_amount", ascending=False)
    )

    fig_city = px.bar(
        city_sales,
        x="city",
        y="purchase_amount",
        title="Sales by City",
        labels={
            "city": "City",
            "purchase_amount": "Sales Amount (₹)"
        },
        color="city"
    )

    st.plotly_chart(fig_city, use_container_width=True)

with col2:
    payment_sales = (
        filtered_df.groupby("payment_method", as_index=False)
        ["purchase_amount"].sum()
    )

    fig_payment = px.pie(
        payment_sales,
        names="payment_method",
        values="purchase_amount",
        title="Sales by Payment Method",
        hole=0.4
    )

    st.plotly_chart(fig_payment, use_container_width=True)

# -------------------------------
# CUSTOMER ANALYSIS
# -------------------------------
st.subheader("👥 Customer Analysis")

col1, col2 = st.columns(2)

with col1:
    gender_count = (
        filtered_df["gender"]
        .value_counts()
        .reset_index()
    )
    gender_count.columns = ["Gender", "Customers"]

    fig_gender = px.bar(
        gender_count,
        x="Gender",
        y="Customers",
        title="Customer Distribution by Gender",
        color="Gender"
    )

    st.plotly_chart(fig_gender, use_container_width=True)

with col2:
    fig_age = px.histogram(
        filtered_df.dropna(subset=["age"]),
        x="age",
        nbins=10,
        title="Customer Age Distribution",
        labels={"age": "Age"},
        color_discrete_sequence=["#3498db"]
    )

    st.plotly_chart(fig_age, use_container_width=True)

# -------------------------------
# SALES TREND
# -------------------------------
st.subheader("📅 Sales Trend Over Time")

daily_sales = (
    filtered_df.groupby(
        filtered_df["purchase_date"].dt.date
    )["purchase_amount"]
    .sum()
    .reset_index()
)

daily_sales.columns = ["Date", "Sales"]

fig_trend = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Daily Sales Trend",
    markers=True
)

st.plotly_chart(fig_trend, use_container_width=True)

# -------------------------------
# BUSINESS INSIGHTS
# -------------------------------
st.subheader("💡 Key Business Insights")

best_city = city_sales.iloc[0]["city"]
best_city_sales = city_sales.iloc[0]["purchase_amount"]

best_payment = payment_sales.loc[
    payment_sales["purchase_amount"].idxmax(),
    "payment_method"
]

highest_sales_day = daily_sales.loc[
    daily_sales["Sales"].idxmax(), "Date"
]

insights = [
    f"{best_city} generated the highest sales (₹{best_city_sales:,.2f}).",
    f"{best_payment} contributed the highest sales among payment methods.",
    f"The dashboard contains {total_orders} purchase records after filtering.",
    f"The average purchase value is ₹{average_order:,.2f}.",
    f"The highest daily sales occurred on {highest_sales_day}."
]

for i, insight in enumerate(insights, 1):
    st.markdown(f"**{i}.** {insight}")

# -------------------------------
# DATA TABLE
# -------------------------------
st.subheader("📋 Filtered Sales Records")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

# -------------------------------
# DOWNLOAD REPORT
# -------------------------------
csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Filtered Dataset",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv"
)

st.caption("Developed for SWYNEX Data Analytics Internship")
