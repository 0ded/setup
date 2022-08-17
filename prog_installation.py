import time
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from bs4 import BeautifulSoup as bs
import requests
import json_helper
import pyuac

links_path = 'C:\\Users\\adamo\\PycharmProjects\\programInstaller\\links.json'
installation_seq = 'C:\\Users\\adamo\\PycharmProjects\\programInstaller\\automation_sequence.json'
download_location = 'C:\\Users\\adamo\\PycharmProjects\\programInstaller\\installation files\\'
file_type = '.exe'


# this function download the setup files from the websites
def get_Installations():
    links = json_helper.get_json(links_path)
    for key in links.keys():
        try:
            with open(download_location + key + file_type, 'wb') as file:
                response = requests.get(links[key])
                file.write(response.content)
                file.close()
        except:
            print("error")


# this function install each file with it's installation sequence, the sequence is stored inside the json file
def installaiton():
    seq = json_helper.get_json(installation_seq)  # getting the automation sequences for installations
    for file in seq.keys():
        app = Application().start(
        cmd_line=r'C:\\Users\\adamo\\PycharmProjects\\programInstaller\\installation files\\steam.exe')
        time.sleep(2)
        for bottun in seq[file]:
            time.sleep(2)
            send_keys(bottun)


get_Installations()
installaiton()


# def main():
#     get_Installations()
#     installaiton()
#
# if __name__ == "main":
#     # making sure we run as admin before starting
#     if not pyuac.isUserAdmin():
#         pyuac.runAsAdmin()
#     else:
#         main()

# with open('m.exe', 'wb') as file:
#     resonse = requests.get('https://laptop-updates.brave.com/download/XWV588')
#     file.write(resonse.content)
#     file.close()

# def get_soup(url):
#     return bs(requests.get(url).text, 'html.parser')
#
# def get_new_link():
#     for link in get_soup(steam_url).find_all('a'):
#         file_link = link.get('href')
#         if FILETYPE in file_link:
#             with open('C:\\Users\\adamo\PycharmProjects\programInstaller\\test\\' + link.text + file_type, 'wb') as file:
#                 response = requests.get(file_link)
#                 file.write(response.content)
#                 file.close()
