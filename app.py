from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Salam, dünya!'

@app.route('/run_code', methods=['POST'])
def run_code():
    data = request.get_json()
    code = data.get('code', '')

    try:
        # Təhlükəsiz şəkildə Python kodunu işlətmək
        exec_globals = {}
        exec(code, exec_globals)
        result = exec_globals.get('result', 'Kodun nəticəsi yoxdur')
    except Exception as e:
        result = f"Xəta baş verdi: {str(e)}"
    
    return jsonify({'result': result})

if __name__ == '__main__':
    # Flask serverini 5001 portunda işə salırıq
    app.run(host="0.0.0.0", port=5001, debug=True)
