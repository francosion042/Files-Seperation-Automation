# -*- coding: utf-8 -*-

import os
import glob
import shutil
from os import path


filename=glob.glob("/home/anthony/Chikezie/*")
documents=['.pdf','.docx','.doc','.txt']
music=['.mp3']
videos=['.mp4']
pictures=['.jpeg','.jpg','.svg','.png','.PNG']
setupFiles=['.exe','.msi']
compressedFiles=['.zip']
files=['.apk']

DocumentsLocation='/home/anthony/Chikezie/documents'
musicLocation='/home/anthony/Chikezie/music'
videosLocation='/home/anthony/Chikezie/videos'
picturesLocation='/home/anthony/Chikezie/pictures'
setupFilesLocation='/home/anthony/Chikezie/setupFiles'
compressedFilesLocation='/home/anthony/Chikezie/compressedFiles'
FilesLocation='/home/anthony/Chikezie/Files'


for file in filename:
    if os.path.splitext(file)[1] in documents:
        if(path.exists(DocumentsLocation)):
            shutil.move(file,DocumentsLocation)
        else:
            os.mkdir(DocumentsLocation)
            shutil.move(file,DocumentsLocation)
            
    if os.path.splitext(file)[1] in music:
        if(path.exists(musicLocation)):
            shutil.move(file,musicLocation)
        else:
            os.mkdir(musicLocation)
            shutil.move(file,musicLocation)
            
    if os.path.splitext(file)[1] in videos:
        if(path.exists(videosLocation)):
            shutil.move(file,videosLocation)
        else:
            os.mkdir(videosLocation)
            shutil.move(file,videosLocation)
            
    if os.path.splitext(file)[1] in pictures:
        if(path.exists(picturesLocation)):
            shutil.move(file,picturesLocation)
        else:
            os.mkdir(picturesLocation)
            shutil.move(file,picturesLocation)
            
    if os.path.splitext(file)[1] in setupFiles:
        if(path.exists(setupFilesLocation)):
            shutil.move(file,setupFilesLocation)
        else:
            os.mkdir(setupFilesLocation)
            shutil.move(file,setupFilesLocation)
    if os.path.splitext(file)[1] in compressedFiles:
        if(path.exists(compressedFilesLocation)):
            shutil.move(file,compressedFilesLocation)
        else:
            os.mkdir(compressedFilesLocation)
            shutil.move(file,compressedFilesLocation)
    if os.path.splitext(file)[1] in files:
        if(path.exists(FilesLocation)):
            shutil.move(file,FilesLocation)
        else:
            os.mkdir(FilesLocation)
            shutil.move(file,FilesLocation)