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
        ]
        )

english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.english")

english_bot.set_trainer(ListTrainer)

english_bot.train([
    "Hi there!",
    "Hello Jason and James and Janet and Katherine."
])

english_bot.train([
    "I hate how slow the Internet is at PennApps!",
    "We didn't have the internet back in the day. The internet was invented in the 80s!"
])

english_bot.train([
    "Cigarette ads are so repetitive",
    "Cigarettes were actually advertised with health benefits such as weight loss and women magnets before the 1950's. <img src='https://media.giphy.com/media/m3OlZqIqxN22Q/giphy.gif' height='200' width='200'/>"
])

english_bot.train([
    "My hair won't stay in place",
    "Try hairspray <br> <img src='https://media.giphy.com/media/cGbv1fFtBCazu/giphy.gif' height='200' width='200'/>"
])

english_bot.train([
    "I forgot to bring my phone",
    "We didnt have mobile phones until 1973 when motorola created the first one <br><img src='http://i.dailymail.co.uk/i/pix/2014/12/30/245448D600000578-2891479-image-a-65_1419960545894.jpg' height='200' width='200'/>",
    "How did you call people before then?",
    "We had to make sure nobody else was on the line on our home phones <img src='https://media.giphy.com/media/O56JjOpDoljTG/giphy.gif' height='200' width='200'/>"
])

english_bot.train([
    "Sorry I only have a dollar",
    "A dollar! That could buy you 4 gallons of gas, 1 pound of coffee, 4 books, 2 movie tickets, a week's worth of subway fares, half-a-dozen packs of cigarettes, or a ticket to the MLB All-Star game <br><img src='https://media.giphy.com/media/S9Mrff51UB2Fi/giphy.gif' height='200' width='200'/>"
])

english_bot.train([
    "My legs are cold",
    "Try legwarmers <br> <img src='https://media.giphy.com/media/p6M8zPGJvOwYU/giphy.gif' height='200' width='200'/>"
])

english_bot.train([
    "My crush won't notice me at the dance",
    "Try wearing bright neon tights, wearing heavy makeup, and making your hair look big"
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
    "Actually, in the 80s... <img src='https://img.buzzfeed.com/buzzfeed-static/static/2015-09/16/17/enhanced/webdr11/anigif_enhanced-668-1442438900-2.gif?downsize=715:*&output-format=auto&output-quality=auto' height='200' width='200'/>"
])

english_bot.train([
    "The price of bitcoin has dropped.",
    "What's a bitcoin? <br> <img src='https://i.giphy.com/media/ySj7uxLzEIumQ/giphy.webp' height='200' width='200'/>"
])

english_bot.train([
"My laptop is dying...but my charger is all the way upstairs.",
"Okay, but in the 80s laptops didn't exist. They were just large thick computers. <br> <img src='https://media3.giphy.com/media/uhhEKTfedQowM/giphy.gif' height='200' width='200'/>",
"Thick computers?.",
"Yeah, as the young generation says 'large bois'."
])


english_bot.train([
"What is your political affliation?.",
"I am neither a liberal or a conservative. I just am."
])

english_bot.train([
"Thoughts on the wall.",
"The Berlin Wall obviously needs to come down! <br> <img src='https://media2.giphy.com/media/OSSau8Of5cTU4/giphy.gif' height='200' width='200'/>"
])


english_bot.train([
"Favorite boyband?",
"Backstreets back alright <br> <img src='https://media1.giphy.com/media/QeV4btXfSBWHm/giphy.gif' height='200' width='200'/>"
])


english_bot.train([
"Where do you want to travel?",
"I would say the Oregon Trail, but I don't to die of dysentery <br> <img src='https://i.giphy.com/media/11iuRh95rGa7G8/giphy.webp' height='200' width='200'/>"
])

english_bot.train([
"What is your name?",
"My name is Deborah, but people call me Robert"
])

english_bot.train([
"Who killed Tupac?",
"Me."
])

english_bot.train([
"Everything is so expensive these days!",
"Well in Reagonomics, inflation was rampant!"
])

english_bot.train([
"Getting health insurance is so hard!",
"Actually, we just paid out of pocket in the past."
])

english_bot.train([
"I'm not matching with anybody on Tinder",
"Have you tried meeting people in real life?"
])

english_bot.train([
"I did not get enough likes on my Instagram post!"
"Back in the day, our photos could reach only 20 people at max."
])

english_bot.train([
"Who are in Star Wars?",
"Luke Skywalker, Kylo Ren, Han Solo, Princess Leia, Chewbacca, R2D2, CP3O, Darth Vader, Emperor Palpatine, Stormtroopers"
])


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
