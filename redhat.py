from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

auth = GoogleAuth() #authorise application
drive_obj = GoogleDrive(auth)
folder = "18vTzaKFVoCs8eHAZ9_bI1aXdI4beDNfx"

file_names = drive_obj.ListFile({'q':f"'{folder}' in parents and trashed=false"}).GetList()
for files in file_names:
	print(files['title'])
        files.GetContentFile(files['title'])
        os.system('cmd /k "dir"')
