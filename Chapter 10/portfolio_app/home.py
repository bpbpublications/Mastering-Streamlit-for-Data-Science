import streamlit as st
from  portfolio import *
from contact import *

def home_show():
    col1, col2, col3, col4 = st.columns((1,1,1,1))

    with col2:
        st.title("HELLO !")
        st.header("I am John Turner")

        st.write("""
                    I am a passionate data professional focused on building stories from the data. I love analyzing the data, cleaning it and looking for patterms. 
                    I have considerable experience in building complex pipelines for Data ingestion and modeling. I have worked with numerous business and Creative stakeholders. 
                    I believe every Dataset has a story to be told 
                """)
        st.write("""
                        - **My Key Skills are** 
                            - Data Exploration
                            - Data Modeling
                            - Building Ingestion pipeline 
                            - Business Intelligence
                                                        
                        - **I love to do** 
                            - Photography 
                            - Travel 
                            - Reading
                    """)
        st.markdown("[LinkedIn](https://www.linkedin.com/in/johnturner)[|Twitter|](https://www.twitter.com/johnturner) [GitHub](https://www.github.com/johnturner) [|Instagram](https://www.instagram.com/johnturner)")

    with col3:
        base_dir = os.path.dirname(__file__)
        image_path = os.path.join(base_dir, 'assets', 'portfolio1.png')
        st.image(image_path, width=500)

st.set_page_config(page_title='John Turner Portfolio', layout='wide')

if __name__ == "__main__":

    tab1, tab2, tab3 = st.tabs(["Home","Portfolio", "Contact"])
    with tab1:
        home_show()
    with tab2:
        portfolio_show()
    with tab3:
        contact_show()
