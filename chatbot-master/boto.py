from bottle import route, run, template, static_file, request
from fuctions import *
import json
import re
from random import randrange
import requests
weather_on = False


@route('/', method='GET')
def index():
    return template("chatbot.html")


def weather(user_message):
    weather_words = ["weather"]
    if any(n in user_message.lower() for n in weather_words):
        return True


def check_weather(user_message):
    global weather_on
    weather_on = False
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?q={}&APPID=85560421f770605c1d50a905ec19876c".format(user_message))
    data = r.json()
    sky = data.get("weather")[0].get("main")
    temperature = data.get("main").get("temp")
    return {"animation": "excited", "msg": "In {} there is {} and the temperature is {:0.2f}ºC".format(user_message,sky,temperature-273)}


def check_for_words(user_message_first):
    global weather_on
    user_message = re.sub(r'[^a-zA-Z\s]', "", user_message_first)
    split_ans_first = user_message_first.lower().split()
    split_ans = []
    for index in split_ans_first:
        split_ans.append(re.sub(r'[^a-zA-Z]', "", index))
    if weather_on:
        weather_is = check_weather(user_message)
        return weather_is
    name = names_func(user_message)
    if name:
        return {"animation": "excited", "msg": f"Hay {name}!! nice to meet you!!"}
    if bad_words_func(split_ans):
        return {"animation": "no", "msg": "Stop curse please!!!"}
    elif good_words_func(user_message):
        return {"animation": "inlove", "msg": "Thank you for saying that! I feel the same way..."}
    elif scary_words_func(split_ans):
        return {"animation": "afraid", "msg": "Can I be honest with you? You used a very scary language ..."}
    elif money(split_ans):
        return {"animation": "money", "msg": "Show me the money!!!"}
    elif dance(split_ans):
        return {"animation": "dancing", "msg": "Shut up and dance with me!!"}
    elif dog(user_message):
        return {"animation": "dog", "msg": "Meet my dog Melnikov!"}
    elif takeoff(user_message):
        return {"animation": "takeoff", "msg": "Ok I'm back to my planet.. Bye bye"}
    elif heartbroke(user_message):
        if randrange(2):
            return {"animation": "heartbroke", "msg": "why would you say that to me?"}
        else:
            return {"animation": "crying", "msg": "you insulted me!!"}
    elif joke_func(user_message):
        chosen_joke = joke_func(user_message)
        return {"animation": "laughing", "msg": chosen_joke}
    elif weather(user_message):
        weather_on = True
        return {"animation": "confused","msg": "Which city in the world would you like to check the weather?"}
    elif question(user_message_first):
        return {"animation": "excited", "msg": "I don't know how to answer this question but I am very excited!!"}
    else:
        if randrange(2):
            return {"animation": "confused", "msg":"I'm not sure I understood .. If you want me to tell you a joke just ask"}
        else:
            return {"animation": "ok", "msg": "I'm not sure I understood.. but whatever..'"}


def joke_func(user_message):
    joke_words = ["joke", "laugh", "funny"]
    r = requests.get("http://api.icndb.com/jokes/random")

    if any(n in user_message.lower() for n in joke_words):
        data = r.json()
        return data.get("value").get("joke")
    else:
        return None


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    ans_after_words_check = check_for_words(user_message)
    return ans_after_words_check


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000, reloader=True)

if __name__ == '__main__':
    main()



