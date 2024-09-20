import streamlit as st
import random
import pandas as pd

# Sample product data
products = ['Phone', 'Laptop', 'Headphones', 'Camera', 'Smartwatch', 'Tablet', 'Charger', 'Keyboard', 'Mouse', 'Speaker']
# Product data with categories
product_categories = {
    'Educational': ['Book', 'Online Course', 'Educational Toy', 'Science Kit', 'Math Workbook', 'Language Learning Software'],
    'Travel': ['Luggage', 'Travel Pillow', 'World Map', 'Travel Guidebook', 'Portable Charger', 'Travel Backpack'],
    'Books': ['Fiction', 'Non-Fiction', 'Biography', 'Mystery', 'Science Fiction', 'Historical Fiction', 'Self-Help'],
    'Gadgets': ['Phone', 'Headset', 'Smartwatch', 'Laptop', 'Tablet', 'E-reader', 'Portable Speaker', 'Fitness Tracker'],
    'Home & Kitchen': ['Coffee Maker', 'Blender', 'Smart Home Device', 'Cookware Set', 'Decorative Vase', 'Bedding Set'],
    'Fashion': ['T-shirt', 'Jeans', 'Dress', 'Watch', 'Handbag', 'Sneakers', 'Sunglasses', 'Jacket'],
    'Health & Wellness': ['Yoga Mat', 'Fitness Band', 'Protein Powder', 'Skincare Product', 'Haircare Kit', 'Vitamins', 'Aromatherapy Diffuser']
}

def generate_random_recommendations(selected_products, products, num_recommendations=3):
    """Generate random product recommendations."""
    available_products = [p for p in products if p not in selected_products]
    recommendations = random.sample(available_products, min(num_recommendations, len(available_products)))
    return recommendations

def create_recommendation_df(recommendations):
    """Create a DataFrame with recommendations and random likelihood percentages."""
    likelihoods = [random.randint(50, 99) for _ in recommendations]  # Random likelihood percentages between 50% and 99%
    return pd.DataFrame({'Recommended Product': recommendations, 'Likelihood of Purchase': likelihoods})

def recommend_main():

    with st.container():
        st.title('Product Recommender')

        # Form for category and product selection
        with st.expander(label="", expanded = True):
            col1, col2 = st.columns(2)
            with col1 :
                selected_category = st.selectbox('Choose category:', options=[''] + list(product_categories.keys()))
            with col2:
                # Enable product selection only if a category is selected
                if selected_category:
                    selected_products = st.multiselect('Choose products:', product_categories[selected_category])
                else:
                    selected_products = st.multiselect('Choose products:', [])

            # Submit button for the form
            submit_button = st.button(label='Get Recommendations')

        if submit_button and selected_category and selected_products:
            recommendations = generate_random_recommendations(selected_products, product_categories[selected_category])

            df_recommendations = create_recommendation_df(recommendations)
            st.write('Recommended Products:')

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
        elif submit_button:
            st.write('Please select a category and at least one product to see recommendations.')

