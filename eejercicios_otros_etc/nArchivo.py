#obtener la extension  de un archivo especifico por el usuario

nombre_archivo = input('Ingrese el nombre del archivo: ')

parte_nombre_archivo = nombre_archivo.split('.')


#print("La extension del archivo {} es {} ".format(nombre_archivo,parte_nombre_archivo[-1]))

if parte_nombre_archivo[-1] == 'py':
    print("La extension del archivo {} es {} ".format(nombre_archivo,parte_nombre_archivo[-1]))
    print("Extension de python")
    
elif parte_nombre_archivo[-1] =='jpeg':
    print("La extension del archivo {} es {} ".format(nombre_archivo,parte_nombre_archivo[-1]))
    print("Extension de imagen")

elif parte_nombre_archivo[-1] =='xlsx':
    print("La extension del archivo {} es {} ".format(nombre_archivo,parte_nombre_archivo[-1]))
    print("Extension excel")

elif parte_nombre_archivo[-1] =='pbix':
    print("La extension del archivo {} es {} ".format(nombre_archivo,parte_nombre_archivo[-1]))
    print("Extension Power bi")

elif parte_nombre_archivo[-1] =='docx':
    print("La extension del archivo {} es {} ".format(nombre_archivo,parte_nombre_archivo[-1]))
    print("Extension word")

else:
    print('Sadra Dios que extension es esa')