import requests
import predict
from pyngrok import ngrok

public_url = ngrok.connect(port='8501')

import streamlit as st
st.title('Primonz')
p_image_url = st.text_input("ลิ้งค์ภาพ: ")
aw = imgurl(p_image_url)
st.text(str(aw))

def imgurl(p_image_url: str):
  #file#Image.open(image.file)
  r = requests.get(p_image_url, allow_redirects=True)
  with open("file2.png",'wb') as f:
      f.write(r.content)
  name = "file2.png"
  char = predict.answer(name)
  return {"name":str(char)}

