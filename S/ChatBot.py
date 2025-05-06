#chatbot

def remind_name():
    print("Please, remind me your name.")
    name = input()
    print("What a great name you have, {}!".format(name))

def guess_age():
    print("Let me guess your age.")
    print("Enter remainders of dividing your age by 3, 5 and 7.")
    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
    print("Your age is {}; that's a good time to start programming!".format(age))

def count():
    print("Now I will show you that I can count to any number you want.")
    num = int(input())
    for i in range(num + 1):
        print("{}!".format(i))

def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To demonstrate the execution of a program.")
    print("4. To interrupt the execution of a program.")
    answer = 2
    while True:
        guess = int(input())
        if guess == answer:
            break
        print("Please, try again.")
    print("Completed, have a nice day!")

def end():
    print("Congratulations, have a nice day!")

print("Hello! My name is SBot.")
print("I was created in 2021.")
remind_name()
guess_age()
count()
test()
end()