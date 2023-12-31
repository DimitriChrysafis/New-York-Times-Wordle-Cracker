from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

driver = webdriver.Chrome()
url = 'https://www.nytimes.com/games/wordle/index.html'
driver.get(url)

try:
    login_form = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/button")
    login_form.click()
    time.sleep(1)
    second_button = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[2]/button[2]")
    second_button.click()
    time.sleep(1)

    third_button = driver.find_element(By.XPATH, "/html/body/div/div/dialog/div/button")
    third_button.click()

    driver.execute_script("window.scrollBy(0, 200)")
    time.sleep(2)

    word = "adieu"
    pyautogui.typewrite(word)
    pyautogui.press("enter")

    time.sleep(5)

    absent_tiles = driver.find_elements(By.CSS_SELECTOR, ".Tile-module_tile__UWEHN[data-state=absent]")
    present_tiles = driver.find_elements(By.CSS_SELECTOR, ".Tile-module_tile__UWEHN[data-state=present]")
    correct_tiles = driver.find_elements(By.CSS_SELECTOR, ".Tile-module_tile__UWEHN[data-state=correct]")

    indices = "nnnnn"

    print("Absent Tiles:")
    for tile in absent_tiles:
        letter = tile.get_attribute("data-letter")
        tile_text = tile.text.lower()
        print(f"Letter: {letter}, Text: {tile_text}")

        position = word.find(tile_text) + 1
        print(f"Position in Word: {position}")

        if position != 0:
            indices = indices[:position - 1] + "n" + indices[position:]

    print("Present Tiles:")
    for tile in present_tiles:
        letter = tile.get_attribute("data-letter")
        tile_text = tile.text.lower()
        print(f"Letter: {letter}, Text: {tile_text}")

        position = word.find(tile_text) + 1
        print(f"Position in Word: {position}")

        if position != 0:
            indices = indices[:position - 1] + "p" + indices[position:]

    print("Correct Tiles:")
    for tile in correct_tiles:
        letter = tile.get_attribute("data-letter")
        tile_text = tile.text.lower()
        print(f"Letter: {letter}, Text: {tile_text}")

        position = word.find(tile_text) + 1
        print(f"Position in Word: {position}")

        if position != 0:
            indices = indices[:position - 1] + "c" + indices[position:]

    print(f"Indices: {indices}")

    input("Press Enter to quit the browser...")
except KeyboardInterrupt:
    pass
finally:
    driver.quit()
