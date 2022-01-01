#Chris Costa
#6/8/21
#Assigment: A3
b='y'
def encrypt(word, filename, key):
       i=0
       z=""
       while i<len(word):
         cx = word[i]
         if (cx.isalpha()):
             if (cx.isupper()):
                  z+=chr((ord(cx)+key-65)%26+65)
             else:
                  z+=chr((ord(cx)+ key-97)%26+97)
         else:
            z+=cx
         i=i+1
       print(f"The encrypted message is: {z}")
       print(f"A file named ({filename}_enc.txt) was created")
       file = open(filename + "_enc.txt","w")
       file.write(z)
       file.close()
def decrypt(word, filename, key):
        i=0
        z=""
        while i<len(word):
          cx = word[i]
          if (cx.isalpha()):
            if (cx.isupper()):
              z+=chr((ord(cx)-key-65)%26+65)
            else:
              z+=chr((ord(cx)-key-97)%26+97)
          else:
            z+=cx
          i=i+1
        print(f"The decrypted message is: {z}")
        print(f"A file named ({filename}_dec.txt) was created")
        file = open(filename + "_dec.txt","w")
        file.write(z)
        file.close()
print(f"Welcome to the Ceaser Cypher program. \nThis program is designed to encrypt your file by moving each letter of the words in your file up the alphabet by 3 letters. \nThis program can also decrypt files, so long as the key is 3.")
while b=='y' or b=='Y':
  
          f=input("Enter file name(not including the .txt): ")
          file = open(f + ".txt","r")
          x= file.read()
          y=3
          a=input("Would you like to decrypt (d) or encrypt (e): ")
          if a=='E' or a=='e':
            encrypt(x, f, y)
          elif a=='D' or a=='d':
            decrypt(x, f, y)
       
          b=input("Would you like to run the program again? (y) for yes, anything else for no: ")