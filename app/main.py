from fastapi import FastAPI
from fastapi.responses import ORJSONResponse
from fastapi.middleware.cors import CORSMiddleware

import api

app = FastAPI(
    title="API для проверки cors и tls",
    docs_url="/tls_test/docs",
    openapi_url="/tls_test/docs_json",
    default_response_class=ORJSONResponse,
)

# Добавляем настройки CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://truepotatoes.ru", "https://confluence.mts.ru"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router, prefix="/tls_test/api/v1", tags=["Test"])
