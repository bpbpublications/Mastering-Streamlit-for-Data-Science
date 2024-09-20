import streamlit as st
import pandas as pd


data_df = pd.DataFrame(
    {
        "widgets": ["st.selectbox", "st.number_input", "st.text_area", "st.button"],
        "widgets_func": ["Let's you select a value ", "Let's you input a number", "Let's you input text", "Let's you click submission"],
        "widget_rank": [9, 950, 3, 1],
        "favorite": [True, False, False, True],
        "category": [
                    "📊 Data Exploration",
                    "📈 Data Visualization",
                    "🤖 LLM",
                    "📊 Data Exploration",
                ],
    }
)

st.data_editor(
    data_df,
    column_config={
        "widgets": st.column_config.Column(
            "Streamlit Widgets",
            help="Streamlit **widget** commands",
            width="medium",
            required=True,
        ),
        "widgets_func": st.column_config.TextColumn(
            "What it does",
            help="Streamlit **widget** function",
            max_chars=50,
            validate="^st\.[a-z_]+$",
        ),
        "widget_rank": st.column_config.NumberColumn(
            "Global Widget rank",
            help="Rank of **widget**",
            min_value=0,
            max_value=1000,
            step=1,
            format="%d",
        ),
        "favorite": st.column_config.CheckboxColumn(
            "Your favorite?",
            help="Select your **favorite** widgets",
            default=False,
        ),
        "category": st.column_config.SelectboxColumn(
            "Category of the widget",
            help="The category of the widget",
            width="medium",
            options=[
                "📊 Data Exploration",
                "📈 Data Visualization",
                "🤖 LLM",
            ]
        )
    },
    hide_index=True,

)


#
#
# df = pd.DataFrame(
#     [
#        {"command": "st.selectbox", "rating": 4, "is_widget": True},
#        {"command": "st.balloons", "rating": 5, "is_widget": False},
#        {"command": "st.time_input", "rating": 3, "is_widget": True},
#    ]
# )
#
# st.write("Table displayed using st.table")
# st.table(df)
# st.divider()
# st.write("Table displayed using st.dataframe")
# st.dataframe(df)
# st.divider()
# st.write("Table displayed and can be edited using st.data_editor")
# edited_df = st.data_editor(df, num_rows="dynamic")
# favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
# st.markdown(f"Your favorite command is **{favorite_command}** ")
