from flask import Flask, render_template

application = Flask(__name__)
application.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'

@application.route('/')
def sessions():
    return render_template('session.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


if __name__ == '__main__':
    application.run(host='0.0.0.0')
