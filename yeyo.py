def cargar_dataset(archivo):
    import pandas as pd # type: ignore
    import os

    # Obtener la extensión del archivo
    extension = os.path.splitext(archivo)[1].lower()
    
    # Cargar el archivo según su extensión
    if extension == '.csv':
        df = pd.read_csv(archivo)
        return(df)
    elif extension == '.xlsx':
        df = pd.read_excel(archivo)
        return(df)
    elif extension == '.json':
        df = pd.read_json(archivo)
        return(df)
    elif extension == '.html':
        df = pd.read_html(archivo)
        return(df)
    else:
        raise ValueError(f'Formato de archivo no soportado: {extension}')
    
##################################################################################################################################################################
# Sustitución de valores nulos por promedio
def sust_prom(dataframe):
    import pandas as pd

    # Seleccionar columnas cuantitativas con valores nulos
    cuantitativas_con_nulos = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    # Seleccionar columnas cualitativas
    cualitativas = dataframe.select_dtypes(include=['object', 'datetime','category'])
    # Rellenar valores nulos con el promedio de cada columna
    cuantitativas = cuantitativas_con_nulos.fillna(round(cuantitativas_con_nulos.mean(), 1))
    # Concatenar las columnas cuantitativas y cualitativas
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos)

##################################################################################################################################################################
# Sustitución de valores nulos por mediana
def sust_median(dataframe):
    import pandas as pd
    
    # Seleccionar columnas cuantitativas con valores nulos
    cuantitativas_con_nulos = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    # Seleccionar columnas cualitativas
    cualitativas = dataframe.select_dtypes(include=['object', 'datetime','category'])
    # Rellenar valores nulos con la mediana de cada columna
    cuantitativas = cuantitativas_con_nulos.fillna(round(cuantitativas_con_nulos.median(), 1))
    # Concatenar las columnas cuantitativas y cualitativas
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos)

##################################################################################################################################################################
# Sustitución de valores nulos por método ffill
def sust_ffill(dataframe):
    import pandas as pd
    
    # Seleccionar columnas cuantitativas
    cuantitativas = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    # Seleccionar columnas cualitativas con valores nulos
    cualitativas_con_nulos = dataframe.select_dtypes(include=['object', 'datetime','category'])
    # Rellenar valores nulos con el método forward fill
    cualitativas = cualitativas_con_nulos.fillna(method='ffill')
    # Concatenar las columnas cuantitativas y cualitativas
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)

    return(Datos_sin_nulos)

##################################################################################################################################################################
# Sustitución de valores nulos por método bfill
def sust_bfill(dataframe):
    import pandas as pd

    # Seleccionar columnas cuantitativas
    cuantitativas = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    # Seleccionar columnas cualitativas con valores nulos
    cualitativas_con_nulos = dataframe.select_dtypes(include=['object', 'datetime','category'])
    # Rellenar valores nulos con el método backward fill
    cualitativas = cualitativas_con_nulos.fillna(method='bfill')
    # Concatenar las columnas cuantitativas y cualitativas
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos)

##################################################################################################################################################################
# Sustitución de valores nulos por un string concreto
def sust_string(dataframe, cadena):
    import pandas as pd

    # Seleccionar columnas cuantitativas
    cuantitativas = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    # Seleccionar columnas cualitativas con valores nulos
    cualitativas_con_nulos = dataframe.select_dtypes(include=['object', 'datetime','category'])
    # Rellenar valores nulos con una cadena específica
    cualitativas = cualitativas_con_nulos.fillna(cadena)
    # Concatenar las columnas cuantitativas y cualitativas
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos)

##################################################################################################################################################################
# Sustitución de valores nulos por el método de constante
def sust_constante(dataframe, constante):
    import pandas as pd 

    # Seleccionar columnas cuantitativas con valores nulos
    cuantitativas_con_nulos = dataframe.select_dtypes(include=['float64', 'int64','float','int'])
    # Seleccionar columnas cualitativas
    cualitativas = dataframe.select_dtypes(include=['object', 'datetime','category'])
    # Rellenar valores nulos con una constante específica
    cuantitativas = cuantitativas_con_nulos.fillna(constante)
    # Concatenar las columnas cuantitativas y cualitativas
    Datos_sin_nulos = pd.concat([cuantitativas, cualitativas], axis=1)
    
    return(Datos_sin_nulos)

##################################################################################################################################################################
# Conteo de valores nulos por columna y total
def cuenta_valores_nulos(dataframe):
    # Valores nulos por columna
    valores_nulos_cols = dataframe.isnull().sum()
    # Valores nulos totales en el dataframe
    valores_nulos_df = dataframe.isnull().sum().sum()
    
    return("Valores nulos por columna", valores_nulos_cols,
            "Valores nulos por dataframe", valores_nulos_df)