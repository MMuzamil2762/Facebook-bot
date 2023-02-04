from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import chromedriver_autoinstaller
import time
import concurrent.futures
import random


# ============================================================
# email = "mmhaw994@gmail.com"
# password = "mmhaw2762"
# ============================================================


def auth_code(auth, chrome):
    extension_url = "chrome-extension://bhghoamapcdpbohphigoooaddinpkbai/view/popup.html"

    chrome.get(extension_url)
    time.sleep(2)
    chrome.find_element(By.ID, "i-edit").click()
    chrome.find_element(By.ID, "i-plus").click()
    chrome.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/button[2]").click()
    chrome.find_element(By.CLASS_NAME, "input").send_keys(auth)
    chrome.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[2]/input").send_keys(auth)
    chrome.find_element(By.CLASS_NAME, "button-small").click()
    data = chrome.page_source
    clean = BeautifulSoup(data, "html.parser")
    print("Page Soucrce:", clean.find(class_="message-box").text)
    if "Invalid" not in clean.find(class_="message-box").text:
        raw_code = clean.find(class_="code")
        for d in raw_code:
            code = d

    else:
        code = "error"

    return code


def facebook_bot(credentials_lst, profile_ids, comments):
    chrome_options = Options()

    chrome_options.add_extension('extension_6_3_3_0.crx')

    chromedriver_autoinstaller.install()
    chrome = webdriver.Chrome(options=chrome_options)

    email = credentials_lst[0]
    password = credentials_lst[1]
    auth = credentials_lst[2]

    comment = random.choice(comments)

    login_url = "https://m.facebook.com/login"
    # profile_ids = profile_ids[:1]
    print(profile_ids)
    print(email, password)

    chrome.get(login_url)
    time.sleep(5)

    chrome.find_element(By.ID, "m_login_email").send_keys(email)
    chrome.find_element(By.ID, "m_login_password").send_keys(password)
    chrome.find_element(By.NAME, "login").send_keys(Keys.ENTER)
    time.sleep(5)

    print("wait for others")
    # barrier.wait()
    curr_url = chrome.current_url

    if curr_url == login_url:
        print("Password Incorrect.....!!!!!!!!!!!")
        chrome.delete_all_cookies()
        return 0

    code = auth_code(auth, chrome)
    if code == "error":
        print("Account Blocked.........!!!!!!!!!")
        chrome.delete_all_cookies()
        return 0

    chrome.get(curr_url)
    try:
        chrome.find_element(By.ID, "approvals_code").send_keys(code)
        chrome.find_element(By.ID, "checkpointSubmitButton-actual-button").click()
        time.sleep(4)
        chrome.find_element(By.ID, "checkpointSubmitButton-actual-button").click()
        time.sleep(4)
        chrome.find_element(By.ID, "checkpointSubmitButton-actual-button").click()
        time.sleep(4)
        chrome.find_element(By.ID, "checkpointSubmitButton-actual-button").click()
        time.sleep(4)
        chrome.find_element(By.ID, "checkpointSubmitButton-actual-button").click()
        time.sleep(4)
        chrome.find_element(By.ID, "checkpointSubmitButton-actual-button").click()
    except:
        pass
    print("Logging in")
    time.sleep(6)

    for profile_id in profile_ids:
        url = "https://m.facebook.com/" + profile_id

        chrome.get(url)
        print("Reached Profile")
        time.sleep(6)

        try:
            chrome.find_element(By.XPATH,
                                "/html/body/div[1]/div/div[4]/div/div[1]/div/div[2]/div[3]/div[3]/section/article[1]/footer/div/div[2]/div[2]/a").click()
            print("Profile Comment Section")
            time.sleep(5)

            chrome.find_element(By.ID, "composerInput").send_keys(comment)
            print("Comment Writed")
            time.sleep(3)

            chrome.find_element(By.NAME, "submit").click()
            chrome.find_element(By.NAME, "submit").click()
            time.sleep(3)
            print(f"Comment Submited: {url}")

        except:
            pass

    chrome.delete_all_cookies()


if __name__ == "__main__":
    access_lst = [["tolpeeva_lilya@mail.ru", "u46PejsVc", "RKMW SKRU 7LBF OXIO PBRJ PBG7 ZSZV X3QL"],
                  ["lushchenkova_khristina@mail.ru", "vb6xUhErL5", "ZDC5 6PIL RNJT AP2A BYDZ J4HM 3K7K W2XY"],
                  ["hanahesser56@yahoo.com", "mGm0JNEv4ss", "WJ7S 2XTO ZNGS UCT2 6XMG LOJT RHG7 GJPK"],
                  ["stas.shevarukhin.80@mail.ru", "0PY0ctlejZ", "CQEO KCVB 3FLY XRBK CXYJ WQ2K JFY2 624W"],
                  ["sanjuanitamccord6@yahoo.com", "nI6svqYxDar", "KYG2 WWJ4 EEYD HCFU 2GM5 XS6J WO3Z RZ3U"]]

    profile_ids_lst = [["100010862103407", "100010629550649", "100010589628682"],
                       ["100010876714534", "100010895227929", "100010938360097"]]

    comment_lst = ["great", "Nice Work", "Awesome", "Great Buddy"]

    cmt = "looking good"

    # for account in access_lst:
    #     facebook_bot(account)
    # facebook_bot(access_lst[0], profile_ids_lst[-1], comment_lst)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(facebook_bot, access_lst, profile_ids_lst, comment_lst)
    # for account in access_lst:
    #     executor.submit(facebook_bot, account, profile_ids_lst, comment_lst)

    # with ThreadPoolExecutor(max_workers=2) as executor:
    #     executor.map(facebook_bot, lst)

    # no_of_threads = 2
    # barrier = Barrier(no_of_threads)
    # threads = []
    # for i in range(no_of_threads):
    #     t = Thread(target=facebook_bot, args=(lst, barrier,))
    #     t.start()
    #     threads.append(t)
    #
    # for t in threads:
    #     t.join()
