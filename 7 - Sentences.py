#Tara Moses
#Assignment 7: Strings
#February 1, 2013

#1. Program takes a sentence from the user.
#2. Program converts sentence to upper-case and lower-case.
#3. Program puts proper punctuation on upper-case sentences exclamation points
#   rather than periods)
#4. Program searches for a user-specified word and reports whether it is found.
#5. Program replaces a user-specified word with another user-specified word.
#6. Program takes a user's full name and outputs his or her initials.

sentence=raw_input("Can I have a sentence, please? ")
sentence_lower=sentence.lower()
sentence_upper=sentence.upper()

sentence_upper=sentence_upper.replace("!", "!!!")
sentence_upper=sentence_upper.replace(".", "!")

print("\nPart 1: Sentence in all lower-case: ")
print(sentence_lower)
print("\nPart 2: Sentence in all upper-case: ")
print(sentence_upper)

search=raw_input("\nPart 3: What would you like me to search for? ")
search_lower=search.lower()

if (sentence_lower.find(search_lower)!=-1):
    print("I found it! I found "+search_lower+".")
else:
    print("I couldn't find "+search_lower+". :( I've failed you.")

first=raw_input("\nPart 4: What word do you hate? ")
second=raw_input("Now give me a word you love: ")

new_sentence=sentence.replace(first, second)

print(new_sentence)

full_name=raw_input("\nPart 5: Full name? ")

first_space=full_name.find(" ")
first_name=full_name[:first_space]

second_space=full_name.rfind(" ")
middle_name=full_name[first_space+1:second_space]

last_name=full_name[len(first_name)+len(middle_name)+2:]

initials=first_name[:1]+middle_name[:1]+last_name[:1]

print("Your initials are "+initials.upper()+".")

awesome_middle_name=sentence.replace(".", "")
awesome_middle_name=awesome_middle_name.replace("!", "")

print("\nAlso, on FaceBook, your name would be "+first_name.capitalize()+" \""+awesome_middle_name.title()+"\" "+last_name.capitalize()+".")
