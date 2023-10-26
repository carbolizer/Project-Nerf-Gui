import PySimpleGUI as sg
import random
import RPi.GPIO as GPIO

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
button_pins = [17, 18, 22, 23]  # Define the GPIO pins for buttons (adjust pin numbers as needed)

# Set up GPIO pins as inputs with pull-up resistors
for pin in button_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def shuffle_options(options, correct_answer):
    all_options = [option for option in options if option != correct_answer]
    all_options.append(correct_answer)
    random.shuffle(all_options)
    return all_options

def create_question_layout(question, options):
    layout = [
        [sg.Text(f"Question: {question}")],
    ]

    for option in options:
        layout.append([sg.Radio(option, "OPTIONS", key=option)])

    layout.append([sg.Button('Submit Answer'), sg.Button('Next Question'), sg.Button('Quit')])
    return layout

def main():
    sg.theme('Black')

    difficulties = ['Easy', 'Medium', 'Hard']

    while True:
        layout = [[sg.Button(difficulty, size=(10, 1)) for difficulty in difficulties] + [sg.Button('Exit')]]
        window = sg.Window('Select Difficulty', layout)

        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event in difficulties:
            window.close()
            quiz_game(event)

def quiz_game(difficulty):
    questions, answers, options = get_quiz_data(difficulty)
    score = 0

    for question_num, (question, correct_answer, option_list) in enumerate(zip(questions, answers, options)):
        shuffled_options = shuffle_options(option_list, correct_answer)
        layout = create_question_layout(question, shuffled_options)
        window = sg.Window(f"{difficulty} Quiz", layout)

        while True:
            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, 'Quit'):
                sg.popup("Quiz Ended", title="Result")
                return

            if event == 'Submit Answer':
                selected_option = [option for option in shuffled_options if values[option]][0]

                if selected_option == correct_answer:
                    sg.popup("Correct!", title="Result")
                    score += 1
                else:
                    sg.popup(f"Incorrect! The correct answer is {correct_answer}", title="Result")

            if event == 'Next Question':
                window.close()
                break

    sg.popup(f"Quiz Ended\nYour Score: {score}/{len(questions)}", title="Result")

def get_quiz_data(difficulty):
    quiz_data = {
        "Hard": {
            "questions": ["What color does gold leaf appear if you hold it up to the light?",
                          "What is the capital city of Paraguay?",
                          "The 'girl in the polka dot dress' was an eye witness in whose assassination?",
                          "Atropos, Lachesis, and Clotho are the Three what of Greek mythology?",
                          "What were the earliest forms of contraceptive made from?",
                          "If you order 'murgh' from the menu at an Indian restaurant, what meat will you get?",
                          "Among land animals, what species has the largest eyes?",
                          "What comedy became the first film directed by a woman to gross over $100 million at the box office?",
                          "So far, which continent has hosted the Olympics the most times?",
                          "The surface area of Earth is about how many square miles?"],
            "options": [["Green", "Blue", "Black", "Red"],
                        ["Lima", "Asunción", "La Paz", "Santiago"],
                        ["Lyndon B. Johnson", "George Bush", "Teddy Roosevelt", "John F. Kennedy"],
                        ["The Oracles", "The Fates", "The Sirens", "The Seers"],
                        ["Latex", "Rubber", "Paper", "Crocodile Dung"],
                        ["Beef", "Chicken", "Pork", "Bison"],
                        ["Cheetah", "Wolf", "Elephant", "Ostrich"],
                        ["Big", "Clueless", "Trainwreck", "Mean Girls"],
                        ["Japan", "Europe", "Asia", "Korea"],
                        ["196", "200", "158", "172"]],
            "answers": ["Black", "Asunción", "John F. Kennedy", "The Fates", "Latex", "Chicken", "Ostrich", "Mean Girls", "Europe", "196"]
        },
        "Easy": {
            "questions": ["Which fictional city is the home of Batman?",
                          "How many points are a touchdown worth?",
                          "Which country gifted the Statue of Liberty to the US?",
                          "How many legs does a spider have?",
                          "What is the freezing point of water?(F)",
                          "What colors are the stars on the American flag?",
                          "How many planets are in our solar system?",
                          "What type of fish is Nemo?",
                          "What is the color of a school bus?",
                          "What is a group of lions called?",
                          "How many inches are in a yard?"],
            "options": [["Gotham City", "Metropolis", "Star City", "New York City"],
                        ["6", "4", "7", "8"],
                        ["France", "Spain", "England", "Italy"],
                        ["6", "8", "10", "12"],
                        ["32", "36", "38", "40"],
                        ["Red", "White", "Blue", "Yellow"],
                        ["7", "8", "9", "10"],
                        ["Goldfish", "Clownfish", "Angelfish", "Regal Blue Tang"],
                        ["Yellow", "Orange", "Red", "Green"],
                        ["Flock", "Pride", "Herd", "Pack"],
                        ["36", "24", "48", "12"]],
            "answers": ["Gotham City", "6", "France", "8", "32", "White", "8", "Clownfish", "Yellow", "Pride", "36"]
        },
        "Medium": {
            "questions": ["How many elements are in the periodic table?",
                          "Buckets, Too Tall, and Dazzle are some of the names listed on the roster of what internationally famous basketball team with over 27,000 wins?",
                          "Kodiak island is in which US state?",
                          "What was the first state?",
                          "Famous for being in the freshly murdered grip of Wild Bill Hickok, a dead man's hand in poker is a pair of eights and a pair of what high cards?",
                          "About how many taste buds does the average human tongue have?",
                          "Which is the highest waterfall in the world?",
                          "What is the third sign of the zodiac?",
                          "Which name is rapper Sean Combs better known by?",
                          "What language has the most words?"],
            "options": [["116", "117", "118", "119"],
                        ["Lakers", "Celtics", "Heat", "Warriors"],
                        ["Alaska", "Hawaii", "California", "Texas"],
                        ["Delaware", "Pennsylvania", "New York", "Maryland"],
                        ["Ace", "King", "Queen", "Joker"],
                        ["2,000", "5,000", "8,000", "10,000"],
                        ["Niagara Falls", "Victoria Falls", "Angel Falls", "Iguazu Falls"],
                        ["Cancer", "Leo", "Gemini", "Virgo"],
                        ["Puff Daddy", "50 Cent", "Jay-Z", "Eminem"],
                        ["English", "Chinese", "Spanish", "Arabic"]],
            "answers": ["118", "Lakers", "Alaska", "Delaware", "Ace", "10,000", "Angel Falls", "Gemini", "Puff Daddy", "English"]
        }
    }

    if difficulty in quiz_data:
        return quiz_data[difficulty]["questions"], quiz_data[difficulty]["answers"], quiz_data[difficulty]["options"]
    else:
        return [], [], []

if __name__ == '__main__':
    main()
