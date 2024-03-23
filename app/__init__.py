from flask import Flask, render_template, jsonify
from . import router

app = Flask(__name__)
app.register_blueprint(router.router)

@app.route('/health_check')
def health_check():
    print(__file__)
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run()





