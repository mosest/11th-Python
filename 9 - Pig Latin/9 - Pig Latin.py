#Tara Moses
#Assignment 9: Pig Latin
#February 8, 2013

#1. Program takes a sentence (or file input) and converts it to pig latin.
#2. Program differentiates between words that start with vowels and words that don't.
#3. Program moves punctuation such as "!,.?" and moves it to the end of the word.
#4. Program moves the first few consonants to the end of the word, if there are more than one.
#5. Program capitalizes new words that were capitalized before.
#6. Program will treat the string 'qu' as a consonant if it appears
#   (such as in the word 'squirrel'.)

def starts_with_vowel(word):
    if vowels.find(word[0].lower())==-1:
        return False
    else:
        return True

def there_is_punctuation(word):
    if punctuation_list.find(word[len(word)-1])==-1:
        return False
    else:
        return True

def is_capitalized(word):
    if word[0].upper()==word[0]:
        return True
    else:
        return False

def translate(sentence):
    words=sentence.split(" ")
    translated_sentence=""
    first=""
    last=""
    single_punctuation=""
    
    for word in words:
        if starts_with_vowel(word):
            if there_is_punctuation(word):
                single_punctuation=word[len(word)-1]
                last=word[:len(word)-1]
            else:
                last=word
                single_punctuation=""
            new_word=last+"-way"+single_punctuation
        elif not starts_with_vowel(word):
            for i in range(len(word)):
                if vowels.find(word[i])!=-1:
                    first=word[0:i]
                    last=word[i:]
                    if there_is_punctuation(word):
                        single_punctuation=word[len(word)-1]
                        last=word[i:len(word)-1]
                    else:
                        single_punctuation=""
                    if word[i-1:i+1]=="qu":
                        first=word[0:i+1]
                        last=word[i+1:]
                        if there_is_punctuation(word):
                            single_punctuation=word[len(word)-1]
                            last=word[i+1:len(word)-1]
                        else:
                            single_punctuation=""
                    break
            if is_capitalized(word):
                first=first.lower()
                last=last.capitalize()
            new_word=last+"-"+first+"ay"+single_punctuation
        translated_sentence=translated_sentence+new_word+" "
    return translated_sentence

vowels="aeiouy"
punctuation_list="!.,?"

print("Computer will translate words to pig latin for you.")

while True:
    print("\nWould you like to (1) enter a sentence, or (2) have Computer read from a file?")
    file_or_user=int(raw_input("Enter either a 1 or a 2: "))

    if file_or_user==1:
        print("\nYou chose option 1.")
        user_sentence=raw_input("Enter a sentence: ")
        print("\n")
        print(translate(user_sentence))
        print("\n")
        again=raw_input("Would you like to translate something else? (y/n): ")
        if again.lower()!="y":
            break
    elif file_or_user==2:
        print("\nYou chose option 2.")
        file_name=raw_input("Enter a file name, or enter 'input.txt' to read from an already-created file. \n")
        document=file(file_name)
        for line in document:
            print translate(line.strip())
