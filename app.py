from flask import Flask, request, jsonify
from flask_cors import CORS # ler arquivo html

# habilita a função para ler dados
app=Flask(__name__)
CORS(app)

# retorna uma resposta simulada baseado na mensagem do usuário
def get_ai_response(user_message):

    msg=user_message.lower()
    if "olá" in msg or "oi" in msg:
        return "Olá! O servidor IA recebeu a mensagem!"
    elif "agente de ia" in msg:
        return "Eu sou o agente de IA e estou funcionando!"
    elif "python" in msg:
        return "O agent de IA está funcionando!"
    else:
        return f"Recebi a mensagem, {user_message}. Sou seu assistente pessoal! 🙂"

@app.route('/api/chat', methods=['POST'])
def chat():
    data=request.get_json()
    user_message=data.get('message', '')

    return jsonify({
        'status': 'success',
        'response': ai_text
    })

@app.route('/', methods=['GET'])
def index():
    return "O agente de IA está funcionando"

if __name__=='__main__':
    app.run(debug=True)
