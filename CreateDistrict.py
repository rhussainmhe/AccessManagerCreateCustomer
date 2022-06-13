import requests
from requests_html import HTML
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import roses
import sys

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options, executable_path='/Users/riaz_hussain/Downloads/chromedriver')

class fixer:
    def search_roses_name(self):
        connected_url = 'https://connected.mcgraw-hill.com/connected/login.do' #connected login URL here
        connected_search_url = 'https://connected.mcgraw-hill.com/connected/support.accountSearch.do?accountName=&oksAccountId=' #connected search url here
        self.oracle_id = input("Enter Oracle ID: ")
        self.actual_roses_name = ''

        # connect to connectED
        try:
            driver.get(connected_url)
            connected_body_el = driver.find_element(by=By.CSS_SELECTOR, value="body")
            connected_html_str = connected_body_el.get_attribute("innerHTML")

            connected_html_obj = HTML(html=connected_html_str)
            time.sleep(2)
        except Exception as e:
            print("Error: Could not load connected login page " + str(e))
            sys.exit(1)

        #input connected user pass and login
        try:
            driver.find_element(By.NAME, "loginUserName").send_keys(roses.u)
            driver.find_element(By.NAME, "loginPassword").send_keys(roses.cep + Keys.ENTER)
            time.sleep(2)
        except Exception as e:
            print("Error: Could not login to connected " + str(e))
            sys.exit(1)

        #Search the oracle id in connected
        try:
            driver.get(connected_search_url + self.oracle_id)
            print(connected_search_url + self.oracle_id)
            time.sleep(2)
            connected_body_el = driver.find_element(by=By.CSS_SELECTOR, value="body")
            connected_html_str = connected_body_el.get_attribute("innerHTML")
            connected_html_obj = HTML(html=connected_html_str)

            # Find the returned roses name and store it
            self.actual_roses_name = driver.find_element(by=By.XPATH, value='//*[@id="supportAccountSearchResults"]/table/tbody/tr/td[2]/div').text
            print('Roses name: ' + self.actual_roses_name)

        except Exception as e:
            print("Error: Could not complete connectED oracle id search " + str(e))
            sys.exit(1)

    def final_change(self):

            #login to roses
            roses_url = 'https://roses-prod.cdiapps.com/roses/login.do' #roses login url here
            search = 'https://roses-prod.cdiapps.com/roses/subscriptionSearchAccount.do' #roses search url here
            manage_edu_id = 'https://roses-prod.cdiapps.com/roses/manageEduEntity.do#/search' #manage educational identity url
            time.sleep(2)

            # connect to roses login page
            try:
                driver.get(roses_url)
                roses_body_el = driver.find_element(by=By.CSS_SELECTOR, value="body")
                roses_html_str = roses_body_el.get_attribute("innerHTML")

                roses_html_obj = HTML(html=roses_html_str)
                time.sleep(2)

            except Exception as e:
                print("Error: Could not load roses login page " + str(e))
                sys.exit(1)

            #input roses user pass
            try:
                driver.find_element(By.NAME, "username").send_keys(roses.u)
                driver.find_element(By.NAME, "password").send_keys(roses.p + Keys.ENTER)
                time.sleep(3)
            except Exception as e:
                print("Error: Could not login to roses " + str(e))
                sys.exit(1)

            # load roses search page
            try:
                driver.get(search)
                roses_body_el = driver.find_element(by=By.CSS_SELECTOR, value="body")
                roses_html_str = roses_body_el.get_attribute("innerHTML")

                roses_html_obj = HTML(html=roses_html_str)
                time.sleep(2)
            except Exception as e:
                print("Error: Could not load roses search page " + str(e))
                sys.exit(1)

            print('Searching oracle name ' + self.actual_roses_name)

            # search roses name
            try:
                driver.find_element(By.NAME, "acctNm").send_keys(self.actual_roses_name + Keys.ENTER)
                time.sleep(3)

            except Exception as e:
                print("Error: Could not search roses name  " + str(e))
                sys.exit(1)

            # find manage schools link and click it
            try:
                roses_body_el = driver.find_element(by=By.CSS_SELECTOR, value="body")
                roses_html_str = roses_body_el.get_attribute("innerHTML")

                roses_html_obj = HTML(html=roses_html_str)
                # manage = driver.find_element(by=By.XPATH, value='//*[@id="SRCH_REC1"]/div[4]/a')
                manage = driver.find_element(by=By.LINK_TEXT, value='Manage District')
                manage.click()

            except Exception as e:
                print("Error: Could not find manage link " + str(e))
                sys.exit(1)

            # fetch district name, city, and state
            try:
                district_name = driver.find_element(by=By.XPATH, value='/html/body/div/div[3]/div/div/div/table/tbody/tr/td[1]/a').text


                city_state = driver.find_element(by=By.XPATH, value='/html/body/div/div[3]/div/div/div/table/tbody/tr/td[2]').text
                print('Found district name + state: ' + district_name + ' ' + city_state)

                # Find states abbreviation
                us_state_to_abbrev = {
                    "Alabama": "AL",
                    "Alaska": "AK",
                    "Arizona": "AZ",
                    "Arkansas": "AR",
                    "California": "CA",
                    "Colorado": "CO",
                    "Connecticut": "CT",
                    "Delaware": "DE",
                    "Florida": "FL",
                    "Georgia": "GA",
                    "Hawaii": "HI",
                    "Idaho": "ID",
                    "Illinois": "IL",
                    "Indiana": "IN",
                    "Iowa": "IA",
                    "Kansas": "KS",
                    "Kentucky": "KY",
                    "Louisiana": "LA",
                    "Maine": "ME",
                    "Maryland": "MD",
                    "Massachusetts": "MA",
                    "Michigan": "MI",
                    "Minnesota": "MN",
                    "Mississippi": "MS",
                    "Missouri": "MO",
                    "Montana": "MT",
                    "Nebraska": "NE",
                    "Nevada": "NV",
                    "New Hampshire": "NH",
                    "New Jersey": "NJ",
                    "New Mexico": "NM",
                    "New York": "NY",
                    "North Carolina": "NC",
                    "North Dakota": "ND",
                    "Ohio": "OH",
                    "Oklahoma": "OK",
                    "Oregon": "OR",
                    "Pennsylvania": "PA",
                    "Rhode Island": "RI",
                    "South Carolina": "SC",
                    "South Dakota": "SD",
                    "Tennessee": "TN",
                    "Texas": "TX",
                    "Utah": "UT",
                    "Vermont": "VT",
                    "Virginia": "VA",
                    "Washington": "WA",
                    "West Virginia": "WV",
                    "Wisconsin": "WI",
                    "Wyoming": "WY",
                    "District of Columbia": "DC",
                    "American Samoa": "AS",
                    "Guam": "GU",
                    "Northern Mariana Islands": "MP",
                    "Puerto Rico": "PR",
                    "United States Minor Outlying Islands": "UM",
                    "U.S. Virgin Islands": "VI",
                }

                split_city_state = city_state.split(', ')
                abbrev_state = ''
                for a in split_city_state:
                    if a in us_state_to_abbrev:
                        abbrev_state = us_state_to_abbrev[a]
                        break

                city = split_city_state[0]
                state = split_city_state[1]
                time.sleep(2)

            except Exception as e:
                print("Error: Could not find district name or state " + str(e))
                sys.exit(1)

            # load manage educaiton identity search page
            try:
                driver.get(manage_edu_id)
                roses_body_el = driver.find_element(by=By.CSS_SELECTOR, value="body")
                roses_html_str = roses_body_el.get_attribute("innerHTML")

                roses_html_obj = HTML(html=roses_html_str)
                time.sleep(2)

            except Exception as e:
                print("Error: Could not load manage educational identity page " + str(e))
                sys.exit(1)

            # enter district name, select district in dropdown, select districts state in dropdown, enter city, search
            try:
                driver.find_element(By.NAME, "entityName").send_keys(district_name)
                select = Select(driver.find_element(By.NAME, "entityType"))
                select.select_by_visible_text('DISTRICT')
                state_select = Select(driver.find_element(By.NAME, "state"))
                state_select.select_by_visible_text(state)
                driver.find_element(By.NAME, "city").send_keys(city + Keys.ENTER)

                time.sleep(3)

            except Exception as e:
                print("Error: Could not search district in manage education identity " + str(e))
                sys.exit(1)

            # find district in returned results and click edit
            try:
                edit_mei = driver.find_element(by=By.XPATH, value='/html/body/div/div[3]/div/div[2]/div/div/div/div[2]/div[2]/div/div[8]/a')
                edit_mei.click()

                time.sleep(3)

            except Exception as e:
                print("Error: Could not find edit button for district in manage educational identity")
                sys.exit(1)

            # return XID, oracle ID, output Access Manager checks in terminal, output customer name and xid
            try:
                xid = driver.find_element(by=By.XPATH, value='//*[@id="page_content"]/div/div/form/div[7]/div[2]').text
                oks_oracle_id = driver.find_element(by=By.XPATH, value='//*[@id="page_content"]/div/div/form/div[23]/div/div[1]/div[4]').text
                print('--------------------------------------------------------')
                print('Does the oracle id you entered match what was returned?')
                print('Entered:  ' + self.oracle_id + '\n' + 'Returned: ' + oks_oracle_id)
                print('--------------------------------------------------------')
                print('If yes create new access manager customer using below info' + '\n')
                print('Access Manager Name:' + '\n' + self.actual_roses_name + ' (' + abbrev_state + ') ' + self.oracle_id)
                print('XID:' + '\n' + xid)

            except Exception as e:
                print("Error: Could not fetch XID " + str(e))
                sys.exit(1)

            driver.quit()

r = fixer()
r.search_roses_name()
r.final_change()
driver.quit()
