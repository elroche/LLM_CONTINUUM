from flask import Flask, render_template, request
from litellm import completion
import docx
import textract

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask_question', methods=['POST'])
def ask_question():
    question = request.form['question']
    file_paths = request.files.getlist('files')
    responses = []
    
    for file in file_paths:
        if file.filename.endswith('.txt'):
            content = file.read().decode('utf-8', 'ignore')
        elif file.filename.endswith('.docx'):
            content = read_docx(file)
        else:
            return render_template('error.html', message="Unsupported file format")

        # Utiliser le modèle pour obtenir la réponse
        response = completion(model="ollama/mistral", messages=[{"content": content, "role": "user"},{"content": question, "role": "user"}])

        # Extraire la réponse textuelle
        response_text = response.choices[0].message.content

        responses.append((file.filename, response_text))
    
    return render_template('responses.html', question=question, responses=responses)

def read_docx(file):
    doc = docx.Document(file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)

if __name__ == '__main__':
    app.run(debug=True)