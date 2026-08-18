# Importar Librerías necesarias

from fastapi import FastAPI #Permite la creación de la API
from pydantic import BaseModel #Define los datos que usa la API
import joblib #Permite cargar el modelo
import pandas as pd 
import uvicorn # Permite ejecutar la FastAPI
import os

# Definir los datos que se van a recibir
# Creación de una clase (Los datos y su categorización. Se utilizaran cuando se haga una predicción por el usuario.)

class DatosAgua(BaseModel): 
    DBO_mg_L: float
    DQO_mg_L: float
    SST_mg_L: float
    COLI_FEC_NMP_100mL: float
    E_COLI_NMP_100mL: float
    OD_PORC: float
    OD_PORC_SUP: float
    TOX_D_48_UT: float
    TOX_V_15_UT: float
    TOX_FIS_SUP_15_UT: float
    LATITUD: float
    LONGITUD: float
    GRUPO: str
    ORGANISMO_DE_CUENCA: str

#Creación de la Aplicación y Carga del Modelo

app = FastAPI(
    title="API de Calidad de Aguas Superficiales",
    description="Predicción de la calidad de aguas superficiales utilizando clasificación de semáforo",
    version="1.0"
)

#Carga del modelo
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
try:
    ruta_modelo = os.path.join(base_dir, "models", "modelo_semaforo_agua.pkl")
    ruta_encoder = os.path.join(base_dir, "models", "label_encoder_semaforo.pkl")
    
    modelo = joblib.load(ruta_modelo)
    encoder = joblib.load(ruta_encoder)
    print("Modelo cargado correctamente")
except Exception as e:
    print(f"Error al cargar el modelo: {e}")
    modelo = None
    encoder = None

#Endpoint Bienvenida
@app.get("/")
def inicio():
    return {"mensaje": "Calidad de Aguas Superficiales. Usa /predict para hacer predicciones"}

# Endpoint para UptimeRobot (health check)
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API funcionando correctamente"}

# Endpoint de Prediccción

@app.post("/predict")
def predecir(datos: DatosAgua):
    if modelo is None or encoder is None:
        return {"error": "El modelo no está disponible"}
    
    entrada = pd.DataFrame([{
        "DBO_mg/L": datos.DBO_mg_L,
        "DQO_mg/L": datos.DQO_mg_L,
        "SST_mg/L": datos.SST_mg_L,
        "COLI_FEC_NMP_100mL": datos.COLI_FEC_NMP_100mL,
        "E_COLI_NMP_100mL": datos.E_COLI_NMP_100mL,
        "OD_PORC": datos.OD_PORC,
        "OD_PORC_SUP": datos.OD_PORC_SUP,
        "TOX_D_48_UT": datos.TOX_D_48_UT,
        "TOX_V_15_UT": datos.TOX_V_15_UT,
        "TOX_FIS_SUP_15_UT": datos.TOX_FIS_SUP_15_UT,
        "LATITUD": datos.LATITUD,
        "LONGITUD": datos.LONGITUD,
        "GRUPO": datos.GRUPO,
        "ORGANISMO_DE_CUENCA": datos.ORGANISMO_DE_CUENCA
    }])
    
    try:
        prediccion_codigo = modelo.predict(entrada)[0]
        resultado = encoder.inverse_transform([prediccion_codigo])[0]
        return {"prediccion": resultado}
    except Exception as e:
        return {"error": f"Error en la predicción: {str(e)}"}