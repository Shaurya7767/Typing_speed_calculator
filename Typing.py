from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try :
            if partest[i] != usertest[i]:
                error = error + 1
        except:
            error = error +1
    return error



def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(userinput) / time_R
    return round(speed)

if __name__ == '__main__':
    while True:
        ck = input(" Ready to do the test : Yes / No :- ")
        if ck == "Yes":
            test = ["A paragraph starts with capital letter and always end with full stop(.)",
                "We have learned ch 1 today and we will learn ch 2 tommrow", "A great years ago, there lived a doctor called dolittle.",
                "The MD showed that he was a proper doctor", "Doctor Dolittle lived in a small town called Puddleby on the march.",
                "He was a tall man and wore a high hat", "Doctor Dolittle lived in a little house at the edge of town."]

            test1 = r.choice(test)
            print("***** Typing speed challenge *****")
            print(test1)
            print()
            print()

            time_1 = time()

            testinput = input(" Enter : ")

            time_2 = time()

            print('Speed : ', speed_time(time_1, time_2, testinput), "w/sec")
            print("Error : ", mistake(test1, testinput))

        elif ck == 'No':
            print("Thank you for visiting our program")
            break

        else:
            print("Wrong Input")