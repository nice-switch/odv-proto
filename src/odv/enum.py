import enum, peewee


class DatabaseConnection(enum.Enum):
    PRODUCTION = peewee.SqliteDatabase("workspace/production.sqlite")
    DEVELOPMENT = peewee.SqliteDatabase("workspace/development.sqlite")


class AccountInformationRequirements(enum.Enum):
    MINIMUM_USERNAME_LENGTH = 4
    