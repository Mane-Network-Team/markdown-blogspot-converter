from cgitb import html
from symtable import symtable
from bs4 import BeautifulSoup
import sys,os,shutil

file_path = sys.argv[1]
dir, fname = os.path.split(file_path)

html_file = open(file_path,'r',encoding='utf-8')
bs = BeautifulSoup(html_file.read(),"html.parser")

if not(os.path.exists(dir + "//" + "output")):
    os.mkdir(dir + "//" + "output")

new_url = input("[>] Input your new url (end with '/'): ")

for img in (bs.find_all("img")):
    print("Copying %s to %s ..." % (dir + "//" + img["src"],dir + "//" + "output"+ "//"))
    shutil.copy(dir + "//" + img["src"], dir + "//" + "output"+ "//")
    img["src"] = new_url + img["src"].split("/")[-1]


save = open(file_path + "_imgout.html",'w',encoding='utf-8')
save.writelines(str(bs))
save.close()

html_file.close()

print("Done")