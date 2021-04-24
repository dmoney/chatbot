from time import sleep
from collections import namedtuple

fact = namedtuple('fact', ['subject', 'verb', 'object'])

#modifier
mod = namedtuple('mod', ['subject', 'preposition', 'object'])

"""

A statement is parsed into a fact, consisting of a
subject, verb, and object.
These can be an individual word or a "modifier",
which has a subject, preposition, and object.

e.g., "The quick brown fox jumped over the lazy dog."


_ = fact(
        mod('fox', None, ['the', 'quick', 'brown']),
        mod('jumped', 'over', mod('dog', None, ['the', 'lazy'])),
        None)

Existing parser may not be capable of this level of parsing.


knowledge is represented as a dictionary. A key is either a
string or a modifier.  A value is a set of facts about that
subject.

knowledge = {}
knowledge['dogs'] = set()
knowledge['dogs'].add(fact(...))
"""

PUNCTUATION = ('!', '?', '.', ',')

def tokenize_word(text):
    """Break a word ending in punctuation into separate
    tokens for the word and the punctuation."""
    if len(text) <= 1:
        return [text]
    elif text[-1] in PUNCTUATION:
        return [text[:-1], text[-1:]] # slices: listname[start:stop:step]
    else:
        return [text]

def tokenize(text):
    """Break text into tokens (words or punctuation)."""
    for word in text.split():
        for token in tokenize_word(word):
            yield token

def sentencify(tokens):
    """Separate the stream of tokens into sentences.
    Breaks an iterable of tokens into an iterable of lists of tokens."""
    sentence = []
    for token in tokens:
        sentence.append(token)
        if token in PUNCTUATION:
            yield sentence
            sentence = []
    if sentence:
        yield sentence

# words at start of sentence indicating a question
question_words = ['is', 'does', 'what', 'am', 'are']

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

def good_conversation():
    knowledge = {}
    talking = True
    print("So, tell me or ask me something.")
    while talking:
        answer = input(">> ")
        if answer == "bye":
            talking = False
        else:
            answer = answer.lower()
            sentences = list(sentencify(tokenize(answer)))
            for sentence in sentences:
                if not sentence:
                    continue
                if sentence[0] == 'is':  # it's a question
                    if len(sentence) < 3:
                        # TODO, cut off punctuation
                        print("Sorry, I don't understand.")
                        continue
                    else:
                        verb = 'is'
                        subject = sentence[1]
                        object = tuple(sentence[2:])
                        result = knowledge.get(subject, None)
                        if result is None:
                            print("I don't know anything about " + subject + '.')
                            continue
                        if fact(subject, verb, object) in result:
                            print("Yes.")
                        else:
                            print("No.")
                elif sentence[1] == 'is':
                    if len(sentence) < 3:
                        # TODO, cut off punctuation
                        print("Sorry, I don't understand.")
                        continue
                    else:
                        subject = sentence[0]
                        verb = 'is'
                        object = tuple(sentence[2:])
                        new_fact = fact(subject, verb, object)
                        knowledge_set = knowledge.get(subject, None)
                        if knowledge_set is None:
                            knowledge_set = set()
                            knowledge[subject] = knowledge_set
                        if new_fact not in knowledge_set:
                            print("Huh, I didn't know that.")
                        else:
                            print("I know.")
                        knowledge_set.add(new_fact)
                else:
                    print("Hm, that's interesting.")





if __name__ == "__main__":

    greeting()
    #catch_up()
    #conversation()
    good_conversation()
    parting()
