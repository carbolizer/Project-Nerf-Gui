import PySimpleGUI as sg
import random

def shuffle_options(options, correct_answer):
    # Create a list of all options including the correct answer
    all_options = options + [correct_answer]

    # Shuffle the options
    random.shuffle(all_options)

    return all_options

def quiz_game(difficulty):
    if difficulty == "Hard":
        questions = ["What color does gold leaf appear if you hold it up to the light?: ",
                     "What is the capital city of Paraguay?: ",
                     "The 'girl in the polka dot dress' was an eye witness in whose assassination?: ",
                     "Atropos, Lachesis, and Clotho are the Three what of Greek mythology?: ",
                     "What were the earliest forms of contraceptive made from?: ",
                     "If you order 'murgh' from the menu at an Indian restaurant, what meat will you get?: ",
                     "Among land animals, what species has the largest eyes?: ",
                     "What comedy became the first film directed by a woman to gross over $100 million at the box office?: ",
                     "So far, which continent has hosted the Olympics the most times?: ",
                     "The surface area of Earth is about how many square miles?: "]
        options = [("Green", "Blue", "Black", "Red"),
                   ("Lima", "Asunción", "La Paz", "Santiago"),
                   ("Lyndon B. Johnson", "George Bush", "Teddy Roosevelt", "John F. Kennedy"),
                   ("The Oracles", "The Fates", "The Sirens", "The Seers"),
                   ("Latex", "Rubber", "Paper", "Crocodile Dung"),
                   ("Beef", "Chicken", "Pork", "Bison"),
                   ("Cheetah", "Wolf", "Elephant", "Ostrich"),
                   ("Big", "Clueless", "Trainwreck", "Mean Girls"),
                   ("Japan", "Europe", "Asia", "Korea"),
                   ("196", "200", "158", "172")]
        answers = ["C", "B", "D", "B", "A", "B", "D", "A", "B", "C"]
    elif difficulty == 'Easy':
        questions = ["Which fictional city is the home of Batman?: ",
                     'How many points are a touchdown worth?: ',
                     'Which country gifted the Statue of Liberty to the US?: ',
                     'How many legs does a spider have?: ',
                     'What is the freezing point of water?(F): ',
                     'What colors are the stars on the American flag?: ',
                     'How many planets are in our solar system?: ',
                     'What type of fish is Nemo?: ',
                     'What is the color of a school bus?: ',
                     'What is a group of lions called?: ',
                     'How many inches are in a yard?: ']
        options = [("A. New York City", "B. Metropolis", "C. Star City", "D. Gotham City"),
                   ("A. 6", "B. 4", "C. 7", "D. 8"),
                   ("A. France", "B. Spain", "C. England", "D. Italy"),
                   ("A. 6", "B. 8", "C. 10", "D. 12"),
                   ("A. 32", "B. 36", "C. 38", "D. 40"),
                   ("A. Red", "B. White", "C. Blue", "D. Yellow"),
                   ("A. 7", "B. 8", "C. 9", "D. 10"),
                   ("A. Goldfish", "B. Clownfish", "C. Angelfish", "D. Regal Blue Tang"),
                   ("A. Yellow", "B. Orange", "C. Red", "D. Green"),
                   ("A. Flock", "B. Pride", "C. Herd", "D. Pack"),
                   ("A. 36", "B. 24", "C. 48", "D. 12")]
        answers = ["D", "C", "A", "B", "A", "C", "B", "B", "A", "B", "C"]
    elif difficulty == "Medium":
        questions = ["How many elements are in the periodic table?: ",
                     "Buckets, Too Tall, and Dazzle are some of the names listed on the roster of what internationally famous basketball team with over 27,000 wins?: ",
                     "Kodiak island is in which US state?: ",
                     "What was the first state?: ",
                     "Famous for being in the freshly murdered grip of Wild Bill Hickok, a dead man's hand in poker is a pair of eights and a pair of what high cards?: ",
                     "About how many taste buds does the average human tongue have?: ",
                     "Which is the highest waterfall in the world?: ",
                     "What is the third sign of the zodiac?: ",
                     "Which name is rapper Sean Combs better known by?: ",
                     "What language has the most words?: "]
        options = [("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Lakers", "B. Celtics", "C. Heat", "D. Warriors"),
                   ("A. Alaska", "B. Hawaii", "C. California", "D. Texas"),
                   ("A. Delaware", "B. Pennsylvania", "C. New York", "D. Maryland"),
                   ("A. Ace", "B. King", "C. Queen", "D. Joker"),
                   ("A. 2,000", "B. 5,000", "C. 8,000", "D. 10,000"),
                   ("A. Niagara Falls", "B. Victoria Falls", "C. Angel Falls", "D. Iguazu Falls"),
                   ("A. Cancer", "B. Leo", "C. Gemini", "D. Virgo"),
                   ("A. Puff Daddy", "B. 50 Cent", "C. Jay-Z", "D. Eminem"),
                   ("A. English", "B. Chinese", "C. Spanish", "D. Arabic")]
        answers = ["C", "A", "A", "B", "C", "B", "A", "B", "A", "D"]
    
    guesses = []
    score = 0
    question_num = 0

    while question_num < len(questions):
        correct_answer = answers[question_num]
        shuffled_options = shuffle_options(list(options[question_num]), correct_answer)

        layout = [
            [sg.Text(f"Question {question_num + 1}: {questions[question_num]}")],
            [sg.Radio(f"{shuffled_options[0]}", 'Options', key=f'-A-{question_num}'),
             sg.Radio(f"{shuffled_options[1]}", 'Options', key=f'-B-{question_num}')],
            [sg.Radio(f"{shuffled_options[2]}", 'Options', key=f'-C-{question_num}'),
             sg.Radio(f"{shuffled_options[3]}", 'Options', key=f'-D-{question_num}')],
            [sg.Button('Submit Answer'), sg.Button('Next Question'), sg.Button('Quit')]
        ]

        window = sg.Window(f"{difficulty} Quiz", layout)

        while True:
            event, values = window.read()

            if event in (None, 'Quit', 'Exit'):
                sg.popup("Quiz Ended", title="Result")
                return

            if event == 'Submit Answer':
                selected_option = values.get(f'-A-{question_num}', False)
                selected_option |= values.get(f'-B-{question_num}', False) << 1
                selected_option |= values.get(f'-C-{question_num}', False) << 2
                selected_option |= values.get(f'-D-{question_num}', False) << 3

                if selected_option > 0:
                    selected_answer = chr(ord('A') + selected_option - 1)
                    if selected_answer == correct_answer:
                        sg.popup("Correct!", title="Result")
                        score += 1
                    else:
                        sg.popup(f"Incorrect! The correct answer is {correct_answer}", title="Result")
                else:
                    sg.popup("Please select an answer!", title="Result")

            if event == 'Next Question':
                window.close()
                question_num += 1
                break

    sg.popup(f"Quiz Ended\nYour Score: {score}/{len(questions)}", title="Result")

# Prompt the user for difficulty before calling the questions() function
difficulty = sg.popup_get_text("What difficulty do you want to play on: Easy, Medium, Hard?", title="Difficulty Selection")
if difficulty in ['Easy', 'Medium', 'Hard']:
    quiz_game(difficulty)
else:
    sg.popup("Invalid difficulty level. Please choose from Easy, Medium, or Hard.", title="Error")
