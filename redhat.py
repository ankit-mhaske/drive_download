from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

auth = GoogleAuth() #authorise application
drive_obj = GoogleDrive(auth)
folder = "18vTzaKFVoCs8eHAZ9_bI1aXdI4beDNfx"

"""file1 = drive_obj.CreateFile({'parents':[{'id':folder}],'title':'hi.txt'})
file1.SetContentString('hello')
file1.Upload()
"""
file_names = drive_obj.ListFile({'q':f"'{folder}' in parents and trashed=false"}).GetList()
for files in file_names:
	files.GetContentFile(files['title'])