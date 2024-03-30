f = open('practice.txt','w+')            #if not exists it will create a new one file
f.write('This is a test string')
f.close()


import os
print(os.getcwd())
print(os.listdir())

#import shutil
#shutil.move('practice.txt','destination')

#os.unlink(path) = delete a file at the path your provided
#os.rmdir(path) = delete a folder (folder must be empty) at path provided
#shutil.rmtree(path) = remove all files and folder contained in the path

#pip install send2trash
#import send2trash
#send2trash.send2trash('practice.txt')

#===================

os.walk        #make a tree , look every single thing in a file path loaction folder,subfolders and files and apply logic...

#file_path = ''
#for folder,sub_folders,files in os.walk(file_path):
    #print(f"Currently looking at{folder}"...)

