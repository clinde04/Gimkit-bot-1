import pprint

class Position:
    #top left: x y
    tlX = 0
    tlY = 0
    #bottom right: x y
    brX = 0
    brY = 0

#for bruteforce mode
class Question:
    has_answer = False
    
    question = ""
    answer = ""

    redAnswer = False
    orangeAnswer = False
    greenAnswer = False
    blueAnswer = False



red_answer_position = Position()
orange_answer_position = Position()
green_answer_position = Position()
blue_answer_position = Position()
question_position = Position()

def read_config():
    from configparser import ConfigParser

    #Generating config object
    config_object = ConfigParser()

    from pathlib import Path
    config_file = Path('./config.ini')

    if config_file.is_file():
        print("Config file exist!")
        
        #Read config.ini file
        config_object.read("config.ini")

        #read position from config.ini file
        question_position.tlX = config_object["QUESTION POSITION"]["tlX"]
        question_position.tlY = config_object["QUESTION POSITION"]["tlY"]
        question_position.brX = config_object["QUESTION POSITION"]["brX"]
        question_position.brY = config_object["QUESTION POSITION"]["brY"]

        red_answer_position.tlX = config_object["RED ANSWER POSITION"]["tlX"]
        red_answer_position.tlY = config_object["RED ANSWER POSITION"]["tlY"]
        red_answer_position.brX = config_object["RED ANSWER POSITION"]["brX"]
        red_answer_position.brY = config_object["RED ANSWER POSITION"]["brY"]

        orange_answer_position.tlX = config_object["ORANGE ANSWER POSITION"]["tlX"]
        orange_answer_position.tlY = config_object["ORANGE ANSWER POSITION"]["tlY"]
        orange_answer_position.brX = config_object["ORANGE ANSWER POSITION"]["brX"]
        orange_answer_position.brY = config_object["ORANGE ANSWER POSITION"]["brY"]
        
        green_answer_position.tlX = config_object["GREEN ANSWER POSITION"]["tlX"]
        green_answer_position.tlY = config_object["GREEN ANSWER POSITION"]["tlY"]
        green_answer_position.brX = config_object["GREEN ANSWER POSITION"]["brX"]
        green_answer_position.brY = config_object["GREEN ANSWER POSITION"]["brY"]

        blue_answer_position.tlX = config_object["BLUE ANSWER POSITION"]["tlX"]
        blue_answer_position.tlY = config_object["BLUE ANSWER POSITION"]["tlY"]
        blue_answer_position.brX = config_object["BLUE ANSWER POSITION"]["brX"]
        blue_answer_position.brY = config_object["BLUE ANSWER POSITION"]["brY"]

        #review position:  top left X Y - bottom right X Y
        print(f"""Question Position: {question_position.tlX} {question_position.tlY} - {question_position.brX} {question_position.brY}
Red answer position: {red_answer_position.tlX} {red_answer_position.tlY} - {red_answer_position.brX} {red_answer_position.brY}
Orange answer position: {orange_answer_position.tlX} {orange_answer_position.tlY} - {orange_answer_position.brX} {orange_answer_position.brY}
Green answer position: {green_answer_position.tlX} {green_answer_position.tlY} - {green_answer_position.brX} {green_answer_position.brY}
Blue answer position: {blue_answer_position.tlX} {blue_answer_position.tlY} - {blue_answer_position.brX} {blue_answer_position.brY}
""")
        return True
        
    else:
        print("""Config file doesn't exist!\nGenerating config file....\nPlease edit config!""")

        config_object["QUESTION POSITION"] = {
            "tlX" : "0",
            "tlY" : "0",
            "brX" : "0",
            "brY" : "0"
        }

        config_object["RED ANSWER POSITION"] = {
            "tlX" : "0",
            "tlY" : "0",
            "brX" : "0",
            "brY" : "0"
        }

        config_object["ORANGE ANSWER POSITION"] = {
            "tlX" : "0",
            "tlY" : "0",
            "brX" : "0",
            "brY" : "0"
        }

        config_object["GREEN ANSWER POSITION"] = {
            "tlX" : "0",
            "tlY" : "0",
            "brX" : "0",
            "brY" : "0"
        }

        config_object["BLUE ANSWER POSITION"] = {
            "tlX" : "0",
            "tlY" : "0",
            "brX" : "0",
            "brY" : "0"
        }

        #Write the above sections to config.ini file
        with open('config.ini', 'w') as conf:
            config_object.write(conf)

        return False





def study_mode():
    print("""Starting Study mode!
""")

    pass

def brute_force_mode():
    print("Starting Bruteforce mode!")
    
    pass


def main():
    print("Reading config file...")
    if not read_config():
        return

    choice = input("""Choose bot mode:
    1 -> Study mode
    2 -> Bruteforce mode
    """)

    if choice == 1:
        study_mode()
    elif choice == 2:
        brute_force_mode()
    else:
        print("Invalid choice!")


if __name__== "__main__":
	main()