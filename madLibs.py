import random

print("Welcome to Hudgens friendly MadLibs game!!!")
print("In this you can select your path, you will be prompted to enter what story you want to do!")
print("Select and have fun!!!!")

choice = input("What story would you like: 'Vaction', 'Fortune Teller', or 'The Invitation: ")

if choice == 'Vacation' or 'vacation' or 'VACATION':
    print("You have chosen Vacation")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter an adjective:")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter a noun:")
    pluralNoun1 = input("Enter a plural noun: ")
    game = input("Enter a fun game: ")
    pluralnoun2 = input("Enter a plural noun: ")
    verbEndingInIng1 = input("Enter a verb ending in ing: ")
    verbEndingInIng2 = input("Enter a verb ending in ing: ")
    pluralNoun3 = input("Enter a plural noun: ")
    verbEndingInIng3 = input("Enter a verb ending in ing: ")
    noun3 = input("Enter a noun: ")
    plant = input("Enter a plant: ")
    partOfBody = input("Enter a part of the body: ")
    location = input("Enter a location: ")
    verbEndingInIng4 = input("Enter a verb ending in ing: ")
    adjective3 = input("Enter an adjective:")
    number = input("Enter a number: ")
    pluralNoun4 = input("Enter a plural noun: ")
    
    vacation = (
        "A vacation is when you take a trip to some " + adjective1 + 
        "place with your " + adjective2 + " family. Usually you go to some place " +
        " that is near a/an" + noun1 +" or up on a/an " + noun2 + ". A good vacation" +
        " place is one where you can ride " +pluralNoun1+ " or play " + game + 
        " or go hunting for " + pluralnoun2 + ". I like to spend my time " + verbEndingInIng1 +
        " or " + verbEndingInIng2 + ". When parents go on a vacation, they spend their time " +
        "eating three " + pluralNoun3 + " a day, and fathers play golf, and mothers " + 
        " sit around " + verbEndingInIng3 + ". Last summer, my little brother fell in a/an " +
        noun3 + " and got poison " +plant+ " all over his " +partOfBody+ ". My family " +
        "is going to go (the) " +location+ ", and I will practice " +verbEndingInIng4+
        ". Parents need vacations more than kids because parents are always very " +
        adjective3 + " and because they have to work " + str(number) + " hours every day " +
        "hours every day all year making enough " + pluralNoun4+ " to pay for the vacation."

    )
    print(vacation)
    print("I hope you enjoyed your story!")
elif choice == 'Fortune Teller' or 'fortune teller' or 'fortuneteller':
    print("The Python Fortune Teller will tell you what want to know or what your should think about!")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter an adjective: ")
    numberGreaterThanOne = input("Enter a number greater")
    pluralnoun1 = input("Enter a plural noun: ")
    partOfBody = input("Enter a part of the body: ")
    adjective3 = input("Enter an adjective: ")
    adjective4 = input("Enter an adjective: ")
    singularNoun = input("Enter a singular noun: ")
    articleOfClothing = input("Enter an article of Clothing: ")
    personInTheRoom = input("Enter someone's name that is close to you: ")

    answer1 = 'Signs point to a very ' + adjective1 + ' says.'
    answer2 = 'The Skies are ' + adjective2 + ' the future is uncertain.'
    answer3 = 'I see' + str(numberGreaterThanOne) + 'big ' + pluralNoun1 + 'in your future.'
    answer4 = 'What does your ' + partOfBody + " tell you?"
    answer5 = 'Signs point to a very ' + adjective3 + ' no.'
    answer6 = 'Picture a/an ' + adjective4+" " + singularNoun + ". That is your answer"
    answer7 = 'You will find the answer in your ' + articleOfClothing
    answer8 = 'Dont believe anything ' + personInTheRoom + 'says.'

    answers = [answer1, answer2, answer3, answer4, answer5,answer6, answer7, answer8]

    print(random.choice(answers))
else:
    print('You have selected The Invitation!')
    name = input('Enter a name: ')
    theme = input('Enter a theme: ')
    location = input('Enter a place: ')
    dayOfTheWeek = input('Enter a day of the week: ')
    time =input('Enter a time: ')
    verb = input('Enter a verb: ')
    animal = input("Enter an animal: ")
    bodyPart = input('Enter a body part: ')
    contactInformation = input('Enter contact information: ')

    invitation = (
        name + " is have a " +theme+ " on " + dayOfTheWeek + ". Please make sure " +
        " to show up at " + str(time) + ", or else you will be required to " + verb + " a/an " +
        animal + " with your " + bodyPart + " RVSP at " + contactInformation +"."
        )

    print(invitation)

print('Thank you for playing!')


