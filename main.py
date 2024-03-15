import streamlit as st
from PIL import Image


st.markdown('# Visualizador de Arquivos')


config_types={
    'jpg':lambda img: st.image(Image.open(img)),
    'png':2
}

data = st.file_uploader(
    label = 'Selecionar Arquivo',
    type = config_types.keys()
                        )

if data:
    config_types[data.name.split('.')[1]](data)
    #st.image(Image.open(data))


