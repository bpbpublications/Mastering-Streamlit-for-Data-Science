import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from joblib import load
import os

@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)



current_dir = os.path.dirname(__file__)
product_sales_file_path = os.path.join(current_dir, 'data', 'products_sales.csv')
product_sales = load_data(product_sales_file_path)
def predict_and_rank(user_id, category, product_sales):

    if user_id not in product_sales['User ID'].unique():
        return f"No User"

    model_pipeline = load('models/recommender_model.joblib')
    all_products_info = product_sales[['Category', 'Product Name']].drop_duplicates()
    filtered_products = all_products_info[all_products_info['Category'] == category]['Product Name'].unique()
    predictions = []
    for product_name in filtered_products:
        prediction = model_pipeline.predict(str(user_id), str(product_name))
        predictions.append((product_name, prediction.est))

    predictions_df = pd.DataFrame(predictions, columns=['Product Name', 'Likelihood'])

    predictions_df.sort_values(by='Likelihood', ascending=False, inplace=True)
    return predictions_df.head(5)

def plot_likelihood_of_purchase(df_recommendations):
    fig, ax = plt.subplots(figsize=(6, 4))
    df_sorted = df_recommendations.sort_values('Likelihood', ascending=True)
    ax.barh(df_sorted['Product Name'], df_sorted['Likelihood'], color='skyblue')
    ax.set_xlabel('Likelihood of Purchase (%)')
    ax.set_title('Likelihood of Purchase for Recommended Products')

def recommend_main():
    with st.form("recommendation_form"):
        st.title('Product Recommender')

        user_id = st.number_input("Enter User ID", value=0, step=1)
        interested_category = st.selectbox("Select Interested Category",
                                           options=[''] + list(product_sales['Category'].unique()))

        submit_button = st.form_submit_button(label='Get Recommendations')

        if submit_button and interested_category:
            ranked_products = predict_and_rank(user_id, interested_category, product_sales)

            with st.container():
                st.title('Recommendations')
                if isinstance(ranked_products, str):
                    st.warning("User ID not found in the database.")
                else:
                    with st.expander(label="", expanded=True):
                        col1, col2 = st.columns(2)  # You can adjust the ratio as needed for your UI
                        with col1:
                            st.dataframe(ranked_products,
                                         column_config={
                                             'Likelihood of Purchase': st.column_config.NumberColumn(
                                                 'Likelihood',
                                                 help="How likely is user to buy this **product**",
                                                 min_value=0,
                                                 max_value=100,
                                                 step=1,
                                                 format="%d %%",
                                             )},
                                         hide_index=True,
                                         )

                        with col2:
                            fig = plot_likelihood_of_purchase(ranked_products)
                            st.pyplot(fig)
        elif submit_button:
            st.warning('Please select a category and at least one product to see recommendations.')

