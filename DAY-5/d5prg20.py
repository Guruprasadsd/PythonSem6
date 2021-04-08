#Using TEST () check whether given string or sentences is pangram or not.
#Pangram means a word or sentences should containing every letter of the alphabet at least once
def TEST(str):
    alph="a b c d e f g h i j k l m n o p q r s t u v w x y z"
    alph1=alph.split()
    alph3=alph.upper().split()
    for i in range(len(alph1)):
        if alph1[i] not in str:
              if alph3[i] not in str:
                return False
    else:
        return True
str = input("Enter the string for checking pangram")
print("The string is pangram?",TEST(str))
