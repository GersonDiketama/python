

def sentence_maker(phrase):
    interrogatives = ("how", "what", "why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        # This will check if the string starts with "any interrogatives" if yes then it will ran the line below:
        # The line below is a string format which mean that the entered string will go wherever the curly brackets are located. example: if user enters: How are you
        # the string will return as => How are you? or {How are you}?
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


results = []

while True:
    user_input = input("Say something ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))
