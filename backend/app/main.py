from fastapi import FastAPI

from app.api.v1 import api_router

API_V1_STR: str = "/api/v1"
PROJECT_NAME: str = "econet24-ng"

app = FastAPI(
    title=PROJECT_NAME,
    openapi_url=f"{API_V1_STR}/openapi.json",
)

app.include_router(api_router, prefix=API_V1_STR)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
