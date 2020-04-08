import csv

# Comentario

# Leer con reader línea a línea accediendo por índices
fileR = './data/Cap1/subvenciones.csv'
fileW = './data/Cap1/subvenciones_esc1.csv'
with open(fileR, encoding='latin1') as fichero_L, open(fileW, 'w', encoding='latin1') as fichero_W:
    lector = csv.reader(fichero_L)
    cabeceras = next(lector, None)
    cabeceras.append('Justificación requerida')
    cabeceras.append('Justificación recibida')

    writer = csv.writer(fichero_W, delimiter=',')
    writer.writerow(cabeceras)

    for linea in lector:
        subvencion = float(linea[2])
        if (subvencion > 300):
            linea.append('Sí')
        else:
            linea.append('No')

        linea.append('No')
        print(linea)
        writer.writerow(linea)


# Leer con DictReader permitiendo acceso por nombres de columna como
# diccionario
fileR = './data/Cap1/subvenciones.csv'
fileW = './data/Cap1/subvenciones_esc2.csv'
with open(fileR, encoding='latin1') as fichero_L, open(fileW, 'w', encoding='latin1') as fichero_W:
    lector = csv.DictReader(fichero_L)

    cabeceras = lector.fieldnames + \
        ['Justificación requerida', 'Justificación recibida']

    escritor = csv.DictWriter(fichero_W, cabeceras)
    escritor.writeheader()

    for linea in lector:
        subvencion = float(linea['Importe'])
        if (subvencion > 300):
            linea['Justificación requerida'] = 'Sí'
        else:
            linea['Justificación requerida'] = 'No'

        linea['Justificación recibida'] = 'No'
        escritor.writerow(linea)
