# test_app.py
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Test",
    page_icon="🧪",
    layout="centered"
)

st.title("🧪 App de prueba")
st.write("Verificando dependencias...")

# Verificar que joblib funciona
try:
    import joblib
    st.success("✅ joblib está instalado correctamente")
except Exception as e:
    st.error(f"❌ Error con joblib: {e}")

# Verificar que pandas funciona
try:
    import pandas as pd
    st.success("✅ pandas está instalado correctamente")
except Exception as e:
    st.error(f"❌ Error con pandas: {e}")

# Verificar que el modelo existe
try:
    with open("models/modelo_semaforo_agua.pkl", "rb") as f:
        st.success("✅ El archivo del modelo existe")
except Exception as e:
    st.error(f"❌ El archivo del modelo NO existe: {e}")

st.write("---")
st.write("Si ves todos los ✅, la app funcionará.")