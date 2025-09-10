from flask import Flask, request
from subprocess import run, PIPE

app = Flask(__name__)

@app.route('/compile', methods=['POST'])
def compile_code():
    code = request.json.get('code')
    result = run(['python', '-c', code], stdout=PIPE, stderr=PIPE, text=True)
    return {'output': result.stdout + result.stderr}