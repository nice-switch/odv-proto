from odv.database import model


class AccountWrapper():
    def __init__(self, account_model: model.Account):
        self.account_model = account_model

        