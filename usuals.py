import requests
from bs4 import BeautifulSoup

class UsualFunctions():
    def __init__(self):
        self.page = requests.get('https://www.worldometers.info/coronavirus/country/brazil/')
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.main_info = self.soup.find_all(class_='maincounter-number') # total, deaths, recovered
        self.active_info = self.soup.find(class_='number-table-main') # active cases
        self.active_conditions = self.soup.find_all(class_='number-table') # condition of active cases


    # get total of cases from main info
    def get_cases(self):
        cases = self.main_info[0].span.text
        cases = self.format_string(cases)
        return cases

    
    # get total of recovered from main info
    def get_recovered(self):
        recovered = self.main_info[2].span.text
        recovered = self.format_string(recovered)
        return recovered


    # get total of deaths from main info
    def get_deaths(self):
        deaths = self.main_info[1].span.text
        deaths = self.format_string(deaths)
        return deaths


    # get total of active cases from active info
    def get_active_cases(self):
        active = self.active_info.text
        active = self.format_string(active)
        return active

    
    # get total of mild conditions
    def get_mild_conditions(self):
        mild = self.active_conditions[0].text
        mild = self.format_string(mild)
        return mild

    
    # get total of serious or critical conditions
    def get_serious_conditions(self):
        serious = self.active_conditions[1].text
        serious = self.format_string(serious)
        return serious


    # format strings
    def format_string(self, string):
        return string.replace(',', '.')