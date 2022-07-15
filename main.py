from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup as besoup
 
login = "https://www.linkedin.com/login"
jobs = "https://www.linkedin.com/jobs"
username="xxxxxxxxxxxxxxxxxxxxxx" #enter username
pw = "xxxxxxxxxxxxxxxxxx" #enter password
 
edgeoptions = Options() #you can use whatever browser you like
edgeoptions.add_argument("headless")
driver = webdriver.Edge(options = edgeoptions)
 
#login
driver.get(login)
driver.find_element(By.ID,'username').send_keys(username)
driver.find_element(By.ID,'password').send_keys(pw)
driver.find_element(By.XPATH,('//*[@id="organic-div"]/form/div[3]/button')).click()
print("accesso effettuato")
 
driver.get(jobs)
jobs_html= driver.page_source
 
#parsing
soup = besoup(jobs_html,'html.parser')
 
lista = soup.find_all('section')[3].find('ul')
links = lista.find_all('a')
 
html = open('html.txt','w')
for i in links:
    if(i.string != None):
        out = str(i.string+"https://www.linkedin.com"+i.get('href')+"\n")
        html.write(out)
 
html.close()
driver.quit()
