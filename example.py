"""
Ejemplo de cifrado y descifrado con AES (modo CBC), usando pycryptodome.
Version corregida y actualizada a Python 3.
"""

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import base64


def generate_secret_key_for_AES_cipher():
    # La clave AES debe tener 16, 24 o 32 bytes
    AES_key_length = 16  # usar un valor mas grande en produccion (32 = AES-256)
    secret_key = get_random_bytes(AES_key_length)
    encoded_secret_key = base64.b64encode(secret_key)
    return encoded_secret_key


def encrypt_message(private_msg, encoded_secret_key):
    secret_key = base64.b64decode(encoded_secret_key)

    # Modo CBC requiere un IV (vector de inicializacion) aleatorio
    cipher = AES.new(secret_key, AES.MODE_CBC)

    # Convertimos el mensaje a bytes y lo rellenamos (padding automatico)
    padded_msg = pad(private_msg.encode("utf-8"), AES.block_size)
    encrypted_msg = cipher.encrypt(padded_msg)

    # Guardamos el IV junto con el mensaje cifrado (se necesita para descifrar)
    encoded_iv = base64.b64encode(cipher.iv)
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)

    return encoded_encrypted_msg, encoded_iv


def decrypt_message(encoded_encrypted_msg, encoded_secret_key, encoded_iv):
    secret_key = base64.b64decode(encoded_secret_key)
    encrypted_msg = base64.b64decode(encoded_encrypted_msg)
    iv = base64.b64decode(encoded_iv)

    cipher = AES.new(secret_key, AES.MODE_CBC, iv=iv)

    decrypted_padded_msg = cipher.decrypt(encrypted_msg)
    decrypted_msg = unpad(decrypted_padded_msg, AES.block_size)

    return decrypted_msg.decode("utf-8")


####### INICIO #######

private_msg = (
    "Lorem ipsum dolor sit amet, malis recteque posidonium ea sit, "
    "te vis meliore verterem. Duis movet comprehensam eam ex, te mea "
    "possim luptatum gloriatur. Modus summo epicuri eu nec. "
    "Ex placerat complectitur eos."
)

secret_key = generate_secret_key_for_AES_cipher()
encrypted_msg, iv = encrypt_message(private_msg, secret_key)
decrypted_msg = decrypt_message(encrypted_msg, secret_key, iv)

print(f"Secret Key: {secret_key} - ({len(secret_key)})")
print(f"IV: {iv} - ({len(iv)})")
print(f"Encrypted Msg: {encrypted_msg} - ({len(encrypted_msg)})")
print(f"Decrypted Msg: {decrypted_msg} - ({len(decrypted_msg)})")
