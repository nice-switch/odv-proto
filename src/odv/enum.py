import peewee


class SaltParams():
    SALT_LENGTH = 32


class ScryptParams():
    KEY_LENGTH = 32
    N = 2 ** 14
    R = 8
    P = 1


class Database():
    PRODUCTION = peewee.SqliteDatabase("workspace/production.sqlite")
    DEVELOPMENT = peewee.SqliteDatabase("workspace/development.sqlite")
    MEMORY = peewee.SqliteDatabase(":memory:")

class AccountCreationRequirements():
    MINIMUM_USERNAME_LENGTH = 6
    MINIMUM_PASSWORD_LENGTH = 12


class AccountCreationErrorMessages():
    MINIMUM_USERNAME_LENGTH_ERROR = f"Username is too short! Must be atleast {AccountCreationRequirements.MINIMUM_USERNAME_LENGTH} characters long!"
    MINIMUM_PASSWORD_LENGTH_ERROR = f"Password is too short! Must be atleast {AccountCreationRequirements.MINIMUM_PASSWORD_LENGTH} characters long!"


class AccountDataTemplates():
    PLAIN = {}
    SECURE = {}