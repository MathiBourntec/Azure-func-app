import azure.functions as func
from flask import Flask, render_template

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def home():
    return render_template('index.html')

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.WsgiMiddleware(app.wsgi_app).handle(req)
