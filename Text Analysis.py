################
# Abdirahman Mohamed CSC 236 Assignment 4 9/4/2017
# Helped by: Vincent Michael Davis --> Debugging

import time
def read_file(words_list):
    """Reads a file, replaces punctuations with a blank space"""
    try:
        open_file = open("war_and_peace.txt", 'r')
        contents = open_file.readlines()

        # replace punctuation with a blank space
        punctuation = ['(', ')', '?', ':', ';', ',', '.', '!', '/', '"', "'"]
        for i in punctuation:
            for j in range(len(contents)):
                contents[j] = contents[j].replace(i, "")

        for i in range(len(contents)):
            contents[i].lower()
            words_list.extend((contents[i].lower()).split())
        open_file.close()
    except IOError:
        print("File does not exist! Try again.")
    print(words_list)
    return words_list


def linear_search(words_list, target):
    """Finds a specific element and counts how many times it has occured"""
    count = 0  #setting counter to 0
    for i in range(len(words_list)):
        if words_list[i] == target:  #if the list has the target
            count += 1   #count how many times it has occured
    print("It was mentioned" + str(count) + "times")

def binary_search(words_list, target):
    """Finds a mid value for the list and checks if the target is equal to it.
    If it finds the target equal, it will return the middle else it will process high and low values"""
    low = 0
    high = len(words_list) - 1
    while low <= high:
        mid = (low + high) // 2
        new_target = words_list[mid]  #Finding the middle value of the list
        if target == new_target:
            return mid
        elif target<new_target:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def main():
    """Finding a specific word using three algorithms and checking the time for completing them"""
    words_list = []
    target = input("What is your target word?")

    read_file(words_list)
    start = time.time()
    linear_search(words_list, target)
    stop = time.time()
    print(stop - start)
    begin = time.time()
    new_list = sorted(words_list)
    binary_search(new_list, target)
    end = time.time()
    print(end-begin)
    initiate= time.time()
    binary_search(words_list,target)
    terminate = time.time()
    print(terminate-initiate)



main()
