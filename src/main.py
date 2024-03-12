import odv

odv.database.model.change_database_to(
    odv.enum.Database.DEVELOPMENT,
    create_tables=True
)

odv.database.get_account_by_username("test_username") or odv.database.create_account("test_username", "test_password", "test@email.com")

if __name__ == "__main__":
    odv.start(
        odv.enum.Database.DEVELOPMENT,
        "127.0.0.1",
        8080
    )


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

print(account.get_secure_dictionary("test_password"))

account.set_secure_dictionary(
    password = "test_password",
    data = {
        "Hello": "world!"
    }
)

print(account.get_secure_dictionary("test_password"))
"""

