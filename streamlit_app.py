import requests
import predict



def imgurl(p_image_url: str):
  #file#Image.open(image.file)
  r = requests.get(p_image_url, allow_redirects=True)
  with open("file2.png",'wb') as f:
      f.write(r.content)
  name = "file2.png"
  char = predict.answer(name)
  return str(char)

import streamlit as st
st.title('Primonz')
p_image_url = st.text_input("ลิ้งค์ภาพ: ")
#if st.button('Excuted'):
aw = imgurl(p_image_url)
st.image("file2.png")
st.text(str(aw))

query = st.experimental_get_query_params()
defaul = int(query["nameChar"][0]) if "nameChar" in query else 0
nameChar = str(aw)
st.experimental_set_query_params(nameChar)
