import selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, csv

#################################### Football ####################################################

def novibet_football_text(page_url: str, driver: selenium.webdriver.chrome.webdriver.WebDriver)->str:    
    # Go to Novibet
    driver.get(page_url)
    cookies = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'acceptCookies_button'))).click()
    # Close Log in pop up window
    x_button = driver.find_element(By.CSS_SELECTOR, '[data-cy="closeBtn"]').click()  
    # Click Daily Coupon (Football)
    dayly_coupon_button = driver.find_element(By.CSS_SELECTOR, 'a.ng-star-inserted[title="Daily coupon"]').click()
    time.sleep(5)
    # Wait for the dailyCoupon_body element to be present on the page
    wait = WebDriverWait(driver, 10)
    # By deafult is the football first
    daily_coupon_body = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'dailyCoupon_body')))
    # Extract footbal text
    football_string = daily_coupon_body.text
    return football_string


def novibet_football_export(football_string: str): 
    # Create list from the initial string
    initial_list = football_string.split('\n')
    # Remove first elements of the list not needed
    remove_elements = ['Daily coupon','Football','Tennis','Basketball',
                       '24 hours','12 hours','3 hours','Popular First','SO']
    football_list = [x for x in initial_list if x not in remove_elements]

    ### I want to find a way to increace the size of i if i insert elements
    # Use padding for 'Markets are not available'
    index = 0
    # Keep track of consecutive occurrences (if I have 3 Markets No avaiblabe add 4 instead of three)
    consecutive_count = 0
    while index < len(football_list):
        if football_list[index] == 'Markets are not available':
            football_list.insert(index+1, 'No_market')
            football_list.insert(index+2, 'No_market')
            football_list.insert(index+3, 'No_market')
            index += 4
            consecutive_count += 1 
            # Check if we have 3 consecutive occurrences
            if consecutive_count == 3:
                 football_list.insert(index, 'No_market')
                 consecutive_count = 0  # Reset count
        else:
            index += 1
            consecutive_count = 0  # Reset count
    
    # Create sublists based on Championship
    championship = [x for x in football_list if ' - ' in x]
    index_championship = [i for i,x in enumerate(football_list) if ' - ' in x]
    sublists_championships = [football_list[i:j] for i, j in zip([0]+index_championship, index_championship + [len(football_list)])]
    # Exclude the initial empty list from sublist_championships
    sublists_championships = sublists_championships[1:]
    
    # Set the filename for the output CSV file
    output_file = 'data/novibet_football.csv'
    # Open the CSV file for writing
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Write the header row to the CSV file
        header = ['Championship','Team1','Team2','Time','1','1_odd','X','X_odd','2','2_odd',
                'Over','O_odd','Under','U_odd','GG','GG_odd','NG','NG_odd']
        writer.writerow(header)

        # Loop through all championships
        for j in range(len(sublists_championships)):          
            team1_lst, team2_lst = [],[]
            time_lst = []
            one_lst, one_odds_lst, x_lst, x_odds_lst, two_lst, two_odds_lst = [],[],[],[],[],[]
            over_lst, over_odds_lst, under_lst, under_odds_lst = [],[],[],[]
            gg_lst, gg_odds_lst, ng_lst, ng_odds_lst = [],[],[],[]
            # Create list with only teams and odds / exclude the championship at the beginning
            teams_only_lst = sublists_championships[j][1:]
            championship_lst = [sublists_championships[j][0] for _ in range(len(teams_only_lst) // 18)]
    
            i = 0
            while i < len(teams_only_lst):
                team1_lst.append(teams_only_lst[i])
                team2_lst.append(teams_only_lst[i+1])
                time_lst.append(teams_only_lst[i+2])
                one_lst.append(teams_only_lst[i+3])
                one_odds_lst.append(teams_only_lst[i+4])
                x_lst.append(teams_only_lst[i+5])
                x_odds_lst.append(teams_only_lst[i+6])
                two_lst.append(teams_only_lst[i+7])
                two_odds_lst.append(teams_only_lst[i+8])
                over_lst.append(teams_only_lst[i+9])
                over_odds_lst.append(teams_only_lst[i+10])
                under_lst.append(teams_only_lst[i+11])
                under_odds_lst.append(teams_only_lst[i+12])
                gg_lst.append(teams_only_lst[i+13])
                gg_odds_lst.append(teams_only_lst[i+14])
                ng_lst.append(teams_only_lst[i+15])
                ng_odds_lst.append(teams_only_lst[i+16])
                i = i + 18

            # Write each row to the CSV file
            for i in range(len(team1_lst)):
                row = [championship_lst[i], team1_lst[i], team2_lst[i], time_lst[i], one_lst[i], one_odds_lst[i], 
                        x_lst[i], x_odds_lst[i], two_lst[i], two_odds_lst[i], over_lst[i], over_odds_lst[i],
                        under_lst[i], under_odds_lst[i], gg_lst[i], gg_odds_lst[i], ng_lst[i], ng_odds_lst[i]]
                writer.writerow(row)

#################################### Basketball #########################################################     

def novibet_basketball_text(driver: selenium.webdriver.chrome.webdriver.WebDriver)->str:  
    # Click the basketball button
    basketball_button = driver.find_element(By.CSS_SELECTOR, '[class = "svgImage default BASKETBALL_GAME medium"]').click()
    time.sleep(5)
    # Wait for the dailyCoupon_body element to be present on the page
    wait = WebDriverWait(driver, 10)
    daily_coupon_body = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'dailyCoupon_body')))
    # Extract basketball text
    basketball_string = daily_coupon_body.text
    return basketball_string


def novibet_basketball_export(basketball_string: str):
    # Create list from the initial string
    initial_list = basketball_string.split('\n')
    # Remove first elements of the list not needed
    remove_elements = ['Daily coupon','Football','Tennis','Basketball',
                    '24 hours','12 hours','3 hours','Popular First','SO']
    basketball_list = [x for x in initial_list if x not in remove_elements]

    # Use padding for 'Markets are not available'
    index = 0
    # Keep track of consecutive occurrences (if I have 3 Marktes No avaiblabe add 4 instead of three)
    consecutive_count = 0
    while index < len(basketball_list):
        if basketball_list[index] == 'Markets are not available':
            basketball_list.insert(index+1, 'No_market')
            basketball_list.insert(index+2, 'No_market')
            basketball_list.insert(index+3, 'No_market')
            index += 4
            consecutive_count += 1 
            # Check if we have 3 consecutive occurrences
            if consecutive_count == 3:
                 basketball_list.insert(index, 'No_market')
                 consecutive_count = 0  # Reset count
        else:
            index += 1
            consecutive_count = 0  # Reset count

    # Create sublists based on Championship
    championship = [x for x in basketball_list if ' - ' in x]
    index_championship = [i for i,x in enumerate(basketball_list) if ' - ' in x]
    sublists_championships = [basketball_list[i:j] for i, j in zip([0]+index_championship, index_championship + [len(basketball_list)])]
    # Exclude the initial empty list from sublist_championships
    sublists_championships = sublists_championships[1:]

    # Set the filename for the output CSV file
    output_file = "data/novibet_basketball.csv"
    # Open the CSV file for writing
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Write the header row to the CSV file
        header = ['Championship','Team1','Team2','Time','win_1','odds_win_1','win_2','odds_win_2',
                    'Over','odds_over','Under','odds_under','1','odds_1','2','odds_2']
        writer.writerow(header)

        # Loop through all championships
        for j in range(len(sublists_championships)):          
            team1_lst, team2_lst = [],[]
            time_lst = []
            win_1_lst, win_1_odds_lst, win_2_lst, win_2_odds_lst = [],[],[],[]
            over_lst, over_odds_lst, under_lst, under_odds_lst = [],[],[],[]
            one_lst, one_odds_lst, two_lst, two_odds_lst = [],[],[],[]
            # Create list with only teams and odds / exclude the championship at the beginning
            teams_only_lst = sublists_championships[j][1:]
            championship_lst = [sublists_championships[j][0] for _ in range(len(teams_only_lst) // 16)]
    
            i = 0
            while i < len(teams_only_lst):
                team1_lst.append(teams_only_lst[i])
                team2_lst.append(teams_only_lst[i+1])
                time_lst.append(teams_only_lst[i+2])
                win_1_lst.append(teams_only_lst[i+3])
                win_1_odds_lst.append(teams_only_lst[i+4])
                win_2_lst.append(teams_only_lst[i+5])
                win_2_odds_lst.append(teams_only_lst[i+6])
                over_lst.append(teams_only_lst[i+7])
                over_odds_lst.append(teams_only_lst[i+8])
                under_lst.append(teams_only_lst[i+9])
                under_odds_lst.append(teams_only_lst[i+10])
                one_lst.append(teams_only_lst[i+11])
                one_odds_lst.append(teams_only_lst[i+12])
                two_lst.append(teams_only_lst[i+13])
                two_odds_lst.append(teams_only_lst[i+14])
                i = i + 16

            # Write each row to the CSV file
            for i in range(len(team1_lst)):
                row = [championship_lst[i], team1_lst[i], team2_lst[i], time_lst[i], win_1_lst[i], win_1_odds_lst[i], 
                        win_2_lst[i], win_2_odds_lst[i], over_lst[i], over_odds_lst[i], under_lst[i], under_odds_lst[i],
                         one_lst[i], one_odds_lst[i], two_lst[i], two_odds_lst[i]]
                writer.writerow(row)

#################################### Tennis ######################################################### 

def novibet_tennis_text(driver: selenium.webdriver.chrome.webdriver.WebDriver)->str:  
    # Click the Tennis button
    tennis_button = driver.find_element(By.CSS_SELECTOR, '[class = "svgImage default TENNIS_SINGLES_MATCH medium"]').click()
    time.sleep(5)
    # Wait for the dailyCoupon_body element to be present on the page
    wait = WebDriverWait(driver, 10)
    daily_coupon_body = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'dailyCoupon_body')))
    # Extract basketball text
    tennis_string = daily_coupon_body.text
    return tennis_string


def novibet_tennis_export(tennis_string: str):
    # Create list from the initial string
    initial_list = tennis_string.split('\n')
    # Remove first elements of the list not needed
    remove_elements = ['Daily coupon','Football','Tennis','Basketball',
                    '24 hours','12 hours','3 hours','Popular First','SO']
    tennis_list = [x for x in initial_list if x not in remove_elements]

    # Use padding for 'Markets are not available'
    index = 0
    # Keep track of consecutive occurrences (if I have 3 Marktes No avaiblabe add 4 instead of three)
    consecutive_count = 0
    while index < len(tennis_list):
        if tennis_list[index] == 'Markets are not available':
            tennis_list.insert(index+1, 'No_market')
            tennis_list.insert(index+2, 'No_market')
            tennis_list.insert(index+3, 'No_market')
            index += 4
            consecutive_count += 1 
            # Check if we have 3 consecutive occurrences
            if consecutive_count == 3:
                 tennis_list.insert(index, 'No_market')
                 consecutive_count = 0  # Reset count
        else:
            index += 1
            consecutive_count = 0  # Reset count

    # Create sublists based on Championship
    championship = [x for x in tennis_list if ' - ' in x]
    index_championship = [i for i,x in enumerate(tennis_list) if ' - ' in x]
    sublists_championships = [tennis_list[i:j] for i, j in zip([0]+index_championship, index_championship + [len(tennis_list)])]
    # Exclude the initial empty list from sublist_championships
    sublists_championships = sublists_championships[1:]

    
    # Set the filename for the output CSV file
    output_file = "data/novibet_tennis.csv"
    # Open the CSV file for writing
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Write the header row to the CSV file
        header = ['championship','player1','player2','time','1','odds_1','2','odds_2',
                    'Over','odds_over','Under','odds_under','win_1','odds_win_1','win_2','odds_win_2']
        writer.writerow(header)

        # Loop through all championships
        for j in range(len(sublists_championships)):       
            player1_lst, player2_lst = [],[]
            time_lst = []
            one_lst, one_odds_lst, two_lst, two_odds_lst = [],[],[],[]
            over_lst, over_odds_lst, under_lst, under_odds_lst = [],[],[],[]
            win_1_lst, win_1_odds_lst, win_2_lst, win_2_odds_lst = [],[],[],[]
            # Create list with only teams and odds / exclude the championship at the beginning
            teams_only_lst = sublists_championships[j][1:]
            championship_lst = [sublists_championships[j][0] for _ in range(len(teams_only_lst) // 16)]
    
            i = 0
            while i < len(teams_only_lst):
                player1_lst.append(teams_only_lst[i])
                player2_lst.append(teams_only_lst[i+1])
                time_lst.append(teams_only_lst[i+2])
                one_lst.append(teams_only_lst[i+3])
                one_odds_lst.append(teams_only_lst[i+4])
                two_lst.append(teams_only_lst[i+5])
                two_odds_lst.append(teams_only_lst[i+6])
                over_lst.append(teams_only_lst[i+7])
                over_odds_lst.append(teams_only_lst[i+8])
                under_lst.append(teams_only_lst[i+9])
                under_odds_lst.append(teams_only_lst[i+10])
                win_1_lst.append(teams_only_lst[i+11])
                win_1_odds_lst.append(teams_only_lst[i+12])
                win_2_lst.append(teams_only_lst[i+13])
                win_2_odds_lst.append(teams_only_lst[i+14])
                i = i + 16

            # Write each row to the CSV file
            for i in range(len(player1_lst)):
                row = [championship_lst[i], player1_lst[i], player2_lst[i], time_lst[i], one_lst[i], one_odds_lst[i],
                       two_lst[i], two_odds_lst[i], over_lst[i], over_odds_lst[i], under_lst[i], under_odds_lst[i],
                       win_1_lst[i], win_1_odds_lst[i], win_2_lst[i], win_2_odds_lst[i]]
                writer.writerow(row)