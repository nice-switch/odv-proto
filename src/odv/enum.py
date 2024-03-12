import enum, peewee


class Database():
    PRODUCTION = peewee.SqliteDatabase("workspace/production.sqlite")
    DEVELOPMENT = peewee.SqliteDatabase("workspace/development.sqlite")


class AccountCreationRequirements():
    MINIMUM_USERNAME_LENGTH = 6
    MINIMUM_PASSWORD_LENGTH = 12


class AccountCreationErrorMessages():
    MINIMUM_USERNAME_LENGTH_ERROR = f"Username is too short! Must be atleast {AccountCreationRequirements.MINIMUM_USERNAME_LENGTH} characters long!"
    MINIMUM_PASSWORD_LENGTH_ERROR = f"Password is too short! Must be atleast {AccountCreationRequirements.MINIMUM_PASSWORD_LENGTH} characters long!"
