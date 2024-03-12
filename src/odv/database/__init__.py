from odv import enum
from odv.database import model, wrapper


def generic_peewee_get(target_model: model.BaseModel, model_property, target_value) -> model.BaseModel | None:
    result_model: target_model | None = None

    try:
        result_model = target_model.get(
            model_property == target_value
        )
    
    except model.peewee.DoesNotExist:
        pass
    
    return result_model


def get_account_by_username(username: str) -> wrapper.AccountWrapper | None:
    account_wrapper: wrapper.AccountWrapper | None = None

    try:
        account_wrapper = wrapper.AccountWrapper(
            model.Account.get(
                model.Account.username == username
            )
        )
    
    except model.peewee.DoesNotExist:
        pass

    return account_wrapper


def get_account_by_email(email: str) -> wrapper.AccountWrapper | None:
    account_wrapper: wrapper.AccountWrapper | None = None

    try:
        account_wrapper = wrapper.AccountWrapper(
            model.Account.get(
                model.Account.email == email
            )
        )
    
    except model.peewee.DoesNotExist:
        pass

    return account_wrapper


def create_account(username: str, password: str, email: str | None = None) -> wrapper.AccountWrapper | None:
    assert len(username) >= enum.AccountCreationRequirements.MINIMUM_USERNAME_LENGTH, enum.AccountCreationErrorMessages.MINIMUM_USERNAME_LENGTH_ERROR
    assert len(password) >= enum.AccountCreationRequirements.MINIMUM_PASSWORD_LENGTH, enum.AccountCreationErrorMessages.MINIMUM_PASSWORD_LENGTH_ERROR
    
    assert get_account_by_username(username) is None, "An account with this username already exists!"
    assert email is None or get_account_by_email(email) is None, "An account with this email already exists!"
    
    account_wrapper = wrapper.AccountWrapper(
        model.Account.create(
            username=username,
            email=email or ""
        )
    )

    account_wrapper.account_model.save()

    return account_wrapper