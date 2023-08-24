from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/questions')
def populate_questions():
    """render the questions form for the prompt"""

    prompts = silly_story.prompts

    return render_template("questions.html",
                           prompt_names = prompts)


# use action tag to direct to new page
# we need a way to id all of the inputs
# when we know id's we also know where our submission data will be
# can predict key value pairs in arg object
# need to create view function that has get
# can use request.args to get all sumbitted info

@app.get('/results')
def result_page():
    """renders resulting story"""

    our_story = silly_story.get_result_text(request.args)
    return render_template("results.html",the_story = our_story )