import requests
import predict


st.experimental_get_query_params(p_image_url)
def imgurl(p_image_url: str):
  #file#Image.open(image.file)
  r = requests.get(p_image_url, allow_redirects=True)
  with open("file2.png",'wb') as f:
      f.write(r.content)
  name = "file2.png"
  char = predict.answer(name)
  return {'nameCH':str(char)}

import streamlit as st
st.title('Primonz')
p_image_url = st.text_input("ลิ้งค์ภาพ: ")
#if st.button('Excuted'):
aw = imgurl(p_image_url)
st.image("file2.png")
st.text(str(aw))

#st.experimental_set_query_params(nameChar="")

#nameChar = str(aw)

