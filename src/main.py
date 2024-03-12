import odv

# TODO
"""
    MAKE DATABASE STUFF! (ENCRYPTION LAST!)
"""

odv.database.model.change_database_to(
    odv.enum.DatabaseConnection.DEVELOPMENT
)

account = odv.database.create_account(
    "test_account",
    "test_password"
)

