from starlette.middleware.base import BaseHTTPMiddleware
import logging


class loggingMiddle(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        logging.INFO(f'Request:{request.method} {request.url}')
        response =  await call_next(request)
        logging.INFO(f'Response:{response.status_code}')
        return response