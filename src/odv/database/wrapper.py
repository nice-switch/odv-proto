import json

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

        
    def get_plain_dictionary(self) -> dict:
        return json.loads(self.account_model.plain)

    
    def get_secure_dictionary(self, password: str) -> dict:
        account_password = bytes.fromhex(self.account_model.password)

        hashes, _ = secure.hash_password(
            password=password,
            override_salt=bytes.fromhex(self.account_model.salt),
            num_hashes=2
        )

        assert hashes[0] == account_password, "Wrong password!"

        decrypted_secure = secure.aes_decrypt_data(
            hashes[1],
            nonce=bytes.fromhex(self.account_model.nonce),
            data=bytes.fromhex(self.account_model.secure)
        )

        return json.loads(decrypted_secure)