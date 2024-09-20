from streamlit.testing.v1 import AppTest

def test_bean_counter():
    app_test = AppTest.from_file("home.py").run()
    app_test.number_input[0].increment().run()
    app_test.button[0].click().run()
    assert app_test.markdown[0].value == 'Total count: `1`'
