"""A madlib game that compliments its users."""

from random import choices

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    list_of_compliments = choices(AWESOMENESS, k = 3)

    return render_template("compliment.html",
                           person=player.title(),
                           compliments=list_of_compliments)

@app.route('/game')
def show_madlibs_form():
	"""Get user's response to 'would you like to play a game?'."""

	play_game = request.args.get("game")

	if play_game == "yes":
		return render_template("game.html")

	else:
		return render_template("goodbye.html")

@app.route('/goodbye')
def say_goodbye():
	"""Say goodbye to user."""

	return render_template("goodbye.html")

@app.route('/madlibs')
def show_madlibs():
	"""Shows madlib provided by the user."""

	person_name = request.args.get("person-name")

	color = request.args.get("color")

	noun = request.args.get("noun")

	adjective = request.args.get("adjective")

	return render_template("madlibs.html", person=person_name.title(), color=color, noun=noun, adjective=adjective)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
