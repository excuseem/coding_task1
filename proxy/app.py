import requests

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from proxy.jwt_utils import create_jwt_token
from proxy.settings import HOST, PORT, UPSTREAM_URL
from proxy.status import Status

app = FastAPI()
status = Status()


@app.post("/proxy")
async def proxy(request: Request):
    status.increment_requests()
    body = await request.json()

    jwt_token = create_jwt_token(body)
    headers = {"x-my-jwt": jwt_token}

    response = requests.post(UPSTREAM_URL, json=body, headers=headers)
    return JSONResponse(content=response.json(), status_code=response.status_code, headers=headers)


@app.get("/status")
def get_status():
    return status.get_status()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=HOST, port=PORT)
