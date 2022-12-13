
from fastapi import Depends, FastAPI, HTTPException
import uvicorn



import logging

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from opentelemetry.sdk.trace import TracerProvider

app = FastAPI(title="Sample FastAPI Application",
    description="Sample FastAPI Application with Swagger and Sqlalchemy",
    version="1.0.0",)

def init_otel():
    resource = Resource(attributes={"service.name": "fastApi_otel_demo"})
    trace.set_tracer_provider(TracerProvider(resource=resource))
    LoggingInstrumentor().instrument()
    FastAPIInstrumentor.instrument_app(app)

init_otel()
logger = logging.getLogger(__name__)


@app.get('/hello')
def say_hello():
    logger.info("This is an info message")
    return {"message": "Hello"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True , log_config='log-desktop.yaml')
