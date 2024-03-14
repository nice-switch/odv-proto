import fastapi, json


from odv import database


def initialize_fastapi() -> fastapi.FastAPI:
    app = fastapi.FastAPI()

    @app.get("/account/public-info")
    async def get_public_info(username: str) -> dict:
        account = database.get_account_by_username(username)

        if account is not None:
            return account.get_public_dictionary()
        else:
            return {"status": 404, "message": "No account found!"}


    @app.get("/account/plain-info")
    async def get_plain_info(username: str, password: str) -> dict:
        account = database.get_account_by_username(username)
        available_info = {"status": 404, "message": "No account found or invalid password!"}

        try:
            available_info = account.get_plain_dictionary(password)
            
        except Exception as _:
            print(_)

        return available_info



    return app