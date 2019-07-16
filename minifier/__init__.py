from flask import Flask, redirect, request
from minifier.model import get_link, shortify
from codra import Template

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def main():
    if request.method == 'GET':
        with open('minifier/templates/form.html', 'r') as fd:
            return Template(fd.read()).render()
    else:
        link = shortify(request.form['link'])
        with open('minifier/templates/view_result.html', 'r') as fd:
            return Template(fd.read()).render(link = link)

@app.route('/<link>')
def forward(link):
    return redirect(get_link(link), code = 302)
