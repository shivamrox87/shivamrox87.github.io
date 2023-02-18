import os
from nbconvert.exporters.python import PythonExporter

def convert_notebook_to_python(notebook_filename):
    notebook_basename = os.path.basename(notebook_filename)
    notebook_dirname = os.path.dirname(notebook_filename)
    notebook_basename_no_ext = os.path.splitext(notebook_basename)[0]
    python_filename = os.path.join(notebook_dirname, notebook_basename_no_ext + '.py')

    with open(notebook_filename) as f:
        body = f.read()

    exporter = PythonExporter()
    (python_body, resources) = exporter.from_notebook_node(exporter.from_filename(notebook_filename)[0])

    with open(python_filename, 'w', encoding='utf-8') as f:
        f.write(python_body)

    return (notebook_basename, os.path.basename(python_filename))
