import json, peewee

__account_config: None | dict = None
__database_config: None | dict = None
with open("config/account.json", "r") as file:
    __account_config = json.loads(file.read())
with open("config/database.json", "r") as file:
    __database_config = json.loads(file.read())

__creation_requirements = __account_config.get("creation_requirements")

__available_connections = __database_config.get("available_connections")

USERNAME_MAXIMUM_LENGTH = __creation_requirements.get("username_maximum_length")
USERNAME_MINIMUM_LENGTH = __creation_requirements.get("username_minimum_length")

SELECTED_DATABASE_NAME = __database_config.get("selected_database")

PRODUCTION_DATABASE_CONNECTION: peewee.Database | None = None
DEVELOPMENT_DATABASE_CONNECTION: peewee.Database | None = None
MEMORY_DATABASE_CONNECTION: peewee.Database | None = None


__selected_database_connection = __available_connections.get(SELECTED_DATABASE_NAME)
if __selected_database_connection is not None:
     PRODUCTION_DATABASE_CONNECTION = peewee[__selected_database_connection.get("peewee_database_class")](
         __selected_database_connection.get("production")
     )   
else:
    raise Exception(f"Invalid selected database! '{SELECTED_DATABASE_NAME}'")