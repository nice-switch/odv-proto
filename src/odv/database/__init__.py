from odv import enum
from odv.database import model, wrapper


def get_account_by_username(username: str) -> wrapper.AccountWrapper | None:
    pass


def get_account_by_email(email: str) -> wrapper.AccountWrapper | None:
    pass


def create_account(username: str, password: str, email: str | None = None) -> wrapper.AccountWrapper | None:
    assert len(username) >= enum.AccountInformationRequirements.MINIMUM_USERNAME_LENGTH.value, f"Username is too short! Must be at least {enum.AccountInformationRequirements.MINIMUM_USERNAME_LENGTH.value} characters long!"

    assert get_account_by_username(username) is None, "An account with this username already exists!"
    assert email is None or get_account_by_email(email) is None, "An account with this email already exists!"
    
