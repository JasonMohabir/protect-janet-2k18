from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, UbuntuCorpusTrainer, ListTrainer

app = Flask(__name__)

english_bot = ChatBot("Chatterbot", 
                      storage_adapter="chatterbot.storage.SQLStorageAdapter",
                      logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
            },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'input_text': 'Who are you?',
            'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org/en/latest/quickstart.html'
            }
        ]
                      )

#english_bot.set_trainer(ChatterBotCorpusTrainer)
#english_bot.train("chatterbot.corpus.english")

english_bot.set_trainer(ListTrainer)

english_bot.train([
    "Hi there!",
    "Hello Jason."
])

english_bot.train([
    "I hate how slow the Internet is at PennApps!",
    "Dumb bitch we didn't have the internet back in the day."
])

english_bot.train([
    "Who are you?",
    "I am Deborah Downer, a Chatbot created by team NYC++ at PennApps Spring 2018."
])

#english_bot.set_trainer(UbuntuCorpusTrainer)
#english_bot.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(english_bot.get_response(userText))

if __name__ == "__main__":
    app.debug = True
    app.run()
