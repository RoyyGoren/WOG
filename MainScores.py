from flask import Flask, render_template
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)
@app.route('/')
def read_score():
    try:
        scores_open = open(SCORES_FILE_NAME, 'r')
        scores_content = int(scores_open.read())
        return render_template('WebScore.html', SCORE=scores_content)
    except ValueError:
        return render_template('WebError.html', ERROR=BAD_RETURN_CODE)

app.run()