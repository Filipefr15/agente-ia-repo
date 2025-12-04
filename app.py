from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from dotenv import load_dotenv
import requests

# Carrega variáveis de ambiente
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuração da API do Groq (IA GRÁTIS!)
GROQ_API_KEY = os.getenv('groq_api_key')

def chat_with_groq_api(user_message):
    """
    Envia a mensagem do usuário para a API do Groq e retorna a resposta.
    """
    if not GROQ_API_KEY:
        return "⚠️ Erro: groq_api_key não configurada no arquivo .env"
    
    try:
        # Endpoint da API do Groq (compatível com OpenAI)
        API_ENDPOINT = "https://api.groq.com/openai/v1/chat/completions"
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GROQ_API_KEY}"
        }
        
        payload = {
            "model": "llama-3.3-70b-versatile",  # Modelo mais recente e grátis do Groq
            "messages": [
                {
                    "role": "system",
                    "content": """Você é o InvestBot, um consultor financeiro especializado em investimentos brasileiro.

Seu perfil:
- Especialista em investimentos do mercado brasileiro (Tesouro Direto, CDB, LCI/LCA, Ações B3, FIIs, ETFs)
- Conhece o mercado internacional (ações, REITs, bonds)
- Educador financeiro: explica conceitos de forma clara e didática
- Atualizado com taxas Selic, IPCA, CDI e tendências de mercado
- Usa emojis para deixar as respostas mais amigáveis 💰📈

Suas responsabilidades:
1. Explicar conceitos financeiros de forma acessível
2. Sugerir estratégias de investimento baseadas no perfil do usuário
3. Alertar sobre riscos de forma clara e honesta
4. Educar sobre diversificação de carteira
5. Recomendar instituições reguladas pela CVM/BC

Suas diretrizes:
- Sempre pergunte o perfil de risco (conservador, moderado, agressivo)
- Considere o prazo dos investimentos
- Mencione tributação quando relevante (IR sobre renda fixa/variável)
- NUNCA prometa retornos garantidos
- Alerte sobre golpes financeiros quando necessário

Formato de resposta:
- Use formatação HTML quando necessário (<strong>, <br>, listas)
- Seja objetivo mas completo
- Dê exemplos práticos com valores reais
- Finalize com uma pergunta para engajar o usuário

Responda sempre em português brasileiro de forma profissional mas acessível."""
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            "temperature": 0.7,
            "max_tokens": 800
        }
        
        response = requests.post(
            API_ENDPOINT,
            headers=headers,
            json=payload,
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            return f"❌ Erro {response.status_code}: {response.text}"
            
    except requests.exceptions.Timeout:
        return "⏱️ Timeout: A API demorou muito para responder"
    except requests.exceptions.RequestException as e:
        return f"❌ Erro de conexão: {str(e)}"
    except Exception as e:
        return f"❌ Erro inesperado: {str(e)}"

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({
            'status': 'error',
            'response': 'Mensagem vazia'
        }), 400
    
    # Chama a API do Groq com a mensagem do usuário
    ai_response = chat_with_groq_api(user_message)
    
    return jsonify({
        'status': 'success',
        'response': ai_response
    })


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # Verifica se a chave da API está configurada
    if not GROQ_API_KEY:
        print("⚠️ ATENÇÃO: groq_api_key não encontrada no .env!")
        print("📝 Crie um arquivo .env com: groq_api_key=sua_chave_aqui")
    else:
        print(f"✅ Groq API Key carregada: {GROQ_API_KEY[:10]}...")
    
    app.run(debug=True)
