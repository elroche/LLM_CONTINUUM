from flask import Flask, render_template, request, redirect, session
from litellm import completion
import docx

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Clé secrète pour les sessions

# Dictionnaire pour stocker les résultats d'analyse des fichiers
file_results = {}


@app.route('/')
def index():
    if 'files_analyzed' in session:
        return render_template('index.html', show_question_form=True)
    else:
        return render_template('index.html', show_question_form=False)


@app.route('/upload_files', methods=['POST'])
def upload_files():
    global file_results
    file_paths = request.files.getlist('files')
    for file in file_paths:
        if file.filename.endswith('.txt'):
            content = file.read().decode('utf-8', 'ignore')
        elif file.filename.endswith('.docx'):
            content = read_docx(file)
        else:
            return render_template('error.html', message="Unsupported file format")

        # Analyse du contenu du fichier avec LLM et stockage des résultats
        response = completion(model="ollama/mistral", messages=[{"content": content, "role": "user"}])
        file_results[file.filename] = response

    session['files_analyzed'] = True  # Marquer les fichiers comme analysés
    return redirect('/')


@app.route('/ask_question', methods=['POST'])
def ask_question():
    global file_results
    question = request.form['question']
    responses = []
    for filename, result in file_results.items():
        # Utilisation des résultats d'analyse pour répondre à la question
        response = completion(model="ollama/mistral", messages=[{"content": result.choices[0].text, "role": "user"}, {"content": question, "role": "user"}])
        responses.append((filename, response.choices[0].text))
    return render_template('responses.html', question=question, responses=responses)



def read_docx(file):
    doc = docx.Document(file)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    return '\n'.join(full_text)


if __name__ == '__main__':
    app.run(debug=True)
