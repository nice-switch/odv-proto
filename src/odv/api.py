import fastapi, json

from odv import database

def initialize_fastapi() -> fastapi.FastAPI:
    app = fastapi.FastAPI()

    @app.get("/get-account-by-username")
    async def get_account_by_username(username: str) -> dict:
        account_wrapper = database.get_account_by_username(username)
        
        return account_wrapper and account_wrapper.get_public_dictionary() or {}


    return app