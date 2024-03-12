import odv

# TODO
"""
    MAKE DATABASE STUFF! (ENCRYPTION LAST!)
"""

odv.database.model.change_database_to(
    database=odv.enum.Database.DEVELOPMENT,
    create_tables=True
)

print(odv.database.generic_peewee_get(
    odv.database.model.Account,
    odv.database.model.Account.username,
    "test_username"
))

#account = odv.database.create_account(
#    "test_username",
#    "test_password"
#)
#print(account.account_model.username)
