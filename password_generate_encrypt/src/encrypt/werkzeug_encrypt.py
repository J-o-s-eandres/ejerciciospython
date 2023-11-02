from werkzeug.security import generate_password_hash , check_password_hash

# check_password_hash sirve para cifrar la contraseña -> recibe el texto a encriptar , el algoritmo y la cantidad de iteraciones 
# check_password_hash sirve para comprobar si un valor cifrado coincide con un valor original (antes de cifrar) -> recibre el texto cifrado y el origen


#texto que servira para simular el password
texto = "$!FUFuhguioshgifvigisyfisfiogafiygU8t808rg89gpi_6fg64654hb_"


#prueba de generate_password_hash, con diferentes conbinaciones 
text_encriptado1 = generate_password_hash(texto)
text_encriptado2 = generate_password_hash(texto, 'sha256')
text_encriptado3 = generate_password_hash(texto, 'sha256', 30)
text_encriptado4 = generate_password_hash(texto, 'pbkdf2:sha256')
text_encriptado5 = generate_password_hash(texto, 'pbkdf2:sha256', 30)
text_encriptado6 = generate_password_hash(texto, 'pbkdf2:sha256:30', 30)


#impresión de los passwords (textos) encriptados
print(text_encriptado1)
print(text_encriptado2)
print(text_encriptado3)
print(text_encriptado4)
print(text_encriptado5)
print(text_encriptado6)



#comprobación de que los textos encriptados sean igual al texto de origen (True)
print(check_password_hash(text_encriptado1, texto))
print(check_password_hash(text_encriptado2, texto))
print(check_password_hash(text_encriptado3, texto))
print(check_password_hash(text_encriptado4, texto))
print(check_password_hash(text_encriptado5, texto))
print(check_password_hash(text_encriptado6, texto))