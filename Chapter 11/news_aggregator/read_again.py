import streamlit as st

def remove_from_favorites(article):
    if article in st.session_state.favorites:
        st.session_state.favorites.remove(article)
        st.rerun()


def read_again():
    if 'favorites' not in st.session_state:
        st.session_state.favorites = []
        st.info('No favorite articles added.')
        return

    if not st.session_state.favorites:
        st.info('No favorite articles added.')
        return

    else:


        for article in st.session_state.favorites:
            col1, col2 = st.columns((4, 1))
            with col1:
                if article.get('title') and article['title'] != '[Removed]':
                    st.write(f"### {article['title']}")
                    if article.get('description'):
                        st.write(article['description'])
                    if article.get('urlToImage'):
                        st.image(article['urlToImage'], use_column_width=True)
                    with st.expander('More Details'):
                        st.write(f"**Author:** {article.get('author', 'N/A')}")
                        st.write(f"**Source:** {article['source'].get('name', 'N/A')}")
                        st.write(f"**Published At:** {article.get('publishedAt')}")
                        if 'video' in article:
                            st.video(article['video'])
            with col2:
                if st.button('Read', key=f"read{article['title']}"):
                    remove_from_favorites(article)
            st.write('----')
