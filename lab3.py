from flask import Flask
app = Flask(__name__)

@app.route('/api/v1/hello-world-21')
def hello_world():
    return 'Hello World 21', 200

if __name__ == '__main__':
    app.run(debug=True)

#curl -v -XGET http://127.0.0.1:8000/api/v1/hello-world-21
#curl -v -XGET http://127.0.0.1:5000/api/v1/hello-world-21
