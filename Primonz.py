from fastapi import FastAPI
from fastapi import UploadFile, File
import uvicorn
import predict
'''import nest_asyncio
nest_asyncio.apply()
__import__('IPython').embed()'''

app = FastAPI()

'''@app.get("/index")
def my_function(name:str):
  return f"Hello {name} !"'''

@app.post("/api/predict")
def predict_image(file:UploadFile = File(...)):
  #print('aaa')
  name = file.filename #.split('.')[-1] in ("jpg", "jpeg", "png","jfif")
  #char = predict.answer(name)
  return str(name)

'''if __name__ == "__main__":
  uvicorn.run(app, port=4000, host='localhost')'''