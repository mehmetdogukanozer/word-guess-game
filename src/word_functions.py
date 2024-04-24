import random

def createSecret(word:str ,hash_count:int)->str:
    word_len = len(word)
    
    latter_list = []

    for latter in word:
        latter_list.append(latter)

    for i in range(hash_count):
        random_index = random.randint(0,word_len-1)
        latter_list[random_index] = "*"

    secret = ""

    for item in latter_list:
        secret += item
    return secret