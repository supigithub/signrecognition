
import os
import cv2
cap=cv2.VideoCapture(0)
directory='Image/'                                                                    `
while True:
    _,frame=cap.read()
    count = {
             'a': len(os.listdir(directory+"/Food")),
             'b': len(os.listdir(directory+"/Hello")),
             'c': len(os.listdir(directory+"/Water")),
             'd': len(os.listdir(directory+"/Like")),
             'e': len(os.listdir(directory+"/Dislike")),
             'f': len(os.listdir(directory+"/Help")),
             'g': len(os.listdir(directory+"/Nice")),
             'h': len(os.listdir(directory+"/Peace")),
             
             }
  
    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,400),(255,255,255),2)
    cv2.imshow("data",frame)
    cv2.imshow("ROI",frame[40:400,0:300])
    frame=frame[40:400,0:300]
    interrupt = cv2.waitKey(10)
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'Food/'+str(count['a'])+'.png',frame)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory+'Hello/'+str(count['b'])+'.png',frame)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'Water/'+str(count['c'])+'.png',frame)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(directory+'Like/'+str(count['d'])+'.png',frame)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory+'Dislike/'+str(count['e'])+'.png',frame)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(directory+'Help/'+str(count['f'])+'.png',frame)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(directory+'Nice/'+str(count['g'])+'.png',frame)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory+'Peace/'+str(count['h'])+'.png',frame)
   


cap.release()
cv2.destroyAllWindows()
