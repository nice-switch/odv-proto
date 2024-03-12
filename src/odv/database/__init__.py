import json

from odv import enum
from odv.database import model, wrapper, secure


def __generic_peewee_get(target_model: model.BaseModel, target_property: model.peewee.Field, target_value) -> model.BaseModel | None:
    result_model: target_model | None = None

    try:
        result_model = target_model.get(
            target_property == target_value
        )
    
    except model.peewee.DoesNotExist:
        pass
    
    return result_model


def get_account_by_username(username: str) -> wrapper.AccountWrapper | None:
    account_model = __generic_peewee_get(
        target_model=model.Account,
        target_property=model.Account.username,
        target_value=username
    )

    return account_model is not None and wrapper.AccountWrapper(account_model) or None


def get_account_by_email(email: str) -> wrapper.AccountWrapper | None:
    account_model = __generic_peewee_get(
        target_model=model.Account,
        target_property=model.Account.email,
        target_value=email
    )

    return account_model is not None and wrapper.AccountWrapper(account_model) or None


def create_account(username: str, password: str, email: str | None = None) -> wrapper.AccountWrapper | None:
    assert len(username) >= enum.AccountCreationRequirements.MINIMUM_USERNAME_LENGTH, enum.AccountCreationErrorMessages.MINIMUM_USERNAME_LENGTH_ERROR
    assert len(password) >= enum.AccountCreationRequirements.MINIMUM_PASSWORD_LENGTH, enum.AccountCreationErrorMessages.MINIMUM_PASSWORD_LENGTH_ERROR
    
    assert get_account_by_username(username) is None, "An account with this username already exists!"
    assert email is None or get_account_by_email(email) is None, "An account with this email already exists!"
    
    keys, salt = secure.hash_password(
        password,
        num_hashes=2
    )

    account_password: bytes = keys[0]
    encryption_password: bytes = keys[1]

    plain_data = json.dumps(enum.AccountDataTemplates.PLAIN)
    secure_data = json.dumps(enum.AccountDataTemplates.SECURE).encode()

    safe_secure_data, nonce = secure.aes_encrypt_data(encryption_password, secure_data)

    account_wrapper = wrapper.AccountWrapper(
        model.Account.create(
            username=username,
            email=email,

            password=account_password.hex(),

            plain=plain_data,
            secure=safe_secure_data.hex(),

            salt=salt.hex(),
            nonce=nonce.hex()
        )
    )

    account_wrapper.account_model.save()

    return account_wrapper