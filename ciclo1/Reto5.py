def casos_positivos(ruta_archivo: str)-> dict:
    import pandas as pd
    
    if ruta_archivo.split('.')[-1] != 'csv':
        return 'Extension invalida.'

    csv= pd.read_csv(ruta_archivo)
    
    df = pd.DataFrame(csv)
    
    df ['POR_INFEC_MUJER'] = round(df['INFECTADO_MUJER']*100/df['TOTAL_GENERAL'],2)
    df ['POR_INFEC_HOMBRE'] = round(df['INFECTADO_HOMBRE']*100/df['TOTAL_GENERAL'],2)
    df ['POR_REC_MUJER'] = round(df['RECUPERADO_MUJER']*100/df['TOTAL_GENERAL'],2)
    df ['POR_REC_HOMBRE'] = round(df['RECUPERADO_HOMBRE']*100/df['TOTAL_GENERAL'],2)
    
    df1 = df.groupby(['DEPARTAMENTOS'])[['POR_INFEC_MUJER','POR_INFEC_HOMBRE','POR_REC_MUJER','POR_REC_HOMBRE']].sum()
    df2 = df1.to_dict()
    
    return df2


print(casos_positivos('https://raw.githubusercontent.com/PaulaAndresOli/P1/main/casos_positivos_colombia.csv'))