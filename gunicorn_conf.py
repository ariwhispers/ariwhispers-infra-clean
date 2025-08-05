import multiprocessing, os
workers = int(os.getenv('GUNICORN_WORKERS', multiprocessing.cpu_count()*2+1))
bind = '0.0.0.0:8000'
worker_class = 'uvicorn.workers.UvicornWorker'
keepalive = 15
loglevel = os.getenv('LOG_LEVEL', 'info')
