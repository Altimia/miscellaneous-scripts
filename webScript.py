from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 
# Open the file containing the hex strings
with open('unique.txt', 'r') as file:
    hex_vals = file.read().splitlines()
 
# Initialize the Chrome driver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
 
# Open the output file
with open('no_map.txt', 'w') as outfile:
    for index, hex_val in enumerate(hex_vals):
        try:
            # Load the website
            driver.get('https://beatsaver.com/')
     
            # Input the hex string into the search bar
            search_bar = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="search"]')))
            search_bar.send_keys(hex_val)
     
            # Click the search button
            search_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))
            search_btn.click()
    
            # Wait until the single map page loads then click the One-Click button
            one_click_btn = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@title="One-Click"]')))
            one_click_btn.click()
        except Exception as e:
            print(f"An error occurred while processing hex value {hex_val}: {str(e)}")
            # Write the hex value to the output file
            outfile.write(hex_val + '\n')
            continue
     
        # Print the progress of the script
        print(f"Progress: {index + 1}/{len(hex_vals)}")
 
# Close the driver
driver.quit()