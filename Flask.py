from flask import Flask, request, jsonify
import os
import nbformat
from nbconvert import PythonExporter

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert():
    # get the uploaded notebook file
    notebook_file = request.files['notebook_file']

    # save the notebook file to disk
    notebook_filename = notebook_file.filename
    notebook_file.save(notebook_filename)

    # convert the notebook file to a Python file
    notebook = nbformat.read(notebook_filename, as_version=4)
    exporter = PythonExporter()
    body, _ = exporter.from_notebook_node(notebook)
    python_filename = os.path.splitext(notebook_filename)[0] + '.py'
    with open(python_filename, 'w', encoding='utf-8') as f:
        f.write(body)

    # delete the uploaded notebook file from disk
    os.remove(notebook_filename)

    # return the name of the converted file to the frontend
    return jsonify({'input_file': notebook_filename, 'output_file': python_filename})

if __name__ == '__main__':
    app.run(debug=True)
