import os
import shutil

def automatefolder():
    pathfolder = 'C:\\Users\\Admin\\Documents\\Sales performance analysis'
    files= [f for f in os.listdir(pathfolder)]
    
    for file in files:
        filetype = file.split('.')
        if len(filetype)>=2:
            foldername = pathfolder+'\\'+filetype[1]
        
            if os.path.isdir(foldername):
               shutil.move(pathfolder+'\\'+file,foldername+'\\'+file)
               continue
            else:
               os.mkdir(foldername)
               shutil.move(pathfolder+'\\'+file,foldername+'\\'+file)
            
if __name__ =="__main__":
    automatefolder()
    