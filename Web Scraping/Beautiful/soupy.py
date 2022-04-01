import re 
from bs4 import BeautifulSoup
import requests

j = r"https://saharareporters\.com/([0-9])+/([0-9])+/([0-9])+/([A-Za-z0-9])*"

def open_file(name):
    file = open(("f{Correct}.txt", name),'w')
    return file
    
def close_file(file):
    file.close()
    
def website_check(i,file2):
    if re.match(j,i):
        file2.writelines(str(i)) 



def Collect_data_from_the_internet(put)
    soup = request.get(put)
    return soup
    
def Collect_data_from_a_file():
    name_of_file = raw_input("What is the name of the file? \n")
    with open(name_of_file) as ap:
        soup = BeautifulSoup(ap)
    return soup
    
class BeautyScrapper():
    
    beauty_database = []
    
    def __init__(self):
        """
            Just writing something here because people used to write something in their DeprecationWarning
        """
        
    def ChoseMethod(self):
        print("Pls, choose the means that would suit you when you want to web scarp\nWould you\n1. Scrape from the Internet. This means inputting a url\n2. Scrape from a file in the present directory. Note that the file has to be in the present directory")
        value = raw_input(" ")
        while True:
            if value == '1':
                break
            elif value =='2':
                break
            else:
                print("Incorrect input.\nPls,input the correct value")
                value = ""
                
    def add_to_database(self, file_name):
        card = open(file_name,'r')
        for i in card:
            x = i.readlines()
            ink = i['href']
        website_check(ink, file)           
                
    def 