from flask import Flask, render_template, request
import requests
import datetime


app = Flask(__name__)

def get_server_time(url):
    try:
        response = requests.head(url, timeout=5)
        server_time = response.headers['date']
        return server_time
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    website_url = request.form['website_url']
    server_time = get_server_time(website_url)
    return render_template('result.html', website_url=website_url, server_time=server_time)


if __name__ == '__main__':
    app.run(debug=False)


