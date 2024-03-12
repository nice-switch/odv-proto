from odv.database import model, secure


class AccountWrapper():
    def __init__(self, account_model: model.Account):
        self.account_model = account_model
        

    
    def authorize_with_password(self, password: str) -> bool:
        account_password = bytes.fromhex(self.account_model.password)

        hash, _ = secure.hash_password(
            password=password,
            override_salt=bytes.fromhex(self.account_model.salt)
        )

        if hash == account_password:
            return True
        
        return False

        
