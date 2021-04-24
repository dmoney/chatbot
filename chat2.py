from time import sleep

# print("Hello, World!")
# sleep(2) #seconds
# print("Okay bye.")
# sleep(1)

# print("Hello, how are you?")
# answer = input(">> ")
# if "good" in answer:
#     print("Glad to hear it")

# greeting
# introduction (your name)
# conversation
#   math
#   talk
#   bye

name = None

def greeting():
    print("Hello!")
    answer = input(">> ")

def introduction():
    print("I'm Computer, what's your name?")
    global name
    name = input(">> ")
    print(f"Hi, {name}, nice to meet you!")

def parting():
    print("Okay, bye!")

def conversation():
    print("What's on your mind?")
    talking = True
    response_number = 0
    responses = [
        "Hmm, that's interesting.",
        "Tell me more!",
        "Wait, what?",
        "Okay, I think I get it.",
        "So what you're saying is, it's complicated?",
    ]
    while talking:
        answer = input(">> ")
        if answer == "bye":
            talking = False
        else:
            print(responses[response_number])
            response_number = response_number + 1
            response_number = response_number % len(responses)



if __name__ == '__main__':
    greeting()
    introduction()
    conversation()
    parting()
