import streamlit as st
from supabase import create_client
supabase = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"])
st.title("Confirmacion de Baby Shower")
nombre= st.text_input("Nombre de quien confirma")
telefono = st.text_input ("Número de quien confirma")
asistencia = st.radio("¿Asistirás?", ["Sí", "No"])

if asistencia=="Sí":
    personas= st.number_input("Número total de personas, incluyendote", min_value=1, step=1)
else:
    personas = 0

mensaje= st.text_area("Mensaje para los papás (Opcional)")

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
