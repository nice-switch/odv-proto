from odv import enum
from odv.database import model, wrapper


def get_account_by_username(username: str) -> wrapper.AccountWrapper | None:
    pass


def get_account_by_email(email: str) -> wrapper.AccountWrapper | None:
    pass


def create_account(username: str, password: str, email: str | None = None) -> wrapper.AccountWrapper | None:
    assert len(username) >= enum.AccountCreationRequirements.MINIMUM_USERNAME_LENGTH, enum.AccountCreationErrorMessages.MINIMUM_USERNAME_LENGTH_ERROR
    assert len(password) >= enum.AccountCreationRequirements.MINIMUM_PASSWORD_LENGTH, enum.AccountCreationErrorMessages.MINIMUM_PASSWORD_LENGTH_ERROR
    
    assert get_account_by_username(username) is None, "An account with this username already exists!"
    assert email is None or get_account_by_email(email) is None, "An account with this email already exists!"
    
