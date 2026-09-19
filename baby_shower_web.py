import streamlit as st
from supabase import create_client
supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"])
st.markdown("""
<style>
.stApp {background-color: #f3f8fc;}

h1, h2, h3 {color: #52789b;}

.stButton > button {background-color: #7fa9ca;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 10px 20px;}

.stButton > button:hover {background-color: #608bab;
    color: white;}
</style>
""", unsafe_allow_html=True)
st.image("encabezado_bruno_balam.png",
    use_container_width=True)
st.markdown("""
<div style="text-align: center;">
    <h1>Confirmación de Baby Shower</h1>
    <h3>Blanch & Tona esperan a Bruno Balam</h3>
    <p>¡Acompáñanos a celebrar su llegada!</p>
    <p style="color: #7d8790;">
        14 de noviembre de 2026 | 10:00 a. m. a 2:00 p. m.
    </p>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center;">
    <p><strong>📍 Calz. de Tlalpan 3059</strong><br>
    Sta. Úrsula Coapa, Coyoacán, CDMX</p>
</div>
""", unsafe_allow_html=True)
columna_izquierda, columna_centro, columna_derecha = st.columns([1, 2, 1])

st.markdown("<p style='text-align: center; color: #b07d42;'><strong>Confirma tu asistencia antes del 30 de octubre</strong></p>",
    unsafe_allow_html=True)

with columna_centro:
    st.link_button("📍 Ver ubicación en Google Maps",
        "https://maps.google.com/?q=19.312031,-99.140984",
        use_container_width=True )
st.divider()
nombre= st.text_input("Nombre de quien confirma")
telefono = st.text_input ("Número de quien confirma")
asistencia = st.radio("¿Asistirás?", ["Sí", "No"])

if asistencia=="Sí":
    personas= st.number_input("Número total de personas, incluyéndote", min_value=1, step=1)
else:
    personas = 0

mensaje= st.text_area("Mensaje para los papás (opcional)")

boton = st.button("Confirmar asistencia")
if boton:
    if nombre=="" or telefono=="":
        st.error("Por favor escribe tu nombnre y teléfono.")
    else:
        datos = {"nombre": nombre,
            "telefono": telefono,
            "asistencia": asistencia,
            "personas": personas,
            "mensaje": mensaje }

        supabase.table("confirmaciones").upsert(
            datos,
            on_conflict="telefono").execute()

        st.success("¡Gracias! Tu respuesta quedó guardada.")
