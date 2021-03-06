
# introducing the game to the user
print("Damilibs Game, ready...")
print("There are different levels in this game \nEasy! Medium!! Hard!!! \nChoose your level")
print("You can choose e or easy or easy for the easy part, m or medium for the medium part and h or hard for the hard"
      "part")

# sentence of the user
first_sentence = "__1__, capital __2__ of Portugal is a __3__ in the euruopean __4__."
second_sentence = "Udacity, is an __1__ __2__ platform based in the __3__ States at Silicon __4__."
third_sentence = "__1__ is a __2__ __3__ where you can find information you need about something.!! \nFacebook __4__ is used for chatting !!"

# answer that we want from the user
first_answer = ["lisbon", "city", "country", "union"]
second_answer = ["online", "learning", "united", "valley"]
third_answer = ["google", "search", "engine", "messenger"]


def get_difficult():
    """ 
    This function takes in the choice of the user and then picks up the quiz choice 
    for instance, if the user chooses the easy, the easy quiz will chosen and so for the other quiz 
    """     
    difficulty = ["easy","medium","hard"]
    while True:
        level = input('Choose a difficulty: (easy / medium / hard)\n').lower()
        if level in difficulty:
            print("You have chosen the \n" + level + " quiz chosen\n")
            if level == difficulty[0]:
                play_game(first_sentence,first_answer)
            elif level == difficulty[1]:
                play_game(second_sentence,second_answer)
            else:
                play_game(third_sentence,third_answer)
            break
        else:
            print("Invalid input :) \nPlease try again")


def play_game(question_level,response_level):
    """ 
    Play the game based on the level chosen. 
    """
    index, counting_score, count,length_of_quiz, score = 0, 0, 0, 4, 9

    while True:
        print(question_level + "\n")
        answer = input("What should be for this : __" + str(index + 1) + "__").lower()
        if answer in response_level:
            if answer in response_level[count]:
                question_level = question_level.replace('__' + str(index + 1) + '__', answer)
                index += 1
                count += 1 
                if index == length_of_quiz:
                    print(question_level + "\n\033[1;32;40m Congratulation!!!")
                    break
        else:
            print("Oops!!! Wrong Guess :) ")
            score -= 1
            if score > counting_score:  
                print('The number of attempt left is : ', score)
            if score == counting_score:
                print('You have no attempt left, Game over!!')
                break
get_difficult()