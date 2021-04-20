from botnoi import scrape as sc
from botnoi import cv
import os
import glob

from google.colab import drive
drive.mount('/content/drive')

'''def extractimagefeat(query):
  #create folder
  foldername = "/content/drive/MyDrive/Third year/Second Term/935308/Chatbot/Char/img2p/"+query
  isdir = os.path.isdir(foldername) 
  #check if folder exist
  if not isdir:
    #create directory
    os.makedirs(foldername)
  #get images from google search
  imglist= []
  imglist.append(glob.glob("/content/drive/MyDrive/Third year/Second Term/935308/Chatbot/Char/"+query+"/*"))
  #print(imglist[0][1])
  i = 1
  for img in imglist[0]:
    #extract image features from each images and save to files
    try:
      print(i)
      #create image path
      savepath = foldername + '/' + str(i)+'.p'
      a = cv.image(img)
      a.getresnet50()
      a.save(savepath)
      i = i + 1
    except:
      pass
  return 'complete' '''

'''characters = ['Zhongli','Hutao','Alberdo','Amber','Barbara','Beidou','Bennett','Chongyun','Diluc','Diona','Fischl','Ganyu','Jean','Kaeya',
'Keqing','Klee','Lisa','Mona','Ningguang','Noelle','Qiqi','Razor','Sucrose','Tartaglia','Venti','Xiangling','Xiao','Xingqiu','Xinyan']
for i in range(len(characters)):
  extractimagefeat(characters[i])'''

import glob
import pandas as pd
import pickle
def createdataset():
  imgfolder = glob.glob("/content/drive/MyDrive/Third year/Second Term/935308/Chatbot/Char/img2p/*")
  dataset = []
  for cls in imgfolder:
    clsset = pd.DataFrame()
    pList = glob.glob(cls+'/*')
    featvec = []
    for p in pList:
      dat = pickle.load(open(p,'rb'))
      featvec.append(dat.resnet50)

    clsset['feature'] = featvec
    cls = cls.split('/')[-1]
    clsset['label'] = cls
    dataset.append(clsset)
  return pd.concat(dataset,axis=0)

dataset = createdataset()

dataset

imgfolder = glob.glob("/content/drive/MyDrive/Third year/Second Term/935308/Chatbot/Char/img2p/*")
for cls in imgfolder:
  imgList = glob.glob(cls+'/*')
imgList

from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.svm import LinearSVC
def trainmodel(dataset,modfile=''):
  trainfeat, testfeat, trainlabel, testlabel = train_test_split(dataset['feature'], dataset['label'], test_size=0.33, random_state=42)
  clf = LinearSVC()
  mod = clf.fit(np.vstack(trainfeat.values),trainlabel.values)
  res = mod.predict(np.vstack(testfeat.values))
  if modfile!='':
    pickle.dump(mod,open(modfile,'wb'))
  acc = sum(res == testlabel)/len(res)
  return mod,acc

mod,acc = trainmodel(dataset,'mymod.mod')

# output function
modFile = 'mymod.mod'
mod = pickle.load(open(modFile,'rb'))

def predicting(imgurl):
  a = cv.image(imgurl)
  feat = a.getresnet50()
  res = mod.predict([feat])
  return res


def answer(name):
  a=predicting(name)
  b = str(a).split(' ')
  c = b[0].split('\'')
  return c[1]
