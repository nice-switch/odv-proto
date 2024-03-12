from odv import enum

from Crypto.Protocol.KDF import scrypt
from Crypto.Cipher import AES

from Crypto.Random import get_random_bytes


def hash_password(password: str | bytes, override_salt: bytes | None = None, num_hashes: int | None = 1) -> tuple[bytes, bytes] | tuple[list[bytes], bytes]:
    password = type(password) is str and password.encode() or password
    salt = override_salt or get_random_bytes(enum.SaltParams.SALT_LENGTH)

    hashes = scrypt(
        password, 
        salt, 
        enum.ScryptParams.KEY_LENGTH, 
        enum.ScryptParams.N,
        enum.ScryptParams.R,
        enum.ScryptParams.P,
        num_keys=num_hashes
    )

    return hashes, salt


def aes_encrypt_data(password: bytes, data: bytes) -> tuple[bytes, bytes]:
    cipher = AES.new(password, mode=AES.MODE_EAX)
    return cipher.encrypt(data), cipher.nonce


def aes_decrypt_data(password: bytes, nonce: bytes, data: bytes) -> bytes | None:
    cipher = AES.new(password, mode=AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt(data)