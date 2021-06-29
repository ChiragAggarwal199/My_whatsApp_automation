import VBMessages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pyautogui
import keyboard

driver = webdriver.Chrome(executable_path=r"C:\Users\hp\PycharmProjects\SiteProject\chromedriver.exe")
driver.get("https://web.whatsapp.com")
driver.maximize_window()

Members = [[ 6239631173,'''HI Coustmer;Good Morning''']]
Faulty = []

keyboard.wait('Esc')
while True:
    Selection_Box = pyautogui.confirm(text="Message Or Image", title="Selection Box",
                                      buttons=["Image", "Message", "Quit"])
    if Selection_Box == 'Message':
        sleep(4)
        for coustmer in Members:
            search_box = driver.find_element_by_xpath(
                "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
            search_box.click()
            search_box.send_keys(str(int(coustmer[0])) + '\n')
            if search_box.text == '':
                while True:
                    try:
                        msg_box = driver.find_element_by_xpath(
                            "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
                        msg_box.click()
                        msg = str(coustmer[1]).split(";")
                        for i in ms:
                            msg_box.send_keys(i)
                            msg_box.send_keys(Keys.SHIFT + Keys.ENTER)
                        msg_box.send_keys('\n')
                        break
                    except:
                        sleep(0.2)
            else:
                Faulty.append(coustmer)
                search_box.clear()
                continue
        if len(Faulty) > 0:
            print(Faulty)
            pyautogui.confirm(text=Faulty, title='UnsetMessages')
        else:
            pyautogui.confirm(text="All Messages Sent Successfully.", title='UnsetMessages')
        continue
    elif Selection_Box == 'Image':
        while True:
            img_box = pyautogui.confirm(text='Have You Copied Image ??', title='Confirmation',
                                        buttons=['Continue', 'No', 'Quit'])
            if img_box == 'Continue':
                sleep(3)
                for number in Members:
                    search_box = driver.find_element_by_xpath(
                        "/html/body/div[1]/div/div/div[3]/div/div[1]/div/label/div/div[2]")
                    search_box.click()
                    search_box.send_keys(str(int(number[0])) + '\n')
                    if search_box.text == '':
                        while True:
                            try:
                                not_box = driver.find_element_by_xpath(
                                    "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")
                                not_box.click()
                                keyboard.press_and_release('Ctrl+v')
                                break
                            except:
                                sleep(0.2)
                        sleep(0.1)
                        while True:
                            try:
                                msg_box = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]")
                                msg_box.click()
                                for i in str(number[1]).split("\n"):
                                    msg_box.send_keys(i)
                                    msg_box.send_keys(Keys.SHIFT + Keys.ENTER)
                                msg_box.send_keys('\n')
                                break
                            except:
                                sleep(0.2)
                    else:
                        Faulty.append(number)
                        search_box.clear()
                        continue
                if len(Faulty) > 0:
                    print(Faulty)
                    pyautogui.confirm(text=Faulty, title='UnsetMessages')
                else:
                    pyautogui.confirm(text="All Messages Sent Successfully.", title='UnsetMessages')
                continue
            elif img_box == 'No':
                sleep(10)
            elif img_box == 'Quit':
                quit()
    elif Selection_Box == 'Quit':
        quit()