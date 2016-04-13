''' remove annoying website names from a music file
    and also if it starts with a number remove it as it
    causes problems while searching a particular file
    Author: Kshitiz Joshi
    e-mail: joshikshitij_13@yahoo.in
'''
from os import listdir,rename
from os.path import isfile, join
import re
import sys

myPath=input("Enter the path to the folder: ")
fileFormats=['.mp3','.mp4','.wma','.wav','.ogg','.mid','.ra','.ram','.rm']
try:
    orignalFiles = [ f for f in listdir(myPath) if isfile(join(myPath,f)) ]
except WindowsError:
    print ("Incorrect location")
    exit
# these are the regular expressions that worked for me
regex_webName= r'\s*\-*\s*[\(\[\{]\S*\.\S*[\)\]\}]\s*'
regex_numStart= r'^[0-9]+\s*[\-\.]?\s*'
for f in orignalFiles:
    # Ensure that it renames only the required file formats
    is_a_targetFile=0
    for ext in fileFormats:
        is_a_targetFile=is_a_targetFile or re.search(ext,f,re.IGNORECASE)
    if is_a_targetFile:
        match_web=True
        match_num=True
        # Repeat if any regex matches
        while match_web or match_num:
            match_web=re.search(regex_webName,f)
            match_num=re.search(regex_numStart,f)
            if match_web and match_num:
                new_f=f.replace(match_web.group(),"")
                new_f=new_f.replace(match_num.group(),"")

            elif match_num:
                new_f=f.replace(match_num.group(),"")
            elif match_web:
                new_f=f.replace(match_web.group(),"")
            else:
                continue
            #file with name as $new_f may already exist
            try:
                rename(join(myPath,f),join(myPath,new_f));
            except WindowsError:
                print ("Error renaming file: ",f,"to",new_f)
                match_web=False
                match_num=False
                continue

            print ("Old Name:",f)
            print ("New Name:",new_f)
            print ("--------------------------------------")
            f=new_f