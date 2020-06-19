import json
import numpy as np
<<<<<<< HEAD
import cv2
odgt_path = 'path.odgt'# odgt文件存放地址
with open(odgt_path, 'r+') as f: #input filename
    datalist = f.readlines()

inputfile = []
inner = {}
anchor = str()
def change_data(x_min,x_max,y_min,y_max,image_shape):
    h,w,_ = image_shape
    x_min = max(0,x_min)
    x_max = min(w-1,x_max)
    y_min = max(0,y_min)
    y_max = min(h-1,y_max)
    return x_min,x_max,y_min,y_max


for i in np.arange(len(datalist)):
    anchor = str()
    adata = json.loads(datalist[i])
    image_path ='D:/BaiduNetdiskDownload/person_train/'+str(adata['ID'])+ '.jpg'
    read_path = 'D:/BaiduNetdiskDownload/personreid/train/'+str(adata['ID'])+ '.jpg'
    #print(image_path)
    gtboxes = adata['gtboxes']
    # vbox = gtboxes['vbox']
    print(len(gtboxes))
    src = cv2.imread(read_path)
    print(src.shape)
    for gtbox in gtboxes:  # Change lines 13 to 27 based on the number of classes you have and their names
=======
from tqdm import tqdm

with open('annotation_train.odgt', 'r+') as f: #input filename
    datalist = f.readlines()


for data in tqdm(datalist):
    anchor = ""
    
    adata = json.loads(data)
    
    image_path ='D:/BaiduNetdiskDownload/personreid/train/'+ adata['ID'] + '.jpg'
  
    gtboxes = adata['gtboxes']
  
    for gtbox in gtboxes:  
>>>>>>> 905d6223eb8564e9f167dcecbd69412c144a4cce
        if gtbox['tag'] == 'person':  # here, person = the class name
                xmin,ymin,w,h = gtbox['vbox']
                xmax = xmin + w
                ymax = ymin+ h
<<<<<<< HEAD
                xmin,xmax,ymin,ymax = change_data(xmin,xmax,ymin,ymax,src.shape)
                box = " " + ",".join(map(str, [xmin, ymin, xmax, ymax, 1]))
                # box = str(' ')+str(xmin)+str(',')+str(ymin)+str(',')+str(xmax)+str(',')+str(ymax)+str(',')+str(0)
                anchor+=box
    print(image_path+anchor)
    src = image_path + anchor
    with open('person_train.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
        file_handle.write(src)  # 写入
        file_handle.write('\n')
=======
                box = " " + ",".join(map(str, [xmin, ymin, xmax, ymax, 1]))
                anchor += box

    src = image_path + anchor
    with open('person.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
        file_handle.write(src + '\n')  # 写入
>>>>>>> 905d6223eb8564e9f167dcecbd69412c144a4cce







