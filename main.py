from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
    """
    Обработка главной страницы

    :return:
    """
    # Можно использовать request.remote_addr или request.environ['REMOTE_ADDR']
    ipaddr = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    return f'<p>IP: {ipaddr}</p>'


if __name__ == '__main__':
    app.run(debug=True)
