import streamlit as st
import random
import pandas as pd
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

product_categories = load_data('data/products.csv')

def generate_random_recommendations(selected_products, product_data, num_recommendations=3):
    # Filter out the selected products
    available_products = product_data[~product_data['Product'].isin(selected_products)]
    # Sample random products for recommendations
    recommendations = available_products.sample(n=min(num_recommendations, len(available_products)))
    return recommendations

def create_recommendation_df(recommendations):
    recommendations['Likelihood of Purchase'] = [random.randint(50, 99) for _ in range(len(recommendations))]
    return recommendations[['Product', 'Likelihood of Purchase']]

def plot_likelihood_of_purchase(df_recommendations):
    fig, ax = plt.subplots(figsize=(6, 4))
    df_sorted = df_recommendations.sort_values('Likelihood of Purchase', ascending=True)
    ax.barh(df_sorted['Product'], df_sorted['Likelihood of Purchase'], color='skyblue')
    ax.set_xlabel('Likelihood of Purchase (%)')
    ax.set_title('Likelihood of Purchase for Recommended Products')
#    st.pyplot(fig)

def recommend_main():
    with st.container():
        st.title('Product Recommender')
        # Form for category and product selection
        with st.expander(label="", expanded = True):
            col1, col2 = st.columns(2)
            with col1 :
                categories = product_categories['Category'].unique()
                selected_category = st.selectbox('Choose category:', options=[''] + list(categories))
            with col2:
                # Enable product selection only if a category is selected
                if selected_category:
                    filtered_products = product_categories[product_categories['Category'] == selected_category]['Product'].tolist()
                    selected_products = st.multiselect('Choose products:', options=filtered_products)
                else:
                    selected_products = st.multiselect('Choose products:', [])

            # Submit button for the form
            submit_button = st.button(label='Get Recommendations')

        if submit_button and selected_category and selected_products:
            recommendations_df = generate_random_recommendations(selected_products, product_categories[product_categories['Category'] == selected_category])
            df_recommendations = create_recommendation_df(recommendations_df)

            with st.container():
                st.title('Recommendations')
                with st.expander(label="", expanded=True):

                    col1, col2 = st.columns(2)  # You can adjust the ratio as needed for your UI
                    with col1:

                        st.dataframe(df_recommendations,
                                 column_config={
                                     'Likelihood of Purchase': st.column_config.NumberColumn(
                                         'Likelihood of Purchase',
                                         help="How likely is user to buy this **product**",
                                         min_value=0,
                                         max_value=100,
                                         step=1,
                                         format="%d %%",
                                     )},
                                 hide_index=True,
                                 )


                    with col2:

                        fig = plot_likelihood_of_purchase(df_recommendations)
                        st.pyplot(fig)
        elif submit_button:
            st.write('Please select a category and at least one product to see recommendations.')