from time import time
from selenium import webdriver
import os
from job_site.constants import URL
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class JobSite(webdriver.Chrome):
    def __init__(self,driver_path=r";C:\SeleniumDrivers"):
        self.driver_path=driver_path
        os.environ['PATH']+=self.driver_path
        super(JobSite,self).__init__()
        self.implicitly_wait(15)
        self.maximize_window()
        
    def landing_page(self):
        self.get(URL)
        
    def accept_cookies(self):
        cookie_element=self.find_element(By.ID,'ccmgt_explicit_accept')
        cookie_element.click()
        
    def search(self,title='Software Engineer',where='London',miles='30 miles'):
        title_element=self.find_element(By.ID,'keywords')
        title_element.click()
        title_element.send_keys(title)
        
        where_element=self.find_element(By.ID,'location')
        where_element.click()
        where_element.send_keys(where)
        time.sleep(1)
        
        miles_element=self.find_element(By.ID,'Radius')
        radius=Select(miles_element)
        radius.select_by_visible_text(miles)
        search=self.find_element(By.ID,'search-button')
        search.click()
    
        
    def get_and_save_data(self):
        for k in range(3):
            title_of_job=self.find_elements(By.XPATH,"//div[@class='sc-fzooss kBgtGS']/a/h2")
            location=self.find_elements(By.XPATH,"//li[@class='sc-fznXWL hSqkJy']/span")
            salary=self.find_elements(By.XPATH,"//dl[@data-at='job-item-salary-info']")
            description=self.find_elements(By.XPATH,"//div[@class='sc-fzoYkl kSkZOQ']/a/span")
            print(len(title_of_job))
            print(len(location))
            print(len(salary))
            print(len(description))
            with open('job_site_data.csv','w') as file:
                file.write('Title;Location;Salary;Description\n')
                for i in range(len(title_of_job)):
                    file.write(title_of_job[i].text+';'+location[i].text+';'+salary[i].text+';'+description[i].text+'\n')
                next=self.find_element(By.XPATH,"//a[@aria-label='Next']")
                next.click()
            file.close()
        self.close()
            
    
