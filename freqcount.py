import mysql.connector
import string
import json

from nltk.tokenize import word_tokenize, sent_tokenize
#moving = open("negligence.txt", "r")

with open('negligence.txt') as fin:
    #tokens = word_tokenize(fin.read())
    sentences = sent_tokenize(fin.read())

print(sentences)
#text = "Imran is sitting at home "


# print(nltk.word_tokenize(moving))


# print("Hello")

# connect to db
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="is940123",
    database="mysql"
)


cur = con.cursor()

cur.execute("select id,name from employee")

rows = cur.fetchall()

# for items in rows:
#   print(f" id = {items[0]} name = {items[1]}")

#print("hey this work")

cur.close()
con.close()


my_dict = dict()
for line in moving:
    line = line.strip()
    line = line.lower()
    line = line.translate(line.maketrans("", "", string.punctuation))

    words = line.split(" ")
    for i in words:
        if i in my_dict:
            my_dict[i] = my_dict[i] + 1
        else:
            my_dict[i] = 1


# for word in list(my_dict.keys()):
#  print(word, ":", my_dict[word])
