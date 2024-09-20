import streamlit as st



#title and header
st.title('This is a title')
st.header('This is a header')
st.subheader('This is a subheader')

# text and markdown
st.write('Hello, World!')
st.text('This is some text.')
st.markdown('**Bold** and _Italic_ Markdown Text')
st.caption('This is a caption that explains something above.')

# displays code
code = '''def hello_streamlit():
    print("This is code!")'''
st.code(code, language='python')
# displays mathematical functions
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
# draws horizontal ruler
st.divider()
st.json({
    'foo': 'bar',
    'baz': 'boz',
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})