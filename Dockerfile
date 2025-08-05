FROM python:3.11-slim
ARG BUILD_DATE
LABEL org.opencontainers.image.created=$BUILD_DATE
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY ./app ./app
COPY gunicorn_conf.py prestart.sh ./
EXPOSE 8000
ENTRYPOINT ["./prestart.sh"]
CMD ["gunicorn", "-c", "gunicorn_conf.py", "app.main:app"]
