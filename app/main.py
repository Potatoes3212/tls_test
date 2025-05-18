from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

import api

app = FastAPI(
    title="API для проверки cors и tls",
    docs_url="/tls_test/docs",
    openapi_url="/tls_test/docs_json",
    default_response_class=ORJSONResponse,
)

app.include_router(api.router, prefix="/tls_test/api/v1", tags=["Test"])
