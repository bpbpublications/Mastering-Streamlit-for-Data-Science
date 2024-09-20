import streamlit as st

from recommend_app import *
from top_products_app import *

# Set page configuration
st.set_page_config(page_title="Product Recommender", page_icon="✔️", layout="wide",initial_sidebar_state="expanded")

def intro():
    st.title('Product Recommender')
    st.markdown("---")
    st.markdown(
        """
        > What does this app do ? 
        * This application helps to recommend products based on the products selected by the user.         
        * The application also shows the top trending products for each category.
        > How to use it ? 
        * Select the products from the dropdown, you can select multiple products too 
        * The result will be displayed with the top recommended products with the likelihood of purchase        
        """)
# Sidebar for user input
with st.sidebar:
    st.write("This is a demo app for Hands-on exercise for building Product Recommender app")



if __name__ == "__main__":
    # main page

    tab1, tab2, tab3 = st.tabs(["Intro","Product Recommendation", "Top Products"])
    with tab1:
        intro()
    with tab2:
        recommend_main()
    with tab3:
        top_products_main()



