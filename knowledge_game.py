cnt = 0
print("Welcome to the game Knowledge.\nYou should answer all the question to win.\nIf your wrong answers are more than three, you lose! ")
print("Good luck")
print("-----------------------------")
user_input = str(input("Type 'yes' to start or 'quit' to quit: "))

while user_input != "quit":

    qst1 = str(input("Which is the name of the capital of Greece?: "))
    qst2 = str(input("Is the color of the sun yellow?  "))
    qst3 = str(input("Which is the common phrase in the programming language you wrote the first time?: "))
    qst4 = str(input("What is the name of the most charismatic prime minister of Greece?: "))
    qst5 = str(input("What did ancient Greece give to the whole world?: "))

    ansr1 = ["athens"]
    ansr2 = ["yes", "correct"]
    ansr3 = ["hello world", "Hello World", "Hello World!"]
    ansr4 = ["kapodistrias"]
    ansr5 = ["democracy", "Democracy"]

    if qst1 in ansr1:
        print("The answer 1 is correct!")
    else:
        print("The answer 1 is wrong!")
        cnt += 1

    if qst2 in ansr2:
        print("The answer 2 is correct!")
    else:
        print("The answer 2 is wrong!")
        cnt += 1

    if qst3 in ansr3:
        print("The answer 3 is correct!")
    else:
        print("The answer 3 is wrong!")
        cnt += 1

    if qst4 in ansr4:
        print("The answer 4 is correct!")
    else:
        print("The answer 4 is wrong!")
        cnt += 1

    if qst5 in ansr5:
        print("The answer 5 is correct!")
    else:
        print("The answer 5 is wrong!")
        cnt += 1

    if cnt == 3:
        print("You lost the game!!!")
        exit()
    else:
        print("You won the game!!")
        exit()

print("Wrong answer(s): ", cnt)








