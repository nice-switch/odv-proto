import odv

# TODO
"""
    MAKE DATABASE STUFF! (ENCRYPTION LAST!)
"""

odv.database.model.change_database_to(
    database=odv.enum.Database.DEVELOPMENT,
    create_tables=True
)

account = odv.database.create_account(
    "test_username",
    "test_password"
)

