import json
import numpy as np

with open('D:/BaiduNetdiskDownload/personreid/annotation_train.odgt', 'r+') as f: #input filename
    datalist = f.readlines()

inputfile = []
inner = {}
anchor = str()
for i in np.arange(len(datalist)):
    anchor = str()
    adata = json.loads(datalist[i])
    image_path ='D:/BaiduNetdiskDownload/personreid/train/'+str(adata['ID'])+ '.jpg'
    #print(image_path)
    gtboxes = adata['gtboxes']
    # vbox = gtboxes['vbox']
    print(len(gtboxes))
    for gtbox in gtboxes:  # Change lines 13 to 27 based on the number of classes you have and their names
        if gtbox['tag'] == 'person':  # here, person = the class name
                xmin,ymin,w,h = gtbox['vbox']
                xmax = xmin + w
                ymax = ymin+ h
                box = str(' ')+str(xmin)+str(',')+str(ymin)+str(',')+str(xmax)+str(',')+str(ymax)+str(',')+str(0)
                anchor+=box
    print(image_path+anchor)
    src = image_path + anchor
    with open('person.txt', 'a') as file_handle:  # .txt可以不自己新建,代码会自动新建
        file_handle.write(src)  # 写入
        file_handle.write('\n')







