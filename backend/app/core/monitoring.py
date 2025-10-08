from prometheus_fastapi_instrumentator import Instrumentator

def setup_metrics(app):
    inst = Instrumentator.instrument(app).expose(app)