import streamlit as st

graph = """
    digraph {
        a -> b;
        b -> c;
        c -> d;
        d -> a;
    }
"""

st.graphviz_chart(graph)
