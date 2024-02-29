from geopy.distance import geodesic 

import pandas as pd
# Especifica la ruta del archivo
archivo_agentes_observados = 'AgentesObservados.xlsx'
archivo_agentes_instalados2023= 'AgentesInstalados2023.xlsx'
# Lee el archivo XLSX en un DataFrame de pandas

df = pd.read_excel(archivo_agentes_observados)
df1 = pd.read_excel(archivo_agentes_instalados2023)

df["Coordeandas Final"]= round(df["coordenada y"],4).astype(str) +","+ round(df["coordenada x "],4).astype(str)
#df_subset=df.iloc[:,[0,2,3,26]]
lista_obser= list(zip(df["Terminal"],df["coordenada y"],df["coordenada x "]))
lista_ins_2023= list(zip(df1["COD_TERMINAL"],df1["COORDENADA Y"],df1["COORDENADA X"], df1["TOTAL_TRX_MES"], df1["PAGO_SERVICIOS"]))
cercania=[]

for coordenadas in lista_obser:
    
    for coordenas2 in lista_ins_2023:
        latitud1=coordenadas[1]
        longitud1=coordenadas[2]
        latitud2=coordenas2[1]
        longitud2=coordenas2[2]
        punto1= (latitud1,longitud1)
        punto2= (latitud2,longitud2)
        distancia=geodesic((latitud1,longitud1),(latitud2,longitud2)).m
        if distancia < 300.00:
            cercania.append((coordenadas[0],distancia,coordenas2[0],coordenas2[3],coordenas2[4]))
        
    #print(f"({latitud1},{longitud1}) y ({latitud2} ,{longitud2})")

nombre_columnas=["Termianl_Observado","Distancia","Termianl_Ins_2023","Total_Trax","Total_PDS"]
df_fianl= pd.DataFrame (cercania, columns=nombre_columnas)        
#df_fianl.to_excel("Agentes_Cercanos_300.xlsx",sheet_name="Cruce Instalacion 2023")


#punto1= (latitud1,longitud1)
#punto2= (latitud2,longitud2)

#distancia=geodesic((latitud1,longitud1),(latitud2,longitud2))
print(df_fianl)
