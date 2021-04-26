import requests
import predict
import streamlit as st

p_image_url = st.experimental_get_query_params()
def imgurl(p_image_url: str):
  #file#Image.open(image.file)
  r = requests.get(p_image_url, allow_redirects=True)
  with open("file2.png",'wb') as f:
      f.write(r.content)
  name = "file2.png"
  char = predict.answer(name)
  return {'nameCH':str(char)}


st.title('Primonz')
p_image_url = st.text_input("ลิ้งค์ภาพ: ")
#if st.button('Excuted'):
aw = imgurl(p_image_url)
st.image("file2.png")
st.text(str(aw))

#st.experimental_set_query_params(nameChar="")

#nameChar = str(aw)

