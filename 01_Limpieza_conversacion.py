nombre = "nombre" #se pone aquí el nombre del que se quiera guardar la información. 
with open("archivo_original.txt", "r", encoding = 'utf-8') as archivo_entrada:
    with open("archivo_limpio.txt", "w", encoding = 'utf-8') as archivo_salida:
        for linea in archivo_entrada:
            if nombre + ":" in linea:
                # toma solo lo que está después de "nombre:"
                linea_limpia = linea.split(nombre + ":")[1].strip()
                print(f"Procesando linea: {linea_limpia}") #imprime un mensajeen consola para saber si está bien ejecutado
                archivo_salida.write(linea_limpia + '\n')





