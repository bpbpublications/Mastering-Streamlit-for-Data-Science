import streamlit as st
import requests
from read_again import *

API_KEY = 'xx'
BASE_URL = 'https://newsapi.org/v2/top-headlines'

@st.cache_data
def load_news(category, language):
    return get_news(category, language)

def get_news(category, language='en'):
    url = f"{BASE_URL}?category={category}&language={language}&apiKey={API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()

        if data.get('status') == 'ok':
            articles = [article for article in data['articles'] if article['title'] != '[Removed]']
            return articles
        else:
            st.error(f"API returned an error: {data.get('message', 'No error message provided')}")
            return []
    except requests.RequestException as e:
        st.error(f"Error fetching news data: {str(e)}")
        return []


def toggle_favorite(title):
    if title in st.session_state.favorites:
        st.session_state.favorites.remove(title)
    else:
        st.session_state.favorites.append(title)

def news_show():
    st.title("Daily News Digest")
    st.write('----')
    st.sidebar.title('Language')
    languages = {'English': 'en', 'Spanish': 'es', 'French': 'fr', 'German': 'de'}
    selected_language = st.sidebar.selectbox('Select language', options=list(languages.keys()), index=0)
    st.sidebar.title('News Categories')
    categories = ['general','business', 'entertainment', 'health', 'science', 'sports', 'technology']
    selected_category = st.sidebar.selectbox('Select a category', categories)


    news_items = load_news(selected_category, languages[selected_language])

    for article in news_items:

        col1, col2 = st.columns((4,1))
        with col1 :
            if article['title'] != '[Removed]':
                st.write(f"### {article['title']}")
                if article['description']:
                    st.write(article['description'])
                if article['urlToImage']:
                    st.image(article['urlToImage'], use_column_width=True)
                with st.expander('More Details'):
                    st.write(f"**Author:** {article.get('author', 'N/A')}")
                    st.write(f"**Source:** {article['source']['name']}")
                    st.write(f"**Published At:** {article['publishedAt']}")

                    if 'video' in article:
                        st.video(article['video'])

                    st.markdown(f"[Read more]({article['url']})", unsafe_allow_html=True)
        with col2 :
            if st.button('Favorite', key=f"fav_{article['title']}"):
                toggle_favorite(article)
        st.write("---")

if __name__ == "__main__":

    tab1, tab2= st.tabs(["News","Read again"])
    with tab1:
        news_show()
    with tab2:
        read_again()




