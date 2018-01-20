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

english_bot.train([
    "i want more likes on my profile picture",
    "<img src='https://static.boredpanda.com/blog/wp-content/uploads/2014/12/satiric-illustrations-john-holcroft-1.jpg' height='200' width='200' />"
])

english_bot.train([
    "i like to drink too much. convince me to stop drinking",
    "<img src='https://static.boredpanda.com/blog/wp-content/uploads/2014/12/satiric-illustrations-john-holcroft-2.jpg' height='200' width='200'/>"
])

english_bot.train([
    "I hate having to wait. i dont want to wait for ads",
    "Actually, in the 80s, if you forget to rewind the video you wanted to watch you'd have to wait five whole minutes. <img src='https://img.buzzfeed.com/buzzfeed-static/static/2015-09/16/19/enhanced/webdr10/anigif_enhanced-17916-1442447274-7.gif?downsize=715:*&output-format=auto&output-quality=auto' height='200' width='200'/>"
])

english_bot.train([
    "my phone sucks. my friend isn't picking up.",
    "Actually, in the 80s... < img src='https://img.buzzfeed.com/buzzfeed-static/static/2015-09/16/17/enhanced/webdr11/anigif_enhanced-668-1442438900-2.gif?downsize=715:*&output-format=auto&output-quality=auto' height='200' width='200'/>"
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
