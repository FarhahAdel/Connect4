import numpy as np

import cv2 as cv
font = cv.FONT_HERSHEY_SIMPLEX

def guiTree(tree):
	
        d =0
        x =0
        y =40
        neighbours = 0
        COLOR = (0,0,255);img = np.zeros((5000,5000,3), np.uint8)
        for i in range(0,len(tree)):
             
                if tree[i].depth == 0 :
                    cv.circle(img,(700,y), 20, (0,0,255), -1)
                    cv.putText(img,str(tree[i].score),(700,y), font, 1,(255,255,255),2,cv.LINE_AA)
                
                elif tree[i].depth == d :
                                                        # # if x < 3300:
                                                        # #     x = x+300
                                                        # # else :
                                                           
                                                        # #     x = 100
                                                        # #     y = y+100
                                                          
                                                        if neighbours == 0 :
                                                            x = 100
                                                            y = y +50
                                                            neighbours = len(tree[i].parent.children)
                                                        else :
                                                            x = x+300
                                                       
                                                       
                                                        cv.circle(img,(x,y), 20, COLOR, -1)
                                                        cv.putText(img,str(tree[i].score)+"("+str(tree[i].column)+")",(x,y), font, 1,(255,255,255),2,cv.LINE_AA)
                                                        neighbours = neighbours-1

                else :
                    if COLOR == (0,0,255):
                        COLOR = (0,255,255)
                    else :
                        COLOR = (0,0,255)

                    x = 100
                    y = y+100
                    d = d+1
                    if d == 1:
                        x = 500
                    cv.circle(img,(x,y), 20, COLOR, -1)
                    cv.putText(img,str(tree[i].score)+"("+str(tree[i].column)+")",(x,y), font, 1,(255,255,255),2,cv.LINE_AA)
                    neighbours = len(tree[i].parent.children)-1
                
        return img

                

def show(img):
    scale_percent = 60 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
  

    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
    cv.imshow("lol",resized)
    cv.waitKey(0)

