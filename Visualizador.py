import streamlit as st
from PIL import Image
from pandas import read_csv
import json

class Cliente:
    def Imagem(img):
        return st.image(Image.open(img))
    
    def CSV(csv):
        df = read_csv(csv)
        return st.dataframe(df)

    def JSON(arq_json):
        return st.json(json.loads(arq_json.read()))
