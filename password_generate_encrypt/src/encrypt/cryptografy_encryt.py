from cryptography.fernet import Fernet

texto = "$!FUFuhguioshgifvigisyfisfiogafiygU8t808rg89gpi_6fg64654hb_"


# Genera una llave en formato de secuencia de bits 

key = Fernet.generate_key()
objecto_cifrado=Fernet(key)
texto_encriptado= objecto_cifrado.encrypt(str.encode(texto))
print(texto_encriptado)

texto_desencriptado_bytes= objecto_cifrado.decrypt(texto_encriptado)
print(texto_desencriptado_bytes)

texto_desencriptado=texto_desencriptado_bytes.decode()
print(texto_desencriptado, type(texto_desencriptado))