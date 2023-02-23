#!/usr/bin/python3
import json
import re
import random_responses


#Created by SprayGod777 
#Github profile=https://github.com/SPRAYGOD7


def load_json(file):
    with open(file) as bot_responses:
        print("|======================= 🤖️Welcome to Health query Chatbot System!🤖️ =====================|")
        print("|========================================= Feel Free =====================================|")
        print("|============================================= To ========================================|")
        print("|===================================== Ask your any query ================================|")
        print("")
        print("|========================================= 💡️Tips💡️ ======================================|")
        print("|=====You can ask for disease according to your symptoms==================================|")
        print("|=====By typing= tell me more about my disease you can get more details===================|")
        print("|=====By typing= i want to buy medicine you can buy medicine according to your disease====|")
        print("|========================================= 💡️Tips💡️ ======================================|")
        print("")
        print("|============================================ Chat =======================================|")
        print("🤖️ : How can i help you!")
        return json.load(bot_responses)



response_data = load_json("bot.json")


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []


    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]


        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        if required_score == len(required_words):

            for word in split_message:

                if word in response["user_input"]:
                    response_score += 1


        score_list.append(response_score)
        
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    if input_string == "":
        return "Please type something so we can chat :("
        
        
    if input_string == "bye":
     print("|===================== see you soon bye!👋️=====================|")
     exit()
     
    if input_string == "goodbye":
     print("|===================== see you soon goodbye!👋️ =====================|")
     exit()
      
        
    if best_response != 0:
        return response_data[response_index]["bot_response"]

    return random_responses.random_string()


while True:                         
    user_input = input("You : ")
    print("🤖️ : ", get_response(user_input))
    
    
    
    
    #Created by SprayGod777 
#Github profile=https://github.com/SPRAYGOD7
   
    
