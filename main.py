############# ---- #############
from os import path
import random
from time import process_time, sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

class Instabot:
    def __init__(self, executable_path, hidebrowser=False):

        browser_options = Options()

        if hidebrowser:
            browser_options.add_argument('--headless')

        self.browser = webdriver.Firefox(
            executable_path=executable_path, options=browser_options)

        print("[+] - STARTING BOT ...")

    def getcbrowser(self):
        return self.browser

    def rep(self, fullname, email, username, phonenumber, message, count):

        for i in range(count):

            url = "https://help.instagram.com/contact/606967319425038?helpref=page_content"
            self.browser.get(url)

            sleep(2)

            fullname_input = self.browser.find_element_by_css_selector(
                "input[id='649649255120112']")
            email_input = self.browser.find_element_by_css_selector(
                "input[id='328991337275965']")
            username_input = self.browser.find_element_by_css_selector(
                "input[id='1464214030500550']")
            phonenumber_input = self.browser.find_element_by_css_selector(
                "input[id='602863763172693']")
            message_input = self.browser.find_element_by_css_selector(
                "textarea[id='709786765737601']")
            submit_button = self.browser.find_element_by_css_selector(
                "button")

            fullname_input.send_keys(fullname)
            email_input.send_keys(email)
            username_input.send_keys(username)
            phonenumber_input.send_keys(phonenumber)
            message_input.send_keys(message)
            submit_button.click()

            print("[+] - Sleeping 50s")
            sleep(50)
            

    def login(self, username, password):

        self.loginusername = username
        self.loginpassword = password

        self.instaloginurl = "https://www.instagram.com/accounts/login/"

        print("[+] - Getting login page | Loading ...")

        self.browser.get(self.instaloginurl)

        sleep(2)

        username_input = self.browser.find_element_by_css_selector(
            "input[name='username']")
        password_input = self.browser.find_element_by_css_selector(
            "input[name='password']")
        submit_button = self.browser.find_element_by_xpath(
            "//button[@type='submit']")

        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()

        print("[+] - You have logged in successfully")

        sleep(12)
        # self.browser.get("https://www.instagram.com/accounts/onetap/")

    def getuserpage(self, user):

        print("[+] - Getting user page | loading ...")

        self.targetusername = user

        self.userpageurl = "https://www.instagram.com/{}/".format(user)

        try:
            self.browser.get(self.userpageurl)

            print("[+] - The user page has been fetched successfully")

        except:

            print("[+] - The user page was not successfully fetched")

    def getpost(self, posturl):

        print("[+] - Getting post | loading ...")

        try:
            self.browser.get(posturl)

            print("[+] - The post has been fetched successfully")
        except:
            print("[+] - The post was not successfully fetched")

        sleep(6)

    def getpostowner(self):

        try:
            post_owner = self.browser.find_element_by_css_selector(
                ".sqdOP.yWX7d._8A5w5.ZIAjV").text
            return f"[+] - This is posted under the username {post_owner}"
        except:
            return "[+] - Can't find username .!"

    def getlikepostbool(self):

        likestatus = None

        # "span.fr66n button.wpO6b[type='button'] .QBdPU .FY9nT svg"

        # "span.fr66n button.wpO6b[type='button']"
        try:
            likertext = self.browser.find_element_by_css_selector(
                "span.fr66n button.wpO6b[type='button'] .QBdPU span svg").get_attribute("aria-label").lower()

            if likertext == "like":
                likestatus = False
            elif likertext == "unlike":
                likestatus = True
            return likestatus

        except:
            return "stop"

    def likepost(self, boollike):

        print("[+] - LIKING ...")
        sleep(2)
        #"span.fr66n button.wpO6b[type='button']"
        like_button = self.browser.find_element_by_css_selector(
            "span.fr66n button.wpO6b[type='button']")

        if self.getlikepostbool() == True:

            if not boollike:
                like_button.click()
                print("[+] - Removing like sign")
        else:
            if boollike:
                like_button.click()
                print("[+] - Adding like sign")

    def sendpost(self, userslist):

        print("[+] - SENDING ...")
        sleep(2)

        sendpost_button = self.browser.find_element_by_css_selector(
            "span._5e4p button.wpO6b[type=button]")
        sendpost_button.click()

        print("[+] - Searching and selecting user ...")
        sleep(6)

        for user in userslist:

            search_input = self.browser.find_element_by_css_selector(
                "input.j_2Hd.uMkC7.M5V28[name='queryBox']")
            search_input.send_keys(user + Keys.RETURN)

            sleep(4)

            usertg = self.browser.find_elements(
                By.CSS_SELECTOR, "div.Igw0E.rBNOH.eGOV_.ybXk5._4EzTm.XfCBB.HVWg4")
            usertg[0].click()

            print(f"[+] - Select {user}")

        print("[+] - Send post for all users ...")

        send_button = self.browser.find_element_by_css_selector(
            "button.sqdOP.yWX7d.y3zKF.cB_4K[type=button]")
        send_button.click()

    def commentpost(self, commentlist, lenpm=6, countforrepeatcomment=1):

        print("[+] - COMMENTING ...")
        sleep(2)

        comment_count = 0

        post_owner = self.getpostowner()

        print(f"[+] - This is posted under the username {post_owner}")

        if self.getlikepostbool() == True:
            liketext = "like"
        else:
            liketext = "unlike"

        print(f"[+] - You put a {liketext} sign in this post")

        print("[+] - Start making comments ...")

        for i in range(countforrepeatcomment):

            commentlist = randomlist(commentlist, lenpm)

            for commenttext in commentlist:

                comment_input = self.browser.find_element_by_css_selector(
                    "textarea[aria-label]")

                sleep(4)
                # 'Add a comment???'

                self.browser.execute_script(
                    """document.querySelector("textarea[aria-label]").value = ''""")

                # click on textarea/comment box and enter comment
                (
                    ActionChains(self.browser)
                    .move_to_element(comment_input)
                    .click()
                    .send_keys(commenttext + Keys.RETURN)
                    .perform()

                )

                print(f" # {comment_count} - {commenttext}")

                print("[+] - Posting comment ...")

                comment_count += 1

                # if comment_count % 5 == 0:
                #     print("[+] - Sleeping ( 20 ) seconds ...")
                #     sleep(10)

                # if comment_count % 15 == 0:
                #     print("[+] - Sleeping ( 40 ) seconds ...")
                #     sleep(40)

    def likeandcommentallposts(self, commentlist, boollike, countforrepeatcomment=1, countforrepeatallfn=1):

        print("[+] - COMMENTING AND LIKING FOR ALL POSTS HIS HAVE ...")
        sleep(2)
        #    , commentlist, countforrepeatecomment, boollike

        for i in range(countforrepeatallfn):

            print("[+] - Getting all posts | Loading ...")

            sleep(4)

            allposts = self.browser.find_elements(
                By.CSS_SELECTOR, "div.v1Nh3.kIKUG._bz0w")

            for postdiv in allposts:

                # open post :
                print("[+] - Opening post")
                postdiv.click()

                sleep(4)

                # set like sign :
                self.likepost(boollike)

                # loop cooment :
                self.commentpost(commentlist, countforrepeatcomment)

                sleep(2)

                # close post :
                print("[+] - Closing post")
                # close_div = self.browser.find_element_by_css_selector(
                #     "div._2dDPU.CkGkG[role='dialog']")

                close_button = self.browser.find_element_by_css_selector(
                    ".Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG button.wpO6b[type='button']")

                # ".Igw0E.IwRSH.eGOV_._4EzTm.BI4qX.qJPeX.fm1AK.TxciK.yiMZG button.wpO6b[type='button']"
                close_button.click()

                sleep(2)

                allposts = self.browser.find_elements(
                    By.CSS_SELECTOR, "div.v1Nh3.kIKUG._bz0w")


############# ---- #############

insta = Instabot("geckodriver.exe")

insta.rep(
    # fullname :
    "Bet??l T??rky??lmaz",
    # email :
    "betulaselll@yandex.com",
    # username :
    "betultrkylmaz_",
    # phonenumber :
    "+905070609322",
    # message :
    "Hi, Instagram Team my account has been disabling for violating terms, I think it has been a mistake, please recover my account .",
    # loop :
    1000)


