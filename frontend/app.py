# Importar librerías
import streamlit as st
import requests 

# Configuraciones de la página
st.set_page_config(
    page_title="Calidad de Aguas Superficiales",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# Personalización CSS

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #e8f4f8 0%, #d4e8f0 100%);
    }
    
    /* Título principal */
    .main-title {
        text-align: center;
        padding: 20px 0 5px 0;
    }
    .main-title h1 {
        font-size: 38px;
        color: #004466;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .main-title p {
        font-size: 16px;
        color: #006699;
        margin: 5px 0 0 0;
    }

# Personalización Párrafo Introductorio

    .intro-box {
        background: white;
        padding: 20px 25px;
        border-radius: 12px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.06);
        border-left: 5px solid #0077b3;
        margin: 10px 0 20px 0;
    }
    .intro-box p {
        margin: 1;
        font-size: 25;
        px;
        color: #333;
        line-height: 1.6;
    }
    .intro-box strong {
        color: #004466;
    }

# Tarjetas para las Columnas

    .tarjeta {
        background: white;
        padding: 20px 20px 10px 20px;
        border-radius: 15px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        border-left: 5px solid #0077b3;
        margin-bottom: 10px;
        transition: transform 0.2s;
    }
    .tarjeta:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 20px rgba(0,0,0,0.12);
    }
    .tarjeta-verde {
        border-left-color: #00a86b;
    }
    .tarjeta-naranja {
        border-left-color: #ff8c00;
    }
    
    .tarjeta .stSubheader {
        color: #004466 !important;
        border-bottom: 2px solid #e0e0e0;
        padding-bottom: 8px;
        margin-bottom: 15px;
    }

# Botón 
    .stButton > button {
        background: linear-gradient(135deg, #0077b3, #004466) !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
        border-radius: 30px !important;
        padding: 12px 40px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0,119,179,0.3) !important;
        transition: all 0.3s ease !important;
        width: 100% !important;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(0,119,179,0.5) !important;
    }

# Presentación de Resultados 
    .stSuccess, .stWarning, .stError {
        border-radius: 15px !important;
        padding: 20px !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08) !important;
    }
    
    .stAlert {
        border-radius: 10px !important;
        border-left: 5px solid #ff8c00 !important;
        background-color: #fff8f0 !important;
    }

# Pie de Página

    .footer {
        text-align: center;
        color: #666;
        font-size: 13px;
        padding: 15px;
        border-top: 1px solid #ddd;
        margin-top: 20px;
    }
    .footer strong {
        color: #004466;
    }
</style>
""", unsafe_allow_html=True)

# Título de la Página

st.markdown("""
<div class="main-title">
    <h1>💧 Modelo de Predicción de la Calidad de Aguas Superficiales 💧</h1>
    <p> Datos CONAGUA | Aguas superficiales de México</p>
</div>
""", unsafe_allow_html=True)

# Párrafo Introductorio

st.markdown("""
<div class="intro-box">
    <p>
        <strong>Información Relevante</strong><br>
        Esta aplicación utiliza un modelo de <strong>Machine Learning</strong> 
         entrenado a partir de datos de CONAGUA para predecir la 
        calidad de aguas superficiales en México. El modelo clasifica las muestras
        utilizando un sistema de <strong>semáforo</strong> (Verde, Amarillo o Rojo) 
        basado en parámetros de diversa índole.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Favor ingresar los parámetros de la muestra para la generación de la predicción.")
st.divider()

# URL de la API
API_URL = "https://aguas-api-55ij.onrender.com/predict"

# Estructuración del Formulario 
# Crear 3 columnas para la introducción de los datos para la predicción.

col1, col2, col3 = st.columns(3)

# Columna 01 -  Parámetros Químicos

with col1:
    st.markdown('<div class="tarjeta">', unsafe_allow_html=True)
    st.subheader("Parámetros Químicos") # Subtitulo de la Columna
    
    dbo = st.number_input( 
        "DBO (mg/L)", 
        min_value=0.0, # Valor mínimo
        value=5.0, #Valor default
        step=0.1, # Incremento
        format="%.2f", # Formato decimales
        help="Introducir Demanda Bioquímica de Oxígeno" # Explicación de la Solicitud para el usuario.
    )
    
    dqo = st.number_input( 
        "DQO (mg/L)", 
        min_value=0.0, 
        value=20.0, 
        step=0.1, 
        format="%.2f", 
        help="Introducir Demanda Química de Oxígeno" 
    )
    
    sst = st.number_input(
        "SST (mg/L)", 
        min_value=0.0, 
        value=20.0, 
        step=0.1, 
        format="%.1f",
        help="Introducir Sólidos Suspendidos Totales"
    )
    
    oxigeno = st.number_input(
        "Oxígeno Disuelto (%)", 
        min_value=0.0, 
        value=80.0, 
        step=0.1, 
        format="%.1f",
        help="Introducir Porcentaje de Oxígeno Disuelto"
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Columna 02 - Parámetros Microbiológicos y Toxicidad

with col2:
    st.markdown('<div class="tarjeta tarjeta-verde">', unsafe_allow_html=True)
    st.subheader("Parámetros Microbiológicos") # Subtitulo de la Columna
    
    coliformes = st.number_input(
        "Coliformes Fecales (NMP/100mL)", 
        min_value=0.0, # Valor mínimo
        value=1000.0, #Valor default
        step=10.0, # Incremento
        format="%.1f", # Formato decimales
        help="Introducir Número Más Probable de Coliformes Fecales" # Asistencia para el usuario
    )
    
    e_coli = st.number_input(
        "E. coli (NMP/100mL)", 
        min_value=0.0, 
        value=100.0, 
        step=10.0, 
        format="%.1f",
        help="Introducir Número Más Probable de Escherichia coli"
    )
    
    st.subheader("Toxicidad") # Subtitulo de la Columna
    
    tox_d48 = st.number_input(
        "Toxicidad D48 (UT)", 
        min_value=0.0, 
        value=0.5, 
        step=0.1, 
        format="%.2f",
        help="Introducir Unidades de Toxicidad a 48 horas"
    )
    
    tox_v15 = st.number_input(
        "Toxicidad V15 (UT)", 
        min_value=0.0, 
        value=0.5, 
        step=0.1, 
        format="%.2f",
        help="Introducir Unidades de Toxicidad a 15 minutos"
    )
    
    tox_fis = st.number_input(
        "Toxicidad FIS (UT)", 
        min_value=0.0, 
        value=0.5, 
        step=0.1, 
        format="%.2f",
        help="Introducir Unidades de Toxicidad FIS"
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Columna 03 - Ubicación Geográfica y Contexto

with col3:
    st.markdown('<div class="tarjeta tarjeta-naranja">', unsafe_allow_html=True)
    st.subheader("Ubicación Geográfica") # Subtitulo de la Columna

    st.info(
        "📍 **Rangos de Limitación Geográfica a México:**\n"
        "- **Latitud:** 14° N a 32° N\n"
        "- **Longitud:** 86° O a 117° O"
    )
    
    latitud = st.number_input(
        "Latitud", 
        min_value=-14.0, # Limitación al sur de México
        max_value=32.0, # Limitación norte de México
        value=20.0, # Aproximación al centro de México
        step=0.001, 
        format="%.3f",
        help="Intruducir Coordenada de Latitud (grados decimales)"
    )
    
    longitud = st.number_input(
        "Longitud", 
        min_value=-117.0, # Limitación Oeste de México
        max_value=-86.0, #Limitación Este de México
        value=-100.0,  # Aproximación al centro de México
        step=0.001, 
        format="%.3f",
        help="Intruducir Coordenada de Longitud (grados decimales)"
    )
    
    st.subheader("Contexto")
    
    grupo = st.selectbox(
        "Grupo",
        ["LOTICO", "LENTICO", "COSTERO"],
        help="Seleccionar Tipo de cuerpo de agua"
    )
    
    organismo = st.selectbox(
        "Organismo de Cuenca",
        [
            "LERMA SANTIAGO PACIFICO",
            "PENINSULA DE BAJA CALIFORNIA",
            "PACIFICO SUR",
            "BALSAS",
            "GOLFO CENTRO",
            "GOLFO NORTE",
            "PACIFICO NORTE",
            "RIO BRAVO",
            "PENINSULA DE YUCATAN",
            "FRONTERA SUR",
            "NOROESTE"
        ],
        help="Seleccionar Organismo de cuenca donde se tomó la muestra"
    )
    st.markdown('</div>', unsafe_allow_html=True)

 # Botón para la Predicción

st.divider()

# Centrar el botón

col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    boton = st.button(
        "Generar Predicción", 
        type="primary", 
        use_container_width=True
    )

# Funcionamiento del botón

if boton:
    # Preparar los datos
    datos = {
        "DBO_mg_L": dbo,
        "DQO_mg_L": dqo,
        "SST_mg_L": sst,
        "COLI_FEC_NMP_100mL": coliformes,
        "E_COLI_NMP_100mL": e_coli,
        "OD_PORC": oxigeno,
        "OD_PORC_SUP": oxigeno,
        "TOX_D_48_UT": tox_d48,
        "TOX_V_15_UT": tox_v15,
        "TOX_FIS_SUP_15_UT": tox_fis,
        "LATITUD": latitud,
        "LONGITUD": longitud,
        "GRUPO": grupo,
        "ORGANISMO_DE_CUENCA": organismo
    }
    
    with st.spinner("Consultando modelo de Machine Learning..."):
        try:
            respuesta = requests.post(API_URL, json=datos, timeout=10)
            
            if respuesta.status_code == 200:
                resultado = respuesta.json()
                prediccion = resultado.get("prediccion", "Error")

                
                # Mostrar el resultado
                st.divider()
                st.subheader("Resultado")
                
                # Centrar el resultado
                col_res1, col_res2, col_res3 = st.columns([1, 2, 1])
                with col_res2:
                    if prediccion == "Verde":
                        st.success(f"### Calidad: **{prediccion}**")
                        st.info("Buena calidad - Cumple con parámetros químicos y microbiológicos aceptables para múltiples usos.")
                    elif prediccion == "Amarillo":
                        st.warning(f"### Calidad: **{prediccion}**")
                        st.warning(" Calidad Media - Algunos parámetros superan los parámetros químicos y microbiológicos aceptables para múltiples usos.")
                    elif prediccion == "Rojo":
                        st.error(f"### Calidad: **{prediccion}**")
                        st.error("❌ Mala calidad - Múltiples parámetros exceden los parámetros químicos y microbiológicos aceptables para múltiples usos.")
                    else:
                        st.info(f"### Calidad: **{prediccion}**")
                
            else:
                st.error(f"Error en la API: {respuesta.status_code}")
                st.write("Detalles:", respuesta.text)
                
        except requests.exceptions.ConnectionError:
            st.error(" No se pudo conectar a la API")
        except Exception as e:
            st.error(f"Error inesperado: {e}") 
# Pie de Página
st.divider()
st.markdown(
    """
    <div class="footer">
         <strong>Modelo de Calidad de Aguas Superficiales</strong> | Módulo 04 | Machine Learning

    </div>
    """,
    unsafe_allow_html=True
)