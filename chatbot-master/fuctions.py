

# "ab" in "nf ab ss"
def bad_words_func(split_ans):
    badwords = open("badwords.txt", "r")
    for num in range(452):
        line = badwords.readline()
        line = line.replace("\n","")
        if line.lower() in split_ans:
            return True
    return None


def good_words_func(user_message):
    good_words = ["i love you", "you're cute", "you're an angel", "you're handsome", "you're a good robot"]
    for sentence in good_words:
        if sentence == user_message.lower():
            return True


def names_func(user_message):
    names = open("names.txt", "r")
    for num in range(22727):
        line = names.readline()
        line = line.replace("\n", "")
        if user_message.lower() == line.lower():
            return line
    return None


def scary_words_func(split_ans):
    scarywords = open("scary.txt", "r")
    for line in range(176):
        line = scarywords.readline()
        line = line.replace("\n", "")
        if line.lower() in split_ans:
            return True
    return None


def money(split_ans):
    good_words = ["money", "silver", "coins", "banknotes", "rich"]
    for word in good_words:
        if word in split_ans:
            return True


def dance(split_ans):
    dancewords = open("dance.txt", "r")
    for line in range(34):
        line = dancewords.readline()
        line = line.replace(" \n", "")
        if line.lower() in split_ans:
            return True
    return None


def dog(user_message):
    dog_words = ["dog", "puppy", "dog food", "do you have a dog?"]
    if any(n in user_message.lower() for n in dog_words):
        return True
    else:
        return None


def question(user_message):
    if user_message[-1:] == "?":
        return True
    else:
        return False


def takeoff(user_message):
    goodbye_words = ["bye", "going away", "goodbye", "leaving"]
    if any(n in user_message.lower() for n in goodbye_words):
        return True
    else:
        return None


def heartbroke(user_message):
    goodbye_words = ["i hate you", "i do not like you", "i dont like you", "stupid", "i dont love you"]
    if any(n in user_message.lower() for n in goodbye_words):
        return True
    else:
        return None

