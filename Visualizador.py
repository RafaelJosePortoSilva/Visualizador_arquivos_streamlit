import streamlit as st
from PIL import Image
from pandas import read_csv
from json import loads

class Cliente:

    def Imagem(img):
        return st.image(Image.open(img))

    def CSV(csv):
        df = read_csv(csv)
        return st.dataframe(df)

    def JSON(json):
        return st.json(loads(json.read()))

    def MP3(mp3):
        return st.audio(mp3)

    def MP4(mp4):
        return st.video(mp4)
