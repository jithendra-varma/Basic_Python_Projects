import string
import random
from itertools import combinations_with_replacement

def meaningful_password(k,wc):
    words = open('words.txt','r')
    dct = {}
    for word in words:
        word = word[:-1]
        if len(word) not in dct:
            dct[len(word)] = [word]
        else:
            dct[len(word)].append(word)
    lt = list(dct.keys())
    lt.sort()
    cwr = list(combinations_with_replacement(lt,wc))
    final = []
    for i in cwr:
        su = 0
        for j in i:
            su += j
        if su == k:
            final.append(i)
    key_value = random.sample(final,1)
    answ_list = []
    for x in key_value:
        for ke in x:
            answ_list.extend(random.sample(dct[ke],1))
    pass_rw = open("passwords.txt","a+")
    while True:
        random.shuffle(answ_list)
        pass_string = "".join(answ_list)
        if pass_string not in pass_rw:
            pass_rw.write(pass_string)
            break
    print(pass_string)

def random_password_with_rules(k):
    low = string.ascii_lowercase
    upp = string.ascii_uppercase
    numb = string.digits
    punc = string.punctuation
    mt = []
    mt.extend(random.sample(upp,1))
    mt.extend(random.sample(numb,1))
    mt.extend(random.sample(punc,1))
    mt.extend(random.sample(low,k-3))
    pass_rw = open("passwords.txt","a+")
    while True:
        random.shuffle(mt)
        pass_string = "".join(mt)+"\n"
        if pass_string not in pass_rw:
            pass_rw.write(pass_string)
            break
    print(pass_string)

def random_password(k):
    low = string.ascii_lowercase
    upp = string.ascii_uppercase
    numb = string.digits
    punc = string.punctuation
    charac_list = []
    charac_list.extend(low)
    charac_list.extend(upp)
    charac_list.extend(numb)
    charac_list.extend(punc)
    pass_rw = open("passwords.txt","a+")
    while True: 
        pass_string = "".join(random.sample(charac_list,k))+"\n"
        if pass_string not in pass_rw:
            pass_rw.write(pass_string)
            break
    print(pass_string)

print("Enter '0' for random_password (or) '1' for random_passoword_with_rules (or) '2' for meaningful_password")
pass_cond = int(input("Enter your choice : "))
if pass_cond == 0:
    pass_len = int(input("Enter the password length : "))
    random_password(pass_len)
elif pass_cond == 1:
    pass_len = int(input("Enter the password length in the range > 4 : "))
    random_password_with_rules(pass_len)
elif pass_cond == 2:
    pass_len = int(input("Enter the length of the password in the range 1 to 31 : "))
    pass_word_count = int(input("Enter the no of words : "))
    meaningful_password(pass_len,pass_word_count)
