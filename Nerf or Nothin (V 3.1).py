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
        questions = ["What color does gold leaf appear if you hold it up to the light?",
                     "What is the capital city of Paraguay?",
                     "The 'girl in the polka dot dress' was an eye witness in whose assassination?",
                     "Atropos, Lachesis, and Clotho are the Three what of Greek mythology?",
                     "What were the earliest forms of contraceptive made from?",
                     "If you order 'murgh' from the menu at an Indian restaurant, what meat will you get?",
                     "Among land animals, what species has the largest eyes?",
                     "What comedy became the first film directed by a woman to gross over $100 million at the box office?",
                     "So far, which continent has hosted the Olympics the most times?",
                     "The surface area of Earth is about how many square miles?"]
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
        answers = [2, 1, 3, 1, 0, 1, 3, 0, 1, 2]
    elif difficulty == 'Easy':
        questions = ["Which fictional city is the home of Batman?",
                     'How many points are a touchdown worth?',
                     'Which country gifted the Statue of Liberty to the US?',
                     'How many legs does a spider have?',
                     'What is the freezing point of water (F)?',
                     'What colors are the stars on the American flag?',
                     'How many planets are in our solar system?',
                     'What type of fish is Nemo?',
                     'What is the color of a school bus?',
                     'What is a group of lions called?',
                     'How many inches are in a yard?']
        options = [
            ("Gotham City", "Metropolis", "Star City", "Central City"),
            (6, 4, 7, 8),
            ("France", "Spain", "England", "Italy"),
            (6, 8, 10, 12),
            (32, 36, 38, 40),
            ("Red", "White", "Blue", "Yellow"),
            (7, 8, 9, 10),
            ("Goldfish", "Clownfish", "Angelfish", "Regal Blue Tang"),
            ("Yellow", "Orange", "Red", "Green"),
            ("Flock", "Pride", "Herd", "Pack"),
            (36, 24, 48, 12)]
        answers = [0, 2, 0, 1, 2, 2, 1, 1, 0, 1, 2]
    elif difficulty == "Medium":
        questions = ["How many elements are in the periodic table?",
                     "Buckets, Too Tall, and Dazzle are some of the names listed on the roster of what internationally famous basketball team with over 27,000 wins?",
                     "Kodiak island is in which US state?",
                     "What was the first state?",
                     "Famous for being in the freshly murdered grip of Wild Bill Hickok, a dead man's hand in poker is a pair of eights and a pair of what high cards?",
                     "About how many taste buds does the average human tongue have?",
                     "Which is the highest waterfall in the world?",
                     "What is the third sign of the zodiac?",
                     "Which name is rapper Sean Combs better known by?",
                     "What language has the most words?"]
        options = [
            (116, 117, 118, 119),
            ("Lakers", "Celtics", "Heat", "Warriors"),
            ("Alaska", "Hawaii", "California", "Texas"),
            ("Delaware", "Pennsylvania", "New York", "Maryland"),
            ("Ace", "King", "Queen", "Joker"),
            (2000, 5000, 8000, 10000),
            ("Niagara Falls", "Victoria Falls", "Angel Falls", "Iguazu Falls"),
            ("Cancer", "Leo", "Gemini", "Virgo"),
            ("Puff Daddy", "50 Cent", "Jay-Z", "Eminem"),
            ("English", "Chinese", "Spanish", "Arabic")]
        answers = [0, 2, 0, 1, 3, 1, 0, 1, 3, 2]
    
    guesses = []
    score = 0
    question_num = 0

    while question_num < len(questions):
        correct_answer = answers[question_num]
        shuffled_options = shuffle_options(list(options[question_num]), correct_answer)

        layout = [
            [sg.Text(f"Question {question_num + 1}: {questions[question_num]}")],
            [sg.Radio(f"{shuffled_options[0]}", 'Options', key='-A-'),
             sg.Radio(f"{shuffled_options[1]}", 'Options', key='-B-')],
            [sg.Radio(f"{shuffled_options[2]}", 'Options', key='-C-'),
             sg.Radio(f"{shuffled_options[3]}", 'Options', key='-D-')],
            [sg.Button('Submit Answer'), sg.Button('Next Question'), sg.Button('Quit')]
        ]

        window = sg.Window(f"{difficulty} Quiz", layout)

        while True:
            event, values = window.read()

            if event in (None, 'Quit', 'Exit'):
                sg.popup("Quiz Ended", title="Result")
                return

            if event == 'Submit Answer':
                selected_option = shuffled_options.index(correct_answer)

                if values['-A-'] or values['-B-'] or values['-C-'] or values['-D-'] == selected_option:
                    sg.popup("Correct!", title="Result")
                    score += 1
                else:
                    sg.popup(f"Incorrect! The correct answer is {shuffled_options[selected_option]}", title="Result")

            if event == 'Next Question':
                window.close()
                question_num += 1
                break

    sg.popup(f"Quiz Ended\nYour Score: {score}/{len(questions)}", title="Result")

# Create a GUI for selecting the difficulty level
layout = [
    [sg.Button('Easy', size=(10, 1)), sg.Button('Medium', size=(10, 1)), sg.Button('Hard', size=(10, 1))]
]

window = sg.Window('Select Difficulty', layout)

while True:
    event, values = window.read()

    if event in (None, 'Exit'):
        break
    elif event in ('Easy', 'Medium', 'Hard'):
        window.close()
        quiz_game(event)
