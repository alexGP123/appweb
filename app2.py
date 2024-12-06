import pandas as pd
import streamlit as st

# Cargar los datos
@st.cache_data
def load_data(nrows):
    DATA_URL = '1715721906602-uber_dataset.csv' 
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data['Date/Time'] = pd.to_datetime(data['Date/Time'])  # Convertir a tipo fecha
    return data

# Cargar solo una muestra de datos
data = load_data(10000)  

# Título de la aplicación
st.title("Viajes de Uber en Nueva York")
st.header("Análisis de viajes de Uber con filtros por hora")

# Control deslizante para seleccionar la hora
hour_to_filter = st.slider("Selecciona la hora del día:", 0, 23, 12)  

# Filtrar los datos por la hora seleccionada
filtered_data = data[data['Date/Time'].dt.hour == hour_to_filter]

# Renombrar las columnas para que sean compatibles con st.map
filtered_data = filtered_data.rename(columns={'Lat': 'lat', 'Lon': 'lon'})

# Mostrar el mapa con los viajes filtrados
st.map(filtered_data[['lat', 'lon']])