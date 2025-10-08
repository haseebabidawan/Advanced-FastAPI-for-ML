from prometheus_fastapi_instrumentator import Instrumentator

def setup_metrics(app):
    instrumentator = Instrumentator()
    instrumentator.instrument(app).expose(app)