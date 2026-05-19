from fastapi import FastAPI
import os
import socket
import time
import logging

app = FastAPI(title="DevOps Health API")

APP_VERSION = os.getenv("APP_VERSION", "local")
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@app.get("/")
def root():
    return {"message": "DevOps Health API is running", "docs": "/docs"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def    ready():
    return {"status": "ready"}


@app.get("/version")
def version():
    return {
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "hostname": socket.gethostname(),
    }


@app.get("/logs-demo")
def logs_demo():
    logger.info("Logs demo endpoint was called")
    return {"message": "Log generated"}


@app.get("/compute")
def compute():
    start = time.time()
    total = sum(i * i for i in range(10000))
    duration = time.time() - start

    return {"result": total, "duration_seconds": duration}
