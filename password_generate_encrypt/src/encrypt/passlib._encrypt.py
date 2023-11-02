from passlib.context import CryptContext

# Round : Iteraciones para reducir la posibilidad de cracking.
contexto = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=3000
)


#texto que simula un password
texto = "$!FUFuhguioshgifvigisyfisfiogafiygU8t808rg89gpi_6fg64654hb_"

#ENCRIPTACION
texto_encriptado = contexto.hash(texto)

#Impreción del password (texto) encriptado
print(texto_encriptado)

#Comprobación de que el texto original sea igual al texto encriptado (True)
print(contexto.verify(texto, texto_encriptado))