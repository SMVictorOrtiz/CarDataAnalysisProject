import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Visualizador de datos')
st.dataframe(car_data)

if st.checkbox("Filtrar fabricantes con menos de 1000 registros"):
    # Contar el número de ocurrencias por fabricante
    manufacturer_counts = car_data['manufacturer'].value_counts()
    # Filtrar fabricantes con menos de 1000 registros
    filtered_manufacturers = manufacturer_counts[manufacturer_counts < 1000].index
    # Filtrar el DataFrame
    data = car_data[~car_data['manufacturer'].isin(filtered_manufacturers)]

hist_button = st.button('Construir histograma')
if hist_button: # al hacer clic en el botón
            # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

fig = px.scatter(data, 
                 x='odometer', 
                 y='price', 
                 color='fuel', 
                 hover_data=['model', 'model_year', 'condition', 'transmission'],
                 title='Precio vs Odometer')

# Mostrar el gráfico en la aplicación
st.plotly_chart(fig)

# Mostrar estadísticas básicas de los datos
st.write("Estadísticas básicas:")
st.write(data.describe())