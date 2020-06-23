
word1 = input("끝말 잇기를 시작합니다. : ")


if(len(word1) ==3):
    word2 = input()

    while(True):
        if(len(word2) ==3) and (word2[0]==word1[2]):
            print("정답입니다. ")
            pre_word = word2
        else:
            print("오답입니다. ")
            break
else: 
    print("오답입니다. ", word2[0], word1[3])