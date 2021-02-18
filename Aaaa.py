from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/image_mars')
def image():
    return f'''<html>
    <head>
        <link rel='stylesheet' type="text/css" href="{url_for('static', filename='css/wow_style.css')}">
        <title>Привет, Марс!</title>
    </head>
    <body>
        <h1> Жди нас, Марс!<h1>
        <img src="{url_for('static', filename='img/mars.png')}"
             alt="здесь должна была быть картинка, но не нашлась">
        <h2>Вот она какая, красная планета!</h2>
    </body>
    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
