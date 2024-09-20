import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(file_path):
    return pd.read_csv(file_path)

current_dir = os.path.dirname(__file__)
product_sales_file_path = os.path.join(current_dir, 'data', 'products_sales.csv')
sales_df = load_data(product_sales_file_path)

sales_df['Order Date'] = pd.to_datetime(sales_df['Order Date'])

def plot_sales_over_time(sales_df):
    # Group by month and sum up sales
    sales_over_time = sales_df.groupby(sales_df['Order Date'].dt.to_period('M')).agg({'Price': 'sum'})
    sales_over_time.reset_index(inplace=True)
    sales_over_time['Order Date'] = sales_over_time['Order Date'].dt.to_timestamp()

    plt.figure(figsize=(10, 5))
    plt.plot(sales_over_time['Order Date'], sales_over_time['Price'], marker='o', linestyle='-')
    plt.title('Sales Over Time')
    plt.xlabel('Order Date')
    plt.ylabel('Total Sales ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    st.pyplot(plt)

def plot_customer_demographics(sales_df):
    # Set a consistent figure size for both plots
    fig_size = (6, 4)  # Width, height in inches

    # Age distribution
    fig_age, ax_age = plt.subplots(figsize=fig_size)
    ax_age.hist(sales_df['User Age'], bins=10, edgecolor='black')
    ax_age.set_title('Age Distribution of Customers')
    ax_age.set_xlabel('Age')
    ax_age.set_ylabel('Frequency')

    # Gender distribution
    fig_gender, ax_gender = plt.subplots(figsize=fig_size)
    gender_counts = sales_df['User Gender'].value_counts()
    ax_gender.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
    plt.tight_layout()

    return fig_age, fig_gender

# # Function to plot Overall Top Products
def plot_top_products(sales_df):
    top_products = sales_df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(10)
    fig_top, ax_top = plt.subplots()
    sns.barplot(x=top_products.values, y=top_products.index, ax=ax_top)
    ax_top.set_title('Top Products by Quantity Sold')
    st.pyplot(fig_top)



def calculate_clv(sales_df):
    # Assuming a simple CLV calculation for demonstration: average revenue per user
    revenue_per_user = sales_df.groupby('User ID')['Price'].sum().mean()
    st.metric(label="Customer Lifetime Value (CLV)", value=f"${revenue_per_user:.2f}")

def calculate_aov(sales_df):
    total_revenue = sales_df['Price'].sum()
    total_orders = sales_df.shape[0]
    aov = total_revenue / total_orders
    st.metric("Average Order Value", f"${aov:.2f}")

def calculate_purchase_frequency(sales_df):
    total_orders = sales_df.shape[0]
    unique_customers = sales_df['User ID'].nunique()
    purchase_frequency = total_orders / unique_customers
    st.metric("Purchase Frequency(orders per customer)", f"{purchase_frequency:.2f}")


def top_products_main():
    st.title('Product Recommender Insights')


    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander(label="", expanded=True):
            calculate_clv(sales_df)
    with col2:
        with st.expander(label="", expanded=True):
            calculate_aov(sales_df)
    with col3:
        with st.expander(label="", expanded=True):
            calculate_purchase_frequency(sales_df)

    st.header('Sales Insight')
    with st.expander(label="", expanded=True):
        plot_sales_over_time(sales_df)

    st.header('Customer Distribution Insights')
    col21, col22 = st.columns(2)
    fig_gender, fig_age = plot_customer_demographics(sales_df)
    with col21:
        with st.expander(label="", expanded=True):
            st.pyplot(fig_gender)
    with col22:
        with st.expander(label="", expanded=True):
            st.pyplot(fig_age)


    # Overall Top Products Visualization
    st.header('Overall Top Products')
    plot_top_products(sales_df)