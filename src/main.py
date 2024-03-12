import odv

# TODO
"""
    MAKE DATABASE STUFF! (ENCRYPTION LAST!)
"""

odv.database.model.change_database_to(
    database=odv.enum.Database.DEVELOPMENT,
    create_tables=True
)

account: odv.database.wrapper.AccountWrapper

try:
    account = odv.database.create_account(
        "test_username",
        "test_password",
        "test@email.com"
    )
except Exception as _:
    account = odv.database.get_account_by_username(
        "test_username"
    )

print(account.authorize_with_password("test_password"))

