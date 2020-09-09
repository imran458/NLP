import string
print("hello world")

moving = open("movenyc.txt","r")
#print(moving.read())

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


for word in list(my_dict.keys()):
    print(word, ":", my_dict[word])
