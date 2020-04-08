import csv

# Comentario

# Leer con reader línea a línea accediendo por índices
with open('./data/Cap1/subvenciones.csv', encoding='latin1') as fichero_csv:
    lector = csv.reader(fichero_csv)
    next(lector, None)
    asociaciones = {}
    for linea in lector:
        centro = linea[0]
        subvencion = float(linea[2])
        if centro in asociaciones:
            asociaciones[centro] = asociaciones[centro] + subvencion
        else:
            asociaciones[centro] = subvencion
    print(asociaciones)


# Leer con DictReader permitiendo acceso por nombres de columna como
# diccionario
with open('../../data/Cap1/subvenciones.csv', encoding='latin1') as fichero_csv:
    dict_lector = csv.DictReader(fichero_csv)
    asociaciones = {}
    for linea in dict_lector:
        centro = linea['Asociación']
        subvencion = float(linea['Importe'])
        if centro in asociaciones:
            asociaciones[centro] = asociaciones[centro] + subvencion
        else:
            asociaciones[centro] = subvencion
    print(asociaciones)
