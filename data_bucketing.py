import cv2 
import shutil
import os 
import argparse 
ap=argparse.ArgumentParser()
ap.add_argument('-i', '--image', type = str , default= '', help = 'path')
ap.add_argument('-d', '--destination', type = str , default= '', help = 'path')
args= vars(ap.parse_args())
l=[]
#path = '/home/chandra/Downloads/Occlusion_Filter_2/Occlusion_Filter_2/Training/Religious/'
path = args['image']
dest = args['destination']
files = os.listdir(path)
os.mkdir( dest  + 'turban') #press t
#os.mkdir('/home/chandra/Documents/'  + 'muslim_caps')# press m
#os.mkdir('/home/chandra/Documents/'  + 'gurkha')  # press g
#os.mkdir('/home/chandra/Documents/'  + 'ghoonghat')# press h
#os.mkdir('/home/chandra/Documents/'  + 'specs') # press s
#os.mkdir('/home/chandra/Documents/'  + 'marathi_caps') # press w
#os.mkdir('/home/chandra/Documents/'  + 'normal') # press n
#os.mkdir('/home/chandra/Documents/'  + 'extra_rel') # press e
# r= os.path('/home/chandra/Documents/religious/')
# n= os.path('/home/chandra/Documents/non_religious/')
# p= os.path('/home/chandra/Documents/Proper/')

for file in files:
    try :
        fp = os.path.join (path , file)
        image= cv2.imread(fp)
        cv2.imshow('images', image)
        key =cv2.waitKey(0)
        if (key == 116):
            
            shutil.move(fp, '/home/chandra/Documents/turban/')
        elif (key == 109): 
            
            shutil.move(fp, '/home/chandra/Documents/muslim_caps/')
        elif(key == 103):
            
            shutil.move(fp, '/home/chandra/Documents/gurkha/')
        elif(key == 104):
            
            shutil.move(fp, '/home/chandra/Documents/ghoonghat/')
        elif(key == 115):
            
            shutil.move(fp, '/home/chandra/Documents/specs/')
        elif(key == 119):
            
            shutil.move(fp, '/home/chandra/Documents/marathi_caps/')
        elif(key == 110):
            
            shutil.move(fp, '/home/chandra/Documents/normal/')
        elif(key == 101):
            
            shutil.move(fp, '/home/chandra/Documents/extra_rel/')
        elif (key == 113):
            break
    except :
        print("this image number has not been bucketed:",image)
        p=l.append(image)
        print(p)
        continue
print("image not bucketed: ",l)
cv2.destroyAllWindows()
