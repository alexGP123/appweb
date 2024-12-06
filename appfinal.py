import pandas as pd
import streamlit as st

# Cargar datos con caché
@st.cache_data
def load_data(nrows):
    data = pd.read_csv('C:/Users/User/Downloads/1715722281738-dataset.csv', nrows=nrows)
    return data

# Título de la aplicación
st.title("Aplicación de Streamlit con Pandas")

# Cargar el dataset
data = load_data(1000)  # Puedes ajustar el número de filas a cargar

# Control de entrada de texto para buscar nombres
myname = st.text_input('Teclea un nombre o las primeras letras de un nombre:')

# Botón para buscar
if st.button('Buscar'):
    if myname:
        # Filtrar el DataFrame por el nombre ingresado
        filtered_data = data[data['name'].str.contains(myname, case=False)]
        st.write(f"Nombres encontrados: {len(filtered_data)}")
        st.dataframe(filtered_data)
    else:
        st.write("Por favor, ingresa un nombre para buscar.")

# Control selectbox para filtrar por sexo
selected_sex = st.selectbox("Selecciona el sexo", data['sex'].unique())

# Botón para filtrar por sexo
if st.button('Filtrar por sexo'):
    filtered_data_sex = data[data['sex'] == selected_sex]
    st.write(f"Número de {selected_sex}: {len(filtered_data_sex)}")
    st.dataframe(filtered_data_sex)