import os.path
from flask import Flask, render_template, request, Response

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r'C:\Users\Leniu\PycharmProjects\sjtudy\systemy informatyczne internetu rzeczy\laby 2\upload'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        upload_file = request.files['file']
        if upload_file.filename.endswith('.txt'):
            upload_file.save(os.path.join(app.config['UPLOAD_FOLDER'],upload_file.filename))
            return "saved"

    return render_template('index.html')

@app.route('/get/<file>', methods=['GET'])
def file_opened(file):
    line = request.args.get(file)
    if not line:
        content = get_file_lines(name=file)

        return Response(content, mimetype='text/plain')
    else:
        return 'brak'


def get_file_lines(name):
    path = os.path.join(app.config['UPLOAD_FOLDER'], name)
    with open(path,'r') as file:
        lines = file.readlines()
        return lines


if __name__== '__main__':
    app.run()
