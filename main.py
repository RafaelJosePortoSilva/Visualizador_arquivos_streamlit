import streamlit as st
from Visualizador import Cliente as viewer
st.markdown('# Visualizador de Arquivos')


config_types={
    'jpg':lambda img: viewer.Imagem(img),
    'png':lambda img: viewer.Imagem(img),
    'csv':lambda csv: viewer.CSV(csv),
    'json':lambda json: viewer.JSON(json),
    'mp3':lambda mp3: viewer.MP3(mp3),
    'mp4':lambda mp4: viewer.MP4(mp4)
}

data = st.file_uploader(
    label = 'Selecionar Arquivo',
    type = config_types.keys()
                        )

if data:
    config_types[data.name.split('.')[1]](data)

else:
    st.error('Nenhum arquivo adicionado')
