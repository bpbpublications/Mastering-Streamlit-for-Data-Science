import streamlit as st
import random
import pandas as pd

# Sample product data
products = ['Phone', 'Laptop', 'Headphones', 'Camera', 'Smartwatch', 'Tablet', 'Charger', 'Keyboard', 'Mouse', 'Speaker']

def generate_random_recommendations(selected_products, products, num_recommendations=3):
    """Generate random product recommendations."""
    available_products = [p for p in products if p not in selected_products]
    recommendations = random.sample(available_products, min(num_recommendations, len(available_products)))
    return recommendations

def create_recommendation_df(recommendations):
    """Create a DataFrame with recommendations and random likelihood percentages."""
    likelihoods = [random.randint(50, 99) for _ in recommendations]  # Random likelihood percentages between 50% and 99%
    return pd.DataFrame({'Recommended Product': recommendations, 'Likelihood of Purchase': likelihoods})

# Streamlit application layout
st.title('Product Recommender')
st.write('Select one or more products to see recommendations.')

# User selects multiple products
selected_products = st.multiselect('Choose products:', products, default=None)

# Generate recommendations if any product is selected
if selected_products:
    recommendations = generate_random_recommendations(selected_products, products)

    # Create and display recommendations DataFrame
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
else:
    st.write('Please select at least one product to see recommendations.')


