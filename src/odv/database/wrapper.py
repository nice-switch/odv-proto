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

        return hash == account_password


    def get_public_dictionary(self) -> dict:
        return json.loads(self.account_model.public)
    

    def set_public_dictionary(self, data: dict) -> bool:
        self.account_model.public = json.dumps(data)
        self.account_model.save()

        return True

        
    def get_plain_dictionary(self) -> dict:
        return json.loads(self.account_model.plain)


    def set_plain_dictionary(self, password: str, data: dict) -> bool:
        assert self.authorize_with_password(password)

        self.account_model.plain = json.dumps(data)
        self.account_model.save()

        return True

    
    def get_secure_dictionary(self, password: str) -> dict:
        account_password = bytes.fromhex(self.account_model.password)

        hashes, _ = secure.hash_password(
            password=password,
            override_salt=bytes.fromhex(self.account_model.salt),
            num_hashes=2
        )

        compare_password = hashes[0]
        encryption_password = hashes[1]

        assert compare_password == account_password, "Wrong password!"

        decrypted_secure = secure.aes_decrypt_data(
            password=encryption_password,
            nonce=bytes.fromhex(self.account_model.nonce),
            data=bytes.fromhex(self.account_model.secure)
        )

        return json.loads(decrypted_secure)
    

    def set_secure_dictionary(self, password: str, data: dict) -> bool:
        assert self.authorize_with_password(password), "Wrong password!"

        hashes, salt = secure.hash_password(password, num_hashes=2)

        account_password, encryption_password = hashes[0], hashes[1]

        encrypted_data, nonce = secure.aes_encrypt_data(
            encryption_password,
            json.dumps(data).encode()
        )

        self.account_model.password = account_password.hex()
        self.account_model.salt = salt.hex()

        self.account_model.secure = encrypted_data.hex()
        self.account_model.nonce = nonce.hex()

        self.account_model.save()

        return True

