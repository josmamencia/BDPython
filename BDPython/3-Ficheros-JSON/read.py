import json

with open('./data/Cap1/subvenciones.json', encoding='utf-8') as ficR, open('./out/subvenciones_esc.json', 'w', encoding='utf-8') as ficW:
    datos = json.load(ficR)

    ASOCIACION = "Asociación"
    ACT_SUBV = "Actividad Subvencionada"
    IMPORTE = "Importe en euros"
    lista = []
    lista_activ = []
    asoc_actual = ""
    objeto = {}

    for elem in datos:
        asoc = elem[ASOCIACION]
        activ = elem[ACT_SUBV]
        imp = elem[IMPORTE]

        if asoc_actual != asoc:
            objeto["Actividades"] = lista_activ
            objeto = {"Asociación": asoc}
            lista.append(objeto)
            lista_activ = []
        lista_activ.append({ACT_SUBV: activ, IMPORTE: imp})
        asoc_actual = asoc

    print(lista)
    json.dump(lista, ficW, ensure_ascii=False, indent=4)  # , sort_keys=False
