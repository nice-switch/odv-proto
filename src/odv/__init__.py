import uvicorn, peewee

from odv import api, database, enum

def start(database_connection: peewee.Database, host: str, port: int):
    database.model.change_database_to(
        database=database_connection
    )

    uvicorn.run(
        app=api.initialize_fastapi(),
        host=host,
        port=port
    )