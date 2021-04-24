from time import sleep

def greeting():
    print("Hello!")
    _ = input(">> ")
    
def parting():
    sleep(2)
    print("Okay bye")
    
def catch_up():
    print("How are you?")

    answer = input(">> ")
    if answer == "good":
        print("Glad to hear it!")
        print("I'm doing well too.")
    
    
def conversation():
    talking = True
    responses = [
        "Hmm, that's interesting.",
        "Tell me more!",
        "Wait, what?",
        "Okay, I think I get it.",
        "So what you're saying is, it's complicated?",
    ]
    r = 0  # current response number
    
    print("What's on your mind?")
    while talking:
        answer = input(">> ")
        if answer == "bye":
            talking = False
        else:
            print(responses[r])
            r += 1
            r = r % len(responses)
    
if __name__ == "__main__":

    greeting()
    catch_up()
    conversation()
    parting()


    