import random

def knuffle_shuffle(array):
    for i in range(len(array)):
        rand = random.randint(0, i)
        array[rand], array[i] = array[i], array[rand]

arr = [1,2,3,4,5,6,7,8,9,10]
knuffle_shuffle(arr)
print(arr)