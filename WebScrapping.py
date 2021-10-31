from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time


# This path might be different for you. Make sure you set the right path for the driver.
PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# For example if you want to download data from all stars with RA 90 to 95 just input "90 95" without the quotes ofc
RA_range = list(map(int, input("Enter the range of RA values you want to download from: ")))


def Get_from_RA(times):

    # variables:
    start = times
    end = start + 0.5
    index = 2*times + 1

    try:
        WebDriverWait(driver, 15).until(
            ec.element_to_be_clickable((By.ID, "textfield-1208-inputEl")))
    except:
        driver.quit()

    # Selecting the first input box to enter the interval
    input_start = driver.find_element_by_id("textfield-1208-inputEl")
    input_start.clear()
    input_start.send_keys(str(start))  # Starting interval
    input_start.send_keys(Keys.RETURN)

    # Selecting the second input box to enter the interval
    input_end = driver.find_element_by_id("textfield-1209-inputEl")
    input_end.clear()

    # There seems to a bug where input_start gets copied to input_end
    for x in range(0 if start == 0 else len(str(start))):
        input_end.send_keys(Keys.BACKSPACE)
    input_end.send_keys(str(end))  # Ending interval
    input_end.send_keys(Keys.RETURN)

    # Selecting the first export button
    export_button = WebDriverWait(driver, 10).until(
        ec.presence_of_element_located((
            By.XPATH, "/html/body/div[10]/div[3]/div/div[1]/div/div/div/a[2]/span/span/span[2]"
        ))
    )
    export_button.click()

    for j in range(15):
        try:
            file_name = driver.find_element_by_xpath("/html/body/div[" + str(
                j) + "]/div[3]/div/div/div/div/fieldset/div/div/div/div/div/div/div/div[1]/\
                div[1]/div[1]/div/input")
            file_name.clear()
            file_name.send_keys("StarData_" + str(index) + ".csv" + Keys.RETURN)
            driver.find_element_by_xpath("/html/body/div[" + str(j) + "]/div[3]/div/div/div/\
                div/fieldset/div/div/div/div/div/div/div/div[6]/div/div/a[1]/span/span/span[2]").click()
            break

        except:
            continue

# Opening the MAST website
driver.get("https://mast.stsci.edu/portal/Mashup/Clients/Mast/Portal.html")

# clicking the first drop-down arrow
drag_button1 = driver.find_element_by_id("combo-1111-trigger-picker")
drag_button1.click()

# selecting 'MAST Catalog' option in the first drop-down
drag_button1_option = driver.find_element_by_id("liActionChooserTopBar_MASTCATALOG")
drag_button1_option.click()

# clicking the second drop-down arrow
drag_button2 = WebDriverWait(driver, 10).until(
    ec.presence_of_element_located((By.ID, "combo-1114-trigger-picker"))
)

drag_button2.click()

# selecting 'TESS CTL v8.01' option in the second drop-down
drag_button2_option = driver.find_element_by_id("liMastCatalogChooserTopBar_Ctl")
drag_button2_option.click()
time.sleep(1)

# Clicking on the "Advanced Search" option
driver.find_element_by_link_text("Advanced Search").click()

for i in range(RA_range[0], RA_range[1] + 1):
    Get_from_RA(i)
    Get_from_RA(i + 0.5)
    
print("download completed")
