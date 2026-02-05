import pandas as pd
import plotly.express as px
import streamlit as st


# agregar un encabezado
st.header("Esta es mi app del proyecto :green[Sprint 7]", divider="gray")

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.checkbox('Construir histograma')  # crear un botón
dist_button = st.checkbox('Construir diagrama de dispersión')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer", labels={
        "odometer": "Odómetro (millas)"
    },
        title="Distribución del Odómetro"
    )  # crear un histograma

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, width="stretch")

if dist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un diagrama de dispersión
    fig = px.scatter(car_data, x="odometer", y="price", labels={
        "odometer": "Odómetro (millas)",
        "price": "Precio del vehículo (USD)"},
        title="Precio vs Odómetro"
    )  # crear un gráfico de dispersión

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, width="stretch")

st.write('¡Gracias por usar mi app! :smile:')  # mensaje de agradecimiento
