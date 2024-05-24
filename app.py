import pandas as pd
import plotly.express as px
import streamlit as st

#título 
"Gráfico venta carros"

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Crear un botón
hist_button = st.button('Construir gráficos')

if hist_button:  # Al hacer clic en el botón
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

 # Escribir un mensaje
    st.write('Creación de un gráfico para el conjunto de datos de venta de coches')

# Crear un gráfico de barras
bar_fig = px.bar(car_data, x='model_year', y='price')

# Mostrar el gráfico de barras
st.plotly_chart(bar_fig)

