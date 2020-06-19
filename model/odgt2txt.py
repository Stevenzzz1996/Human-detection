import json
import numpy as np
from tqdm import tqdm

with open('annotation_train.odgt', 'r+') as f: #input filename
    datalist = f.readlines()


for data in tqdm(datalist):
    anchor = ""
    
    adata = json.loads(data)
    
    image_path ='D:/BaiduNetdiskDownload/personreid/train/'+ adata['ID'] + '.jpg'
  
    gtboxes = adata['gtboxes']
  
    for gtbox in gtboxes:  
        if gtbox['tag'] == 'person':  # here, person = the class name
                xmin,ymin,w,h = gtbox['vbox']
                xmax = xmin + w
                ymax = ymin+ h
                box = " " + ",".join(map(str, [xmin, ymin, xmax, ymax, 1]))
                anchor += box

    src = image_path + anchor
    with open('person.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
        file_handle.write(src + '\n')  # 写入







