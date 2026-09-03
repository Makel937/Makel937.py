full_name = "Makel Agyeman"
sentence = "If some one tells you a secret, tell everyone so you dont forget. -Tsun Zu, Art of Ragebait"
word_searched = "Tsun"

print(full_name.upper())
print(full_name.lower())
title_name = full_name.title().strip()

print(len(title_name))

if sentence.find(word_searched) == True :
    print("Your word has been found")
else :
    print("Your word has not been found")

print(sentence.count(word_searched))
sentence.replace("If","When")
print(sentence)

print(sentence.isalpha())
print(sentence.isalnum())
print(sentence.startswith("If"))

if sentence == " " :
    print("OI, WRITE NOW!!")
if full_name == " " :
    print("OI, WRITE NOW!!")
if word_searched == " " :
    print("OI, WRITE NOW!!")

if full_name == "Makel Agyeman" :
    print("Your username is RoMak")