import os
from boilerflask import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config["DEBUG"], port=int(os.environ.get('PORT', 5000)))