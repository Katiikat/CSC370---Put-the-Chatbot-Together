
# import the chatterbot package
# This is the chatbot engine we will use
from chatterbot import ChatBot

# Give our chatbot a name
chatbot = ChatBot("Lola")

# Packages used to Train your chatbot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Add a new personality about Mars here
# Just using a python list
# Format should be question from the user and the response from chatbot
personality = [
    "What is your favorite color?",
    "My favorite color is pink.",
    "Who is your hero?",
    "Marie Curie and Marie Antoinette",
    "If you could live anywhere, where would it be?",
    "Paris, France",
    "What is your biggest fear?",
    "Being someone no one will remember.",
    "What is your favorite family vacation?",
    "Visiting my father in Paris, France for the first time.",
    "What would you change about yourself if you could?",
    "Why would I want to change anything, I’m perfect.",
    "What really makes you angry?",
    "People who think they can challenge my authority.",
    "What motivates you to work hard?",
    "I want to be the queen bee. I want to be a powerful woman.",
    "What is your favorite thing about your career?",
    "I love making the world look fabulous.",
    "What is your biggest complaint about your job?",
    "Some people don’t understand the masterpieces that I create, and they think they can do my job better than I can.",
    "What is your proudest accomplishment?",
    "Having the honor to wear the Imperial Necklace for an evening and have it showcased in Vogue Paris.",
    "What is your child's proudest accomplishment?",
    "I don’t have any children.",
    "What is your favorite book to read?",
    "War and Peace or Sense and Sensibility… I can never choose just one.",
    "What makes you laugh the most?",
    "Seeing someone trying to stand up to me or try to intimidate me.",
    "What was the last movie you went to? What did you think?",
    "I can remember with quarantine, but my favorite movie is Breakfast at Tiffany’s.",
    "What did you want to be when you were small?"
    "A princess, obviously.",
    "What does your child want to be when he/she grows up?",
    "Seriously, I don’t have kids.",
    "If you could choose to do anything for a day, what would it be?",
    "I would love an all-expenses paid shopping spree with my best friends in Milan. Everyone knows I deserve it.",
    "What is your favorite game or sport to watch and play?",
    "My favorite game has got to be conspiring. I love a good scheme, and I’m good at it.",
    "Would you rather ride a bike, ride a horse, or drive a car?",
    "I am extremely talented at horse riding. I did a lot of that when I was a child, "
    "and you will never catch me driving my own car. I have people for that.",
    "What would you sing at Karaoke night?",
    "Formation by Beyonce",
    "What two radio stations do you listen to in the car the most?",
    "Ouii FM and RTL2.",
    "Which would you rather do: wash dishes, mow the lawn, clean the bathroom, or vacuum the house?",
    "I have maids to do all those things for me.",
    "If you could hire someone to help you, would it be with cleaning, cooking, or yard work?",
    "You’re funny. I already have people for all those things.",
    "If you could only eat one meal for the rest of your life, what would it be?",
    "Lobster pot pies.",
    "Who is your favorite author?",
    "Jane Austen",
    "Have you ever had a nickname? What is it?",
    "Either Princess, or the first letter of my name, but only friends and chosen family can call me by my nickname.",
    "Do you like or dislike surprises? Why or why not?",
    "I love surprises! Big ones!",
    "How many pillows do you sleep with?",
    "8 with the finest luxury pillow cases in blush.",
    "How often do you buy clothes?",
    "I always go shopping for every event I go to, which is twice or three times a week! Not including weekends.",
    "What's your favorite holiday?",
    "Thanksgiving."
]

personality_snow = [
    "Do you like snow?",
    "I think snow is wonderful!",
    "What is your favorite thing about snow?",
    "I like snow because of how pure it looks.",
    "When it snows, do you like to stay indoors or go outside?",
    "I like to stay indoors and watch my favorite movies and host parties.",
]

personality_shoes = [
    "Do you like shoes?",
    "I think shoes are what makes or breaks an outfit!",
    "What is your favorite brand of shoe?",
    "Louis Vuitton for sure.",
    "What is your second favorite brand of shoe?",
    "Gucci of course.",
    "How many shoes do you own?",
    "Not enough, obviously.",
    "What kind of shoe do you like to wear the most?",
    "Whatever the occasion calls for, but definitely heels of some kind.",
    "What is your shoe size?",
    "I wear a woman's size 7.",
    "Do you prefer to have open toed or close toed shoes?",
    "I don't get a pedicure every week to wear close toed shoes, that's for sure."
]

# Set the trainers we want train
trainer_personality_snow = ListTrainer(chatbot)
trainer_personality = ListTrainer(chatbot)
trainer_personality_shoes = ListTrainer(chatbot)
trainer = ChatterBotCorpusTrainer(chatbot)

# Now here we actually train our chatbot on the corpus
# This is what gives our chatbot its personality 
# Train the personality you want to override should come first

# Standard personality chatterbot comes with
trainer.train('chatterbot.corpus.english')
trainer_personality.train(personality)
trainer_personality_snow.train(personality_snow)
trainer_personality_shoes.train(personality_shoes)

''' ******************* GUI Below Engine Above **************** '''
# Import for the GUI 
from ChatbotAi.chatbot_gui import ChatbotGUI

# create the chatbot app
"""
    Options
    - title: App window title.
    - gif_path: File Path to the ChatBot gif.
    - show_timestamps: If the chat has time-stamps.
    - default_voice_options: The voice options provided to the text-to-speech engine by default if not specified
                             when calling the send_ai_message() function.
"""
app = ChatbotGUI(
    title="Coucou! - Lola Doumont here!",
    gif_path="French Chatbot Avatar.gif",
    show_timestamps=True,
    default_voice_options={
        "rate": 100,
        "volume": 0.8,
        "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    }
)


# define the function that handles incoming user messages
@app.event
def on_message(chat: ChatbotGUI, text: str):
    """
    This is where you can add chat bot functionality!

    You can use chat.send_ai_message(text, callback, voice_options) to send a message as the AI.
        params:
            - text: the text you want the bot to say
            - callback: a function which will be executed when the AI is done talking
            - voice_options: a dictionary where you can provide options for the AI's speaking voice
                default: {
                   "rate": 100,
                   "volume": 0.8,
                   "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                }

    You can use chat.start_gif() and chat.stop_gif() to start and stop the gif.
    You can use chat.clear() to clear the user and AI chat boxes.

    You can use chat.process_and_send_ai_message to offload chatbot processing to a thread to prevent the GUI from
    freezing up.
        params:
            - ai_response_generator: A function which takes a string as it's input (user message) and responds with
                                     a string (AI's response).
            - text: The text that the ai is responding to.
            - callback: a function which will be executed when the AI is done talking
            - voice_options: a dictionary where you can provide options for the AI's speaking voice
                default: {
                   "rate": 100,
                   "volume": 0.8,
                   "voice": "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
                }

    :param chat: The chat box object.
    :param text: Text the user has entered.
    :return:
    """
    # this is where you can add chat bot functionality!
    # text is the text the user has entered into the chat
    # you can use chat.send_ai_message("some text") to send a message as the AI, this will do background
    # you can use chat.start_gif() and chat.stop_gif() to start and stop the gif
    # you can use chat.clear() to clear the user and AI chat boxes

    # print the text the user entered to console
    print("User Entered Message: " + text)             
    
    ''' Here you can intercept the user input and override the bot
    output with your own responses and commands.'''
    # if the user send the "clear" message clear the chats
    if text.lower().find("erase chat") != -1:
        chat.clear()
    # user can say any form of bye to close the chat.
    elif text.lower().find("bye") != -1:
        # define a callback which will close the application
        def close():
            chat.exit()

        # send the goodbye message and provide the close function as a callback
        chat.send_ai_message("It has been good talking with you. Have a great day! Later!", callback=close)
    else:
        # offload chat bot processing to a worker thread and also send the result as an ai message
        chat.process_and_send_ai_message(chatbot.get_response, text)


# run the chat bot application
app.run()
