#!/bin/python3

#def function taking key and value
def encrypt(key, message):

    #variable into empty string times key
    ciphertext = [''] * key

    #for-loop
    for x in range(key):

        #Pointer - navigate through a list w/o modifying
        pointer = x

        #Pointer less-then length of message
        while pointer < len(message):

            #add the value in 'x'
            ciphertext[x] += message[pointer]

            #assigns a new pointer to the key
            pointer += key
          
    #show empty sting with added new cipher text
    return ''.join(ciphertext)

#main function taking in user input
def main():

    message = input('Enter a message: ')
    key = int(input('Select a key: '))
    print(encrypt(key, message))


if __name__ == '__main__':
    main()