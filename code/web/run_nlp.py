import configparser
from flask import Flask, url_for, send_from_directory, redirect

from nlp import *

config = configparser.RawConfigParser()
config.read('rusnlp.cfg')
url = config.get('Other', 'url')

app_rusnlp = Flask(__name__, static_url_path='/data/')

@app_rusnlp.route('/data/<path:query>/')
def send(query):
    if 'rus_nlp.db.gz' in query:
        return redirect('http://rusvectores.org/static/rusnlp/rus_nlp.db.gz')
    else:
        return send_from_directory('data/', query)


app_rusnlp.register_blueprint(nlpsearch)


def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)


app_rusnlp.jinja_env.globals['url_for_other_page'] = url_for_other_page

if __name__ == '__main__':
    app_rusnlp.run()