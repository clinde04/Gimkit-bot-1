from selenium import webdriver

import time

from colorama import Fore


options = webdriver.ChromeOptions();
options.add_experimental_option("excludeSwitches", ['enable-automation']);
options.add_argument('--start-maximized')

driver = webdriver.Chrome(executable_path='workspace\Gimkit-bot-1\chromedriver', options= options) 

driver.get("https://www.gimkit.com/live")

#if input game code form appear
while True:
    try:
        elem = driver.find_element_by_xpath(xpath="//input[contains(@class, 'sc-eIVEXM hBRYKu')]")
    except:
        pass
    else:
        if elem.get_attribute('placeholder') == 'Game Code':
            print("{}[?] {}Please input game code!{}".format(Fore.RESET, Fore.CYAN, Fore.RESET))
            break

#if input player name appear
while True:
    try:
        elem = driver.find_element_by_xpath(xpath="//input[contains(@class, 'sc-eIVEXM hBRYKu')]")
    except:
        pass
    else:
        if elem.get_attribute('placeholder') == 'Your Name':
            print("{}[?] {}Please input your name!{}".format(Fore.RESET, Fore.CYAN, Fore.RESET))
            break

#if waiting lobby appear
while True:
    try:
        elem = driver.find_element_by_xpath(xpath="//div[contains(@class, 'sc-efAmGo coKrHv')]")
    except:
        pass
    else:
        if elem.text == 'Get ready...':
            print("{}[?] {}Wait till the game to start!{}".format(Fore.RESET, Fore.CYAN, Fore.RESET))
            break

#if money progess bar appear -> game start
while True:
    try:
        elem = driver.find_element_by_xpath(xpath="//div[contains(@class, 'sc-ioBwqd cqUMAV')]")
    except:
        pass
    else:
        print("{}[?] {}Game started!{}".format(Fore.RESET, Fore.CYAN, Fore.RESET))
        break


class Question:
    def __init__(self, question):
        self.question = question
        
        self.answer = "None"

        self.dict_answer = {
            1 : {"answer" : "None",
                "bool" : None},
            2 : {"answer" : "None",
                "bool" : None},
            3 : {"answer" : "None",
                "bool" : None},
            4 : {"answer" : "None",
                "bool" : None}
        }



class Position:
    #top left: x y
    tlX = 0
    tlY = 0
    #bottom right: x y
    brX = 0
    brY = 0

red_answer_position = Position()
orange_answer_position = Position()
green_answer_position = Position()
blue_answer_position = Position()
question_position = Position()


def on_press(key):
    # print('{0} pressed'.format(key))
    global last_selected_answer
    if key == "'1'":
        while True:
            try:
                red_answer_container = driver.find_element_by_xpath(xpath="/html[@class='focus-outline-hidden']/body/div[@id='root']/div[@class='sc-fsPSfr jnZcev']/div/div[@id='content']/div[1]/div[@class='sc-bMbkRG ekUWsb']/div[@class='sc-whdbJ kKBEZb']/div[@class='sc-TZjqS hzeXst']/div/div[@class='sc-bQQHgq fHpdyf fade-router-enter-done']/div[@class='sc-bKcCCv kdVWkL']/div[@class='sc-eKQksS fzkzxu'][1]/div[@class='sc-hJfILt hkooIz']/div")
                last_selected_answer = "red"

            except:
                pass
            else:
                red_answer_container.click()                
                
                break
    elif key == "'2'":
        while True:
            try:
                orange_answer_container = driver.find_element_by_xpath(xpath="/html[@class='focus-outline-hidden']/body/div[@id='root']/div[@class='sc-fsPSfr jnZcev']/div/div[@id='content']/div[1]/div[@class='sc-bMbkRG ekUWsb']/div[@class='sc-whdbJ kKBEZb']/div[@class='sc-TZjqS hzeXst']/div/div[@class='sc-bQQHgq fHpdyf fade-router-enter-done']/div[@class='sc-bKcCCv kdVWkL']/div[@class='sc-eKQksS fzkzxu'][2]/div[@class='sc-hJfILt idzska']")
            except:
                pass
            else:

                orange_answer_container.click()
                last_selected_answer = "orange"
                break
    elif key == "'3'":
        while True:
            try:
                green_answer_container = driver.find_element_by_xpath(xpath="/html[@class='focus-outline-hidden']/body/div[@id='root']/div[@class='sc-fsPSfr jnZcev']/div/div[@id='content']/div[1]/div[@class='sc-bMbkRG ekUWsb']/div[@class='sc-whdbJ kKBEZb']/div[@class='sc-TZjqS hzeXst']/div/div[@class='sc-bQQHgq fHpdyf fade-router-enter-done']/div[@class='sc-bKcCCv kdVWkL']/div[@class='sc-eKQksS fzkzxu'][3]/div[@class='sc-hJfILt lcJMJC']")
            except:
                pass
            else:

                green_answer_container.click()
                last_selected_answer = "green"
                break
    elif key == "'4'":
        while True:
            try:
                blue_answer_container = driver.find_element_by_xpath(xpath="/html[@class='focus-outline-hidden']/body/div[@id='root']/div[@class='sc-fsPSfr jnZcev']/div/div[@id='content']/div[1]/div[@class='sc-bMbkRG ekUWsb']/div[@class='sc-whdbJ kKBEZb']/div[@class='sc-TZjqS hzeXst']/div/div[@class='sc-bQQHgq fHpdyf fade-router-enter-done']/div[@class='sc-bKcCCv kdVWkL']/div[@class='sc-eKQksS fzkzxu'][4]/div[@class='sc-hJfILt jrviZn']")
            except:
                pass
            else:

                blue_answer_container.click()
                last_selected_answer = "blue"
                break
    elif str(key) == "Key.space":
        while True:
            try:
                continue_answer_container = driver.find_element_by_xpath(xpath="/html[@class='focus-outline-hidden']/body/div[@id='root']/div[@class='sc-fsPSfr jnZcev']/div/div[@id='content']/div[1]/div[@class='sc-bMbkRG ekUWsb']/div[@class='sc-whdbJ kKBEZb']/div[@class='sc-TZjqS hzeXst']/div/div[@class='fade-router-enter-done']/div[@class='sc-ieSwJA dkSJHi']/div[@class='sc-nUItV hrXxNi']/span[2]")
            except:
                pass
            else:
                continue_answer_container.click()
                break
    elif str(key) == "'`'":
        while True:
            try:
                shop_container = driver.find_element_by_xpath(xpath="/html[@class='focus-outline-hidden']/body/div[@id='root']/div[@class='sc-fsPSfr jnZcev']/div/div[@id='content']/div[1]/div[@class='sc-bMbkRG ekUWsb']/div[@class='sc-whdbJ kKBEZb']/div[@class='sc-TZjqS hzeXst']/div/div[@class='fade-router-enter-done']/div[@class='sc-ieSwJA dkSJHi']/div[@class='sc-nUItV hrXxNi']/span[1]")
            except:
                pass
            else:
                shop_container.click()
                break
    
    elif str(key) == "Key.ctrl_l":
        #view correct answer

        pass


import winsound

selected_answer = "None"

list_questions = list()

import keyboard


def keypress(event):
    global selected_answer
    global list_questions
    if str(event.name) == "1":
        selected_answer = red_answer_text

    elif str(event.name) == "2":
        selected_answer = orange_answer_text
        
    elif str(event.name) == "3":
        selected_answer = green_answer_text
        
    elif str(event.name) == "4":
        selected_answer = blue_answer_text

    elif str(event.name) == "ctrl":
        print("======Printing questions list======")
        for question_obj in list_questions:
            print("***")
            print(f"Question = {question_obj.question} : answer = {question_obj.answer}")    
            print(question_obj.dict_answer[1])
            print(question_obj.dict_answer[2])
            print(question_obj.dict_answer[3])
            print(question_obj.dict_answer[4])
            print("***")

    #fast shop open
    elif str(event.name) == "`":
        try:
            shop_button = driver.find_element_by_xpath("/html/body/div[@id='root']/div[@class='sc-fsPSfr jnZcev']/div/div[@id='content']/div[1]/div[@class='sc-bMbkRG ekUWsb']/div[@class='sc-whdbJ kKBEZb']/div[@class='sc-TZjqS hzeXst']/div/div[@class='fade-router-enter-done']/div[@class='sc-ieSwJA dkSJHi']/div[@class='sc-nUItV hrXxNi']/span[1]")
        except:
            pass
        else:
            shop_button.click

keyboard.on_press(keypress)

bool_auto_continue_until_have_enough_money = True

bot_start = True

global red_answer_text
global orange_answer_text
global green_answer_text
global blue_answer_text

question_text = "None"
red_answer_text = "None"
orange_answer_text = "None"
green_answer_text = "None"
blue_answer_text = "None"

#bot working
while bot_start:
    while True:
        time.sleep(1)
        #gather data: getting currently question and 4 answers
        try:
            question = driver.find_element_by_xpath(xpath="//div[@class='sc-eGMfeR OzGgw']//span")
            red_answer = driver.find_element_by_xpath(xpath="//div[contains(@class, 'sc-hJfILt hkooIz')]")             
            orange_answer = driver.find_element_by_xpath(xpath="//div[contains(@class, 'sc-hJfILt idzska')]")
            green_answer = driver.find_element_by_xpath(xpath="//div[contains(@class, 'sc-hJfILt lcJMJC')]")
            blue_answer = driver.find_element_by_xpath(xpath="//div[contains(@class, 'sc-hJfILt jrviZn')]")
        except:
            pass
        else:
            question_text = question.text
            red_answer_text = red_answer.text
            orange_answer_text = orange_answer.text
            green_answer_text = green_answer.text
            blue_answer_text = blue_answer.text

            is_exist = False

            for question_obj in list_questions:
                #find currently question in list_questions
                if question_obj.question == question_text:
                    #if this question has answer
                    if question_obj.answer != "None":
                        #auto answer if currently question has answer
                        if question_obj.answer == red_answer_text:
                            keyboard.send( "1" )
                        elif question_obj.answer == orange_answer_text:
                            keyboard.send( "2" )
                        elif question_obj.answer == green_answer_text:
                            keyboard.send( "3" )
                        elif question_obj.answer == blue_answer_text:
                            keyboard.send( "4" )
                    is_exist = True
                    break

            if is_exist == False:
                list_questions.append(Question(question = question_text))
                list_questions[-1].dict_answer[1]["answer"] = red_answer_text
                list_questions[-1].dict_answer[2]["answer"] = orange_answer_text
                list_questions[-1].dict_answer[3]["answer"] = green_answer_text
                list_questions[-1].dict_answer[4]["answer"] = blue_answer_text

            #done work.
            winsound.PlaySound('ting.wav', winsound.SND_FILENAME)

            break


    while True:
        # #check green box appear when choose correct answer
        try:
            correct_answer = driver.find_element_by_xpath(xpath="/html[@class='focus-outline-hidden']/body/div[@id='root']/div[@class='sc-fsPSfr jnZcev']/div/div[@id='content']/div[1]/div[@class='sc-bMbkRG ekUWsb']/div[@class='sc-whdbJ kKBEZb']/div[@class='sc-TZjqS hzeXst']/div/div[@class='fade-router-enter-done']/div[@class='sc-ieSwJA dkSJHi']/div[@class='sc-cdQEHs eOjyCP']")
        except:
            pass
        else:
        #     print("{}[?] {}{} is CORRECT answer!{}".format(Fore.RESET, Fore.CYAN, selected_answer, Fore.RESET))

            is_exist = False

            #now bot has: a question and a true answer for this question

            #check if currently question is in list_questions 
            for question_obj in list_questions:
                #if yes, check found question has answer or not? 
                if question_obj.question == question_text:
                    #if currenty question doesn't have answer
                    #add selected answer to its answer
                    if question_obj.answer == "None":
                        question_obj.answer = selected_answer
                        
                    is_exist = True
                    break
            
            #if currently answer is not in list_questions
            if (not is_exist) and (selected_answer != "None"):
                #add currently question to list_questions
                list_questions.append(Question(question = question_text))
                #add selected answer to added question's answer
                list_questions[-1].answer = selected_answer

            #go out of main loop
            break

        #check red box appear when choose incorrect answer
        try:
            wrong_answer = driver.find_element_by_xpath(xpath="/html[@class='focus-outline-hidden']/body/div[@id='root']/div[@class='sc-fsPSfr jnZcev']/div/div[@id='content']/div[1]/div[@class='sc-bMbkRG ekUWsb']/div[@class='sc-whdbJ kKBEZb']/div[@class='sc-TZjqS hzeXst']/div/div[@class='fade-router-enter-done']/div[@class='sc-ieSwJA dkSJHi']/div[@class='sc-cdQEHs gdfwZi']")                
        except:
            pass
        else:
            
            # print("{}[?] {}{} is WRONG answer!{}".format(Fore.RESET, Fore.CYAN, selected_answer, Fore.RESET))

            is_exist = False

            #now bot has a question and a wrong answer for this question

            #check if currently question is in list_questions
            for question_obj in list_questions:
                #find which question == currently question
                if question_obj.question == question_text:
                    #if yes
                    for i in range(1,5):
                        #find which answer of found question == selected wrong answer
                        if (question_obj.dict_answer[i]["answer"] == selected_answer):
                            #set its bool value to false
                            question_obj.dict_answer[i]["bool"] = False
                            break

                    is_exist = True
                    break

            #if not exist in list_questions
            if (not is_exist) and (selected_answer != "None"):
                #add new question to list_questions
                list_questions.append(Question(question= question_text))

                #add 4 answers of currently question to added question's 4 answers
                list_questions[-1].dict_answer[1]["answer"] = red_answer_text
                list_questions[-1].dict_answer[2]["answer"] = orange_answer_text
                list_questions[-1].dict_answer[3]["answer"] = green_answer_text
                list_questions[-1].dict_answer[4]["answer"] = blue_answer_text
                
                for i in range(1,5):
                    if ( list_questions[-1].dict_answer[i]["answer"] == selected_answer ):
                        list_questions[-1].dict_answer[i]["bool"] = False
                        break

            #go out of main loop
            break
    
    selected_answer = "None"
    if bool_auto_continue_until_have_enough_money:
        keyboard.send("Enter")
            
