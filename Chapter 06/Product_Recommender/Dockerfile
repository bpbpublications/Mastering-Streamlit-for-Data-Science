FROM python:3.9-slim
EXPOSE 8501

RUN pip install --upgrade pip

WORKDIR /app

# Copying requirements file first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copying your Streamlit applications
COPY ./data_app.py .
COPY ./recommend_app.py .
COPY ./top_products_app.py .

# Copying the data directory
COPY ./data ./data

# Copying the models directory
COPY ./models ./models

CMD streamlit run data_app.py --server.port=8501 --browser.serverAddress="0.0.0.0"
