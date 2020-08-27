# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_email_one(email, word):
    censor_word = ""
    for letter in word:
        if letter == " ":
            censor_word += " "
        else:
            censor_word += "*"
    return email.replace(word, censor_word)

#print(email_one)
#print(censor_email_one(email_one,"learning algorithms"))

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms", "her", "herself"]

def censor_email_two(email, array):

    for word in sorted(array, reverse=True):
        #print(word)
        censor_word = ""
        for letter in word:
            if letter == " ":
                censor_word += " "
            else:
                censor_word += "*"
        email = email.replace(word, censor_word)
    return email


#print(email_two)
#print(censor_email_two(email_two,proprietary_terms))

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_email_three(email, negative, propriety):
    censorWord = negative + propriety
    email = censor_email_two(email,censorWord)


    return email


#print(email_three)
#print(censor_email_three(email_three,negative_words,proprietary_terms))

censor_words = negative_words + proprietary_terms
punctuation_marks = [".", ",", "?", ";", "\'", ":", "(", ")", "[", "]", "{", "}", "!", "\"",]
def censor_email_four(email, censor_list):
    text = []
    for i in email.split():
        words = i.split('\n')
        for word in words:
            text.append(word)
    for j in range(len(text)):
        checked_word = text[j].lower()
        for mark in punctuation_marks:
            checked_word = checked_word.strip(mark)
        if checked_word in censor_list:

            word_target = text[j]
            censor_word = ""
            for letter in range(len(word_target)):
                censor_word += "*"
            text[j] = text[j].replace(word_target, censor_word)

            word_before_target = text[j-1]
            censor_word = ""
            for letter in word_before_target:
                censor_word += "*"
            text[j-1] = text[j-1].replace(word_before_target, censor_word)

            word_after_target = text[j+1]
            censor_word = ""
            for letter in word_after_target:
                censor_word += "*"
            text[j+1] = text[j+1].replace(word_after_target, censor_word)

    return " ".join(text)



#print(word_checked_marks)
#print(text)
#print(email_four)
#print(censor_email_four(email_one, censor_words))
#print(censor_email_four(email_two, censor_words))
#print(censor_email_four(email_three, censor_words))
#print(censor_email_four(email_four, censor_words))
