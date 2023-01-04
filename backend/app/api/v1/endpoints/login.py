from fastapi import APIRouter

router = APIRouter()


@router.post("/login")
def login():
    return {"status": "Not implemented yet!"}


# @router.post("/econnet24/login")
# def login():
#     return {"status": "Not implemented yet!"}


# import codecs
# import os
# import pickle
# from dataclasses import dataclass
#
# # TODO: Maybe use APIRouter to communicate to econet24 directly rather than through econet24_api
# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse
# from fastapi.staticfiles import StaticFiles
#
# from econet24_api import Econet24History
#
# app = FastAPI()
# api_root = os.path.dirname(os.path.abspath(__file__))
# app_root = os.path.join(os.path.dirname(api_root), "frontend")
# app.mount("/app", StaticFiles(directory=app_root, html=True), name="app")
#
#
# @dataclass
# class Login:
#     username: str
#     password: str
#
#
# @app.post("/api/login")
# async def econet24_login(login: Login, request: Request):
#     api = Econet24History()
#     _ = api.login(username=login.username, password=login.password)  # TODO: Return proper response from API
#
#     response = JSONResponse(content=request.cookies)
#
#     for cookie in api.session.cookies:
#         value = codecs.encode(
#             pickle.dumps(cookie, 0),
#             "base64"
#         ).decode()
#         response.set_cookie(
#             key=cookie.name,
#             value=value,
#             expires=cookie.expires,
#             domain="127.0.0.1",
#             path="/api",
#             secure=True,
#             httponly=True,
#             samesite="strict"
#         )
#
#     return response