import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, csv

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
    
    ### Scroll down the page and wait all values to load ###
    # Get browser height
    browser_window_height = driver.get_window_size(windowHandle='current')['height']
    current_position = driver.execute_script('return window.pageYOffset')
    while True:
        # Get the total height of the web page
        total_page_height = driver.execute_script("return document.body.scrollHeight")
        # Exit the loop if we've reached the bottom of the page
        if total_page_height <= current_position + browser_window_height:
            break
        # Scroll down the page
        driver.execute_script(f"window.scrollTo({current_position}, {browser_window_height + current_position});")
        # Update the current position
        current_position = driver.execute_script('return window.pageYOffset')
        time.sleep(5)

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
    'Soccer - Matches in the next 24 hours','Matches','1','X','2','O/U 2.5','GG/NG','0%','Semifinals','In neutral venue']
    list_1 = [x for x in initial_list if x not in remove_elements]
    # Remove elements that start with "1st leg"
    football_list = [x for x in list_1 if not x.startswith('1st leg:')]
    # Create sublists based on date (matches)
    match = [x for x in football_list if '/' in x]
    index_match = [i for i,x in enumerate(football_list) if '/' in x]
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
    output_file = "stoiximan_football.csv"
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['date', 'time', 'team1', 'team2', '1', 'X', '2', 'O', 'O_odds', 
                         'U', 'U_odds', 'Yes', 'Yes_odds', 'No', 'No_odds'])
        for row in sublists_matches:
            writer.writerow(row)

######################################## Basketball ####################################################


########################################## Tennis ######################################################