#!/usr/bin/python

#Developed by Faasi
#https://github.com/faasii


import dropbox
import sys

token = ""  #Enter your dropbox access token here
try:
	dbx = dropbox.Dropbox(token)
	print("Connected ")

except:
	print("Connection Failed")
	exit()

def list():
	flag = 0
	for entry in dbx.files_list_folder('').entries:
		flag = flag + 1
		a = entry.name
		print(str(flag) + ". " + a)

def upload(dname,lname):
    try:
        with open(lname) as f:
            print("Uploading ... please wait ! ")
            #dbx.files_upload(f,name)
            dbx.files_upload(open(lname, "rb").read(), dname)
            print("Successfully Uploaded ")
            list()
    except:
        print("Uploading Failed !")

def download(dname,lname):
    try:
        with open(lname, "wb") as f:
            print("Downloading ... please wait")
            metadata, res = dbx.files_download(path=dname)
            f.write(res.content)
            print("Download completed")
    except:
        print('Downloading *Failed !')
def delete(dname):
    try:
        dbx.files_delete(dname)
        print("file Successfully deleted")
        list()
    except:
        print("Can't delete file ,try again")
        exit()
def link(dname):
    try:
        shared_link_metadata = dbx.sharing_create_shared_link_with_settings(dname)
        print(shared_link_metadata.url)
    except:
        print("Can't Create Link")
def arg():
    d = "/"
    try:
        a = sys.argv[1]
    except:
        print("Usage :")
        print("python dbox.py list                                                                      *for list all files / folder in dropbox")
        print("python dbox.py upload <path of local file> <dropbox name of the file>                    *Upload files to dropbox")
        print("python dbox.py download  <name of dropbox file > <name you want to save in your system>  *Download file from dropbox")
        print("python dbox.py delete  <dropbox name of the file>                                        *Delete file from dropbox")
        print("python dbox.py link  <dropbox name of file >                                             *Crete shareble link" )
        exit()

    if a == "list":
        list()
    elif a == "download":
        b = sys.argv[2]
        c = sys.argv[3]
        b = d + b
        download(b,c)
    elif a == "upload":
        b = sys.argv[2]
        c = sys.argv[3]
        c = d + c
        upload(c,b)

    elif a == "delete":
        b = sys.argv[2]
        b = d + b
        delete(b)

    elif a == "link":
        b = sys.argv[2]
        b = d + b
        link(b)
    else:
        print('Wrong Argument , Try Again !')
arg()

