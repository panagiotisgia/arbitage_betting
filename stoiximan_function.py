import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, csv
import re

######################################### Football ####################################################

def stoiximan_football_text(football_url: str, driver: selenium.webdriver.chrome.webdriver.WebDriver)->str:  
    # Maximize window
    driver.maximize_window()
    # Go to football coupon
    driver.get(football_url)
    cookies = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))).click()
    # Close Log in pop up window
    x_button = driver.find_element(By.CSS_SELECTOR, '[class="sb-modal__close__btn uk-modal-close-default uk-icon uk-close"]').click()
    # Click 24 hours button
    button_24 = driver.find_element(By.CSS_SELECTOR, '[class="events-tabs-container__tab__item__button GTM-24"]').click()
    time.sleep(5)
    
    ##### Scroll down the page and wait all values to load #####
    # Get the height of the footer element
    footer = driver.find_element(By.CSS_SELECTOR, '[class="sb-footer GTM-footer"]')
    footer_height = footer.size['height']
    # Get the height of the window
    window_height = driver.execute_script("return window.innerHeight;")
    # Initialize the last height variable with a value
    last_height = driver.execute_script("return document.body.scrollHeight")
    # Define how many times you want to scroll the webpage
    num_scrolls = 100

    # Loop through the number of times you want to scroll
    for i in range(num_scrolls):
        # Scroll down the webpage by the height of the window minus the height of the footer
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight - window.innerHeight - %s);" % footer_height)
        # Wait for the webpage to load
        time.sleep(3)
        # Get the new height of the webpage after scrolling
        new_height = driver.execute_script("return document.body.scrollHeight")
        # If the new height is the same as the old height, we have reached the end of the webpage
        if new_height == last_height:
            break
        # Otherwise, update the last height and continue scrolling
        last_height = new_height

    # Wait for the dailyCoupon_body element to be present on the page
    wait = WebDriverWait(driver, 10)
    # By deafult is the football first
    daily_coupon_body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="grid__column grid__column--fluid grid__column--main"]')))
    # Extract footbal text
    football_string = daily_coupon_body.text
    return football_string 


def stoiximan_football_export(football_string: str): 
    # Create list from the initial string
    initial_list = football_string.split('\n')
    # Remove first elements of the list not needed
    remove_elements = ['Home Soccer Next 24 Hours Full Coupon', 'Soccer - Complete Coupon',
                        'All', '3 hours', '12 hours','24 hours','By start time','By Competition',
                        'Soccer - Matches in the next 24 hours','Matches','1','X','2','O/U 2.5','GG/NG','0%',
                        'Semifinals','In neutral venue','Behind Closed Doors']
    list_1 = [x for x in initial_list if x not in remove_elements]
    # Remove elements that start with "1st leg"
    football_list = [x for x in list_1 if not x.startswith('1st leg:')]
    # Create sublists based on date (matches)
    match = [x for x in football_list if re.match(r'\d{2}/\d{2}', x)]
    index_match = [i for i,x in enumerate(football_list) if re.match(r'\d{2}/\d{2}', x)]
    sublists_matches = [football_list[i:j] for i, j in zip([0]+index_match, index_match + [len(football_list)])]
    # Exclude the initial empty list from sublist_championships
    sublists_matches = sublists_matches[1:]
    
    # Remove the last element of each sublist (extra bets)
    for sublist in sublists_matches:
        sublist.pop()
    # Add extra elements for the missing bets
    extra_element = 'No_bet'
    for sublist in sublists_matches:
        if len(sublist) < 15:
            sublist.extend([extra_element] * (15 - len(sublist)))

    # Set the filename for the output CSV file
    output_file = "data\stoiximan_football.csv"
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Time', 'Team1', 'Team2', 'One_odd', 'X_odd', 'Two_odd', 'O', 'O_odd', 
                         'U', 'U_odd', 'GG', 'GG_odd', 'NG', 'NG_odd'])
        for row in sublists_matches:
            writer.writerow(row)

######################################## Basketball ####################################################

def stoiximan_basketball_text(basketball_url: str, driver: selenium.webdriver.chrome.webdriver.WebDriver)->str: 
    # Maximize window
    driver.maximize_window()
    # Go to basketball coupon
    driver.get(basketball_url)
    # Click 24 hours button
    button_24 = driver.find_element(By.CSS_SELECTOR, '[class="events-tabs-container__tab__item__button GTM-24"]').click()
    time.sleep(5)
    
    ##### Scroll down the page and wait all values to load #####
    # Get the height of the footer element
    footer = driver.find_element(By.CSS_SELECTOR, '[class="sb-footer GTM-footer"]')
    footer_height = footer.size['height']
    # Get the height of the window
    window_height = driver.execute_script("return window.innerHeight;")
    # Initialize the last height variable with a value
    last_height = driver.execute_script("return document.body.scrollHeight")
    # Define how many times you want to scroll the webpage
    num_scrolls = 100

    # Loop through the number of times you want to scroll
    for i in range(num_scrolls):
        # Scroll down the webpage by the height of the window minus the height of the footer
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight - window.innerHeight - %s);" % footer_height)
        # Wait for the webpage to load
        time.sleep(3)
        # Get the new height of the webpage after scrolling
        new_height = driver.execute_script("return document.body.scrollHeight")
        # If the new height is the same as the old height, we have reached the end of the webpage
        if new_height == last_height:
            break
        # Otherwise, update the last height and continue scrolling
        last_height = new_height

    # Wait for the dailyCoupon_body element to be present on the page
    wait = WebDriverWait(driver, 10)
    # By deafult is the football first
    daily_coupon_body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="grid__column grid__column--fluid grid__column--main"]')))
    # Extract footbal text
    basketball_string = daily_coupon_body.text
    return basketball_string 


def stoiximan_basketball_export(basketball_string: str):
    # Create list from the initial string
    initial_list = basketball_string.split('\n')
    # Remove first elements of the list not needed
    remove_elements = ['Home Basketball Next 24 Hours Full Coupon', 'Basketball - Complete Coupon',
                        'All', '3 hours', '12 hours','24 hours','By start time','By Competition',
                        'Basketball - Matches in the next 24 hours','Matches','WIN','HANDICAP','OVER/UNDER','0%',
                        'Semifinals','In neutral venue','Behind Closed Doors']
    list_1 = [x for x in initial_list if x not in remove_elements]
    # Remove elements that start with "1st leg"
    basketball_list = [x for x in list_1 if not x.startswith('1st leg:')]
    # Create sublists based on date (matches)
    match = [x for x in basketball_list if re.match(r'\d{2}/\d{2}', x)]
    index_match = [i for i,x in enumerate(basketball_list) if re.match(r'\d{2}/\d{2}', x)]
    sublists_matches = [basketball_list[i:j] for i, j in zip([0]+index_match, index_match + [len(basketball_list)])]
    # Exclude the initial empty list from sublist_championships
    sublists_matches = sublists_matches[1:]

    # Remove the last element of each sublist (extra bets)
    for sublist in sublists_matches:
        sublist.pop()
    # Add extra elements for the missing bets
    extra_element = 'No_bet'
    for sublist in sublists_matches:
        if len(sublist) < 14:
            sublist.extend([extra_element] * (14 - len(sublist)))

    # Set the filename for the output CSV file
    output_file = "data\stoiximan_basketball.csv"
    with open(output_file, 'w', newline='',  encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Time', 'Team1', 'Team2', 'One_odd', 'Two_odd',
                         'Win1','Win1_odd','Win2', 'Win2_odd', 'O','O_odd','U','U_odd'])
        for row in sublists_matches:
            writer.writerow(row)

########################################## Tennis ######################################################

def stoiximan_tennis_text(tennis_url: str, driver: selenium.webdriver.chrome.webdriver.WebDriver)->str: 
    # Maximize window
    driver.maximize_window()
    # Go to tennis coupon
    driver.get(tennis_url)
    # Click 24 hours button
    button_24 = driver.find_element(By.CSS_SELECTOR, '[class="events-tabs-container__tab__item__button GTM-24"]').click()
    time.sleep(5)

    ##### Scroll down the page and wait all values to load #####
    # Get the height of the footer element
    footer = driver.find_element(By.CSS_SELECTOR, '[class="sb-footer GTM-footer"]')
    footer_height = footer.size['height']
    # Get the height of the window
    window_height = driver.execute_script("return window.innerHeight;")
    # Initialize the last height variable with a value
    last_height = driver.execute_script("return document.body.scrollHeight")
    # Define how many times you want to scroll the webpage
    num_scrolls = 100

    # Loop through the number of times you want to scroll
    for i in range(num_scrolls):
        # Scroll down the webpage by the height of the window minus the height of the footer
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight - window.innerHeight - %s);" % footer_height)
        # Wait for the webpage to load
        time.sleep(3)
        # Get the new height of the webpage after scrolling
        new_height = driver.execute_script("return document.body.scrollHeight")
        # If the new height is the same as the old height, we have reached the end of the webpage
        if new_height == last_height:
            break
        # Otherwise, update the last height and continue scrolling
        last_height = new_height

    # Wait for the dailyCoupon_body element to be present on the page
    wait = WebDriverWait(driver, 10)
    # By deafult is the football first
    daily_coupon_body = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="grid__column grid__column--fluid grid__column--main"]')))
    # Extract footbal text
    tennis_string = daily_coupon_body.text
    return tennis_string 


def stoiximan_tennis_export(tennis_string: str):
    # Create list from the initial string
    initial_list = tennis_string.split('\n')
    # Remove first elements of the list not needed
    remove_elements = ['Home Tennis Next 24 Hours Full Coupon', 'Tennis - Complete Coupon',
                        'All', '3 hours', '12 hours','24 hours','By start time','By Competition',
                        'Tennis - Matches in the next 24 hours','Matches','WIN','HANDICAP','OVER/UNDER','GAMES O/U','0%',
                        'Semifinals','In neutral venue','Behind Closed Doors']
    list_1 = [x for x in initial_list if x not in remove_elements]
    # Remove elements that start with "1st leg"
    tennis_list = [x for x in list_1 if not x.startswith('1st leg:')]
    # Create sublists based on date (matches)
    match = [x for x in tennis_list if re.match(r'\d{2}/\d{2}', x)]
    index_match = [i for i,x in enumerate(tennis_list) if re.match(r'\d{2}/\d{2}', x)]
    sublists_matches = [tennis_list[i:j] for i, j in zip([0]+index_match, index_match + [len(tennis_list)])]
    # Exclude the initial empty list from sublist_championships
    sublists_matches = sublists_matches[1:]

    # Remove the last element of each sublist (extra bets)
    for sublist in sublists_matches:
        sublist.pop()
    # Add extra elements for the missing bets
    extra_element = 'No_bet'
    for sublist in sublists_matches:
        if len(sublist) < 14:
            sublist.extend([extra_element] * (14 - len(sublist)))

    # Set the filename for the output CSV file
    output_file = "data\stoiximan_tennis.csv"
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date', 'Time', 'Player1', 'Player2', 'One_odd', 'Two_odd', 
                          'O','O_odd','U','U_odd', 'Win1','Win1_odd','Win2','Win2_odd'])
        for row in sublists_matches:
            writer.writerow(row)