from xlrd import open_workbook, colname
import xlwt

with open_workbook('./data/Cap1/subvenciones.xls', on_demand=True) as libro_lect:
    asociaciones = {}
    libro_escr = xlwt.Workbook()
    for nombre in libro_lect.sheet_names():
        hoja_lect = libro_lect.sheet_by_name(nombre)
        hoja_escr = libro_escr.add_sheet(nombre)
        for i in range(hoja_lect.nrows):
            for j in range(hoja_lect.ncols):
                hoja_escr.write(i, j, hoja_lect.row(i)[j].value)
            if i != 0:
                fila = hoja_lect.row(i)
                centro = fila[0].value
                subvencion = float(fila[2].value)
                if centro in asociaciones:
                    asociaciones[centro] = asociaciones[centro] + subvencion
                else:
                    asociaciones[centro] = subvencion
    hoja_escr = libro_escr.add_sheet('Totales')
    hoja_escr.write(0, 0, "Asociación")
    hoja_escr.write(0, 1, "Importe total")
    hoja_escr.write(0, 2, "Importe justificado")
    hoja_escr.write(0, 3, "Restante")
    for i, clave in enumerate(asociaciones):
        fila = i + 1
        fila_form = i + 2
        hoja_escr.write(fila, 0, clave)
        hoja_escr.write(fila, 1, asociaciones[clave])
        hoja_escr.write(fila, 2, 0)
        hoja_escr.write(fila, 3, xlwt.Formula("C" + str(fila_form) + "-" + "B" + str(fila_form)))
    libro_escr.save('./out/subvenciones_totales.xls')
