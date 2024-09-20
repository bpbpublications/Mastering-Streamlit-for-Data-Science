FROM python:3.9-slim
EXPOSE 8501

RUN pip install --upgrade pip

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r  requirements.txt

COPY data_app.py .

CMD streamlit run data_app.py --server.port=8501 --browser.serverAddress="0.0.0.0"