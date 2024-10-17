import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Visualizador de datos')
st.dataframe(car_data)
    
hist_button = st.button('Construir histograma')
if hist_button: 
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

fig = px.scatter(car_data, 
                 x='odometer', 
                 y='price', 
                 color='fuel', 
                 hover_data=['model', 'model_year', 'condition', 'transmission'],
                 title='Precio vs Odometer')

# Mostrar el gráfico en la aplicación
st.plotly_chart(fig)

# Mostrar estadísticas básicas de los datos
st.write("Estadísticas básicas:")
st.write(car_data.describe())
