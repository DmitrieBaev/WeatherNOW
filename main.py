from flask import (Flask,
                   request, render_template,
                   url_for)

app = Flask(__name__)


@app.route('/')
def index():
    """
    Обработка главной страницы

    :return: Шаблон главной страницы
    """
    # Можно использовать request.remote_addr или request.environ['REMOTE_ADDR']
    ipaddr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
