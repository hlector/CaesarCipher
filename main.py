#CASEAR CIPHER
import numpy as np

arr1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's','t','u','v','w','x','y','z']
arr2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's','t','u','v','w','x','y','z']

finalindex = 0
finalindex_out = 0
temp = ''
sum = 0
temp2 = ''
finalindexreverse = 0
finalindexreverseout = 0
keyreverse = 0
negtopos = 0
finalposvalue = 0

while True:
    value = input("Please enter value or q to exit\n")
    key = input("Please enter KEY (1-24) or q to exit\n")

    if value == "q":
        exit()

    elif int(key) > 24:
        print("Max key value is 24")

    elif key.isalpha():
        print("Not a digit! Please try again...")

    elif key.isdigit():
        value.strip()
        temp = ''
        temp2 = ''

        for element in range(0, len(value)):
            #print("Symbols: ", value[element])
            for i in arr1:
                if value[element] == i:
                    #print("Value", value[element]) #value
                    #print("Index", arr1.index(i)) #index
                    finalindex = arr1.index(i) + int(key)
                    #print("Final index is ", finalindex)

                    for k in arr2:
                        if finalindex >= len(arr2):

                            finalindex_out = finalindex - len(arr2)

                            #finalindex_out = finalindex + sum + (int(key) - sum)
                            #print("Finalindex_out", finalindex_out)
                            if finalindex_out == arr2.index(k):
                                temp = temp + k
                                print("Decrypt phrase", temp)

                        elif finalindex == arr2.index(k):
                            temp = temp + k
    print(temp)

    keyreverse = 0
    keyreverse = int(key)
    if keyreverse == int(key):
        for element2 in range(0, len(temp)):
            #print("Test", temp[element2])
            for n in arr1:
                if temp[element2] == n:
                    finalindexreverse = arr1.index(n) - keyreverse
                    #print("Finalindexreverse = ", finalindexreverse)

                    for x in arr2:
                        if finalindexreverse > len(arr2):
                            finalindexreverseout = finalindexreverse - len(arr2)
                            #print("Finalindexreverseout", finalindexreverseout)
                            temp2 = temp2 + x
                        elif finalindexreverse == arr2.index(x):
                            temp2 = temp2 + x
                        elif finalindexreverse < 0:

                            negtopos = abs(finalindexreverse)
                            #print("Negtopos", negtopos)
                            finalposvalue = len(arr2) - negtopos + 1
                            #print("Finalposvalye", finalposvalue)
                            #print("Ura")
                            finalindexreverse = finalposvalue - 1
                            #print("Again finalindexreverse", finalindexreverse)
                            if finalindexreverse < 0:
                                   finalindexreverse = finalposvalue
                                   #print("Finalposvalue", finalindexreverse)
                                   temp2 = temp2 + x

    print("Decrypting....Reverse value is", temp2)











