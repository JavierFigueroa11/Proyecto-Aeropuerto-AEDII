import pandas as pd
import pprint

def vertices():
    #Pongan el directorio de donde tengan el archivo o el nombre del archivo solo si lo tienen en la misma carpeta
    df=pd.read_csv("D:\Archivos de Gonzalo\Proyecto AED II\AeropuertosArg.csv",header=None,names=["ID","Nombre","Ciudad","Provincia","Latitud","Longitud"])
    df2=pd.read_csv("D:\Archivos de Gonzalo\Proyecto AED II\RutasAeropuertosAleatorio.csv",names=["Origen","Destino"])


    lista=[]
    for index,row in df.iterrows():
        lista.append(row["ID"])
    vertices=dict.fromkeys(lista)

    rutitas = dict()

    for row in df2.itertuples():
        if row[1] in rutitas:
            rutitas[row[1]].append(row[2])
        else:
            rutitas[row[1]]=[row[2]]

    keys=rutitas.keys()

    for x in range(1,25):
        if x not in keys:
            rutitas[x]=[]

    #pprint.pprint(rutitas)
    return rutitas
