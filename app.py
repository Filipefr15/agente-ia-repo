from flask import Flask, request, jsonify, render_template
from flask_cors import CORS # ler arquivo html

# habilita a função para ler dados
app=Flask(__name__)
CORS(app)

# InvestBot - IA especializada em consultoria de investimentos
def get_ai_response(user_message):
    import re
    
    msg = user_message.lower()
    
    # 🏦 SAUDAÇÕES E APRESENTAÇÃO
    if any(word in msg for word in ["olá", "oi", "bom dia", "boa tarde", "boa noite", "hello"]):
        return "Olá! 👋 Sou o InvestBot, seu consultor de investimentos pessoal. Como posso ajudá-lo a fazer seu dinheiro trabalhar para você hoje?"
    
    # 🎯 PERGUNTA ESPECÍFICA: Como começar a investir com pouco dinheiro?
    if "como começar a investir com pouco dinheiro" in msg:
        return """🌱 <strong>Como Começar a Investir com Pouco Dinheiro:</strong><br><br>

💰 <strong>Valores para começar:</strong><br>
• <strong>R$ 30:</strong> Tesouro Direto (mínimo)<br>
• <strong>R$ 100:</strong> CDB de bancos digitais<br>
• <strong>R$ 200:</strong> Primeiros ETFs (BOVA11, IVVB11)<br><br>

📋 <strong>Passo a passo prático:</strong><br>
1. 🏦 <strong>Abra conta gratuita:</strong> Inter, Rico, Clear ou XP<br>
2. 💳 <strong>Transfira R$ 100-300</strong> da sua conta corrente<br>
3. 🎯 <strong>Comece com Tesouro Selic</strong> (liquidez diária, 13% ao ano)<br>
4. 📚 <strong>Estude 30min/dia</strong> enquanto investe básico<br>
5. 📈 <strong>Evolua gradualmente</strong> para ações e ETFs<br><br>

🔥 <strong>Estratégia dos R$ 200/mês:</strong><br>
• R$ 100 → Tesouro IPCA+ (segurança)<br>
• R$ 100 → BOVA11 (ações Brasil)<br><br>

<strong>Em 1 ano:</strong> R$ 2.400 investidos + rendimentos = ~R$ 2.600<br>
<strong>Em 5 anos:</strong> ~R$ 15.000 (com aportes regulares)<br><br>

💡 <strong>Lembre-se:</strong> Consistência > valor inicial!"""
    
    # 💰 COMEÇAR A INVESTIR / INICIANTES (demais variações)
    elif any(phrase in msg for phrase in ["começar", "iniciar", "primeiro", "nunca investi", "iniciante", "como investir"]):
        return """💡 **Primeiros Passos para Investir:**
        
1. 🎯 **Reserve sua emergência** - 6 meses de gastos em poupança
2. 📚 **Estude o básico** - Renda fixa vs variável 
3. 🏦 **Abra conta em corretora** - XP, Rico, Clear, Inter
4. 💵 **Comece pequeno** - R$ 100/mês já faz diferença
5. 📊 **Diversifique** - Não coloque tudo em um lugar

**Sugestão inicial:** Tesouro IPCA+ (inflação) + algum fundo de ações. Quer saber sobre algum específico?"""
    
    # 📊 PERGUNTA ESPECÍFICA: Qual a diferença entre ações e fundos?
    elif "qual a diferença entre ações e fundos" in msg:
        return """📊 <strong>Ações vs Fundos - Comparação Completa:</strong><br><br>

🏢 <strong>AÇÕES INDIVIDUAIS:</strong><br>
✅ <strong>Vantagens:</strong><br>
• Você escolhe exatamente qual empresa<br>
• Potencial de ganhos altos (100%+ ao ano)<br>
• Controle total da carteira<br>
• Dividendos diretos da empresa<br><br>

❌ <strong>Desvantagens:</strong><br>
• Risco alto (pode perder 50%+ em crises)<br>
• Precisa estudar cada empresa<br>
• Mínimo ~R$ 200 para diversificar<br>
• Tempo para análise e acompanhamento<br><br>

📈 <strong>FUNDOS DE INVESTIMENTO:</strong><br>
✅ <strong>Vantagens:</strong><br>
• Gestão profissional (especialista escolhe)<br>
• Diversificação automática<br>
• Pequenos valores (a partir de R$ 100)<br>
• Menos tempo dedicado<br><br>

❌ <strong>Desvantagens:</strong><br>
• Taxa de administração (0,5% - 3% ao ano)<br>
• Menor controle individual<br>
• Dependência do gestor<br>
• Pode não bater o mercado<br><br>

🎯 <strong>RECOMENDAÇÃO PRÁTICA:</strong><br>
• <strong>Iniciante:</strong> ETFs (BOVA11, IVVB11) - melhor de ambos<br>
• <strong>Intermediário:</strong> 70% ETFs + 30% ações individuais<br>
• <strong>Avançado:</strong> Ações individuais (após muito estudo)<br><br>

<strong>ETFs são ideais:</strong> Baixa taxa (0,3% ao ano) + diversificação + simplicidade!"""
    
    # 🌍 PERGUNTA ESPECÍFICA: Como diversificar minha carteira?
    elif "como diversificar minha carteira" in msg:
        return """🌍 <strong>Guia Completo de Diversificação:</strong><br><br>

🎯 <strong>REGRA DE OURO:</strong> "Não coloque todos os ovos na mesma cesta"<br><br>

📊 <strong>CARTEIRA MODELO CONSERVADORA:</strong><br>
• 🏛️ <strong>50%</strong> Renda Fixa (Tesouro IPCA+, CDB)<br>
• 🇧🇷 <strong>30%</strong> Ações Brasil (BOVA11 ou individuais)<br>
• 🇺🇸 <strong>15%</strong> Ações Exterior (IVVB11 - S&P 500)<br>
• 🏢 <strong>5%</strong> Fundos Imobiliários (FIIs)<br><br>

⚡ <strong>CARTEIRA MODELO AGRESSIVA:</strong><br>
• 🏛️ <strong>20%</strong> Renda Fixa (emergência)<br>
• 🇧🇷 <strong>40%</strong> Ações Brasil<br>
• 🇺🇸 <strong>25%</strong> Ações Exterior<br>
• 🏢 <strong>10%</strong> FIIs<br>
• 💎 <strong>5%</strong> Ativos alternativos (REITs, Commodities)<br><br>

🎂 <strong>DIVERSIFICAÇÃO POR IDADE:</strong><br>
• <strong>20-30 anos:</strong> 80% renda variável + 20% fixa<br>
• <strong>30-50 anos:</strong> 60% renda variável + 40% fixa<br>
• <strong>50+ anos:</strong> 30% renda variável + 70% fixa<br><br>

🔄 <strong>DIVERSIFICAÇÃO POR SETORES (Ações):</strong><br>
• Bancos, Tecnologia, Consumo, Utilities, Commodities<br><br>

⏰ <strong>REBALANCEAMENTO:</strong><br>
A cada 6 meses, volte às proporções originais vendendo o que subiu muito e comprando o que caiu.<br><br>

💡 <strong>Dica:</strong> Comece simples com 3-4 ativos e evolua gradualmente!"""
    
    # ⚠️ PERGUNTA ESPECÍFICA: Quais os riscos de investir em ações?
    elif "quais os riscos de investir em ações" in msg:
        return """⚠️ <strong>Análise Completa dos Riscos das Ações:</strong><br><br>

🔴 <strong>PRINCIPAIS RISCOS:</strong><br><br>

<strong>1. 📉 Risco de Mercado (Volatilidade)</strong><br>
• Ações podem cair 20-50% em crises<br>
• Ibovespa já caiu 40% em 2020 (COVID)<br>
• Recuperação pode levar anos<br><br>

<strong>2. 🏢 Risco da Empresa</strong><br>
• Empresa pode quebrar (ex: Oi, Samarco)<br>
• Má gestão, corrupção, problemas operacionais<br>
• Perda de 100% do investimento<br><br>

<strong>3. 💱 Risco Cambial</strong><br>
• Dólar afeta ações (commodities, importadores)<br>
• Empresas com dívida em dólar sofrem mais<br><br>

<strong>4. 🏛️ Risco Político/Regulatório</strong><br>
• Mudanças na política afetam setores<br>
• Novas leis podem prejudicar empresas<br><br>

🛡️ <strong>COMO SE PROTEGER:</strong><br><br>

<strong>✅ Diversificação:</strong><br>
• Nunca mais de 5% em uma ação<br>
• Invista em setores diferentes<br>
• Use ETFs para diversificação automática<br><br>

<strong>✅ Prazo Longo:</strong><br>
• Ações são para 5+ anos mínimo<br>
• Tempo dilui a volatilidade<br>
• Média histórica: 15%+ ao ano (longo prazo)<br><br>

<strong>✅ Stop Loss Mental:</strong><br>
• Se perdeu 20%, analise se deve sair<br>
• Não se apegue emocionalmente<br>
• Aceite prejuízos pequenos<br><br>

<strong>✅ Educação Contínua:</strong><br>
• Entenda a empresa antes de comprar<br>
• Acompanhe resultados trimestrais<br>
• Leia análises de especialistas<br><br>

🎯 <strong>REGRA FUNDAMENTAL:</strong><br>
Só invista em ações o dinheiro que pode ficar parado por 5+ anos e que não fará falta se perder 50%.<br><br>

💡 <strong>Para iniciantes:</strong> Comece com ETFs (BOVA11) - risco diluído entre 60+ empresas!"""
    
    # 📈 AÇÕES E BOLSA
    elif any(phrase in msg for phrase in ["ação", "ações", "bolsa", "b3", "bovespa", "papéis"]):
        return """📈 **Investimento em Ações:**
        
**Vantagens:** 
• Potencial de altos retornos
• Liquidez diária 
• Proteção contra inflação

**Riscos:**
• Volatilidade alta
• Pode perder dinheiro no curto prazo
• Precisa de conhecimento

**Dica de ouro:** Invista apenas o que pode ficar parado por 5+ anos. Considere ETFs para diversificação automática (IVVB11, BOVA11).

Quer analisar alguma ação específica?"""
    
    # 🏛️ RENDA FIXA
    elif any(word in msg for word in ["renda fixa", "tesouro", "cdb", "lci", "lca", "selic", "ipca"]):
        return """🏛️ **Renda Fixa - Investimentos Seguros:**
        
**Tesouro Direto:**
• 💚 Selic (juros curto prazo): 13,25% ao ano
• 📊 IPCA+ (inflação): IPCA + 6% ao ano
• 📅 Prefixado: Taxa fixa conhecida

**CDBs de Bancos:**
• 🏦 Grandes bancos: 95-100% do CDI
• 🚀 Bancos digitais: até 120% do CDI
• 🛡️ Garantia FGC até R$ 250 mil

**Recomendação:** 60% Tesouro IPCA+ / 40% CDB 120% CDI para começar."""
    
    # 📊 FUNDOS DE INVESTIMENTO
    elif any(word in msg for word in ["fundo", "fundos", "fii", "etf", "cotas"]):
        return """📊 **Fundos de Investimento:**
        
**ETFs (Recomendados):**
• 🇺🇸 IVVB11: S&P 500 (ações americanas)
• 🇧🇷 BOVA11: Ibovespa (ações brasileiras)
• 💰 FIXA11: Renda fixa brasileira

**Fundos Imobiliários (FIIs):**
• 🏢 Dividendos mensais
• 🏠 Exposição ao mercado imobiliário
• ⚠️ Risco médio-alto

**Taxa de administração:** Prefira fundos com taxa < 1% ao ano. ETFs costumam ter as menores taxas!"""
    
    # 💵 VALORES E QUANTO INVESTIR
    elif "quanto" in msg or "valor" in msg or "dinheiro" in msg or "reais" in msg or "mil" in msg or "salário" in msg or re.findall(r'r\$?\s*(\d+(?:\.\d{3})*(?:,\d{2})?|\d+)', msg):
        return """💵 **Quanto Investir:**
        
**Regra 50-30-20:**
• 50% gastos essenciais
• 30% gastos pessoais  
• 20% investimentos + emergência

**Por faixa de renda:**
• 📱 Até R$ 3.000: R$ 200/mês - Tesouro + CDB
• 💼 R$ 3-8.000: R$ 500/mês - 70% renda fixa + 30% ações
• 🚀 Acima R$ 8.000: R$ 1.000+ - Diversificação completa

**Meta:** Acumular 12x seus gastos mensais em 5-10 anos!"""
    
    # ⚠️ RISCOS E SEGURANÇA  
    elif any(word in msg for word in ["risco", "riscos", "seguro", "perder", "prejuízo", "perigoso"]):
        return """⚠️ **Gestão de Riscos:**
        
**Níveis de Risco:**
• 🟢 **Baixo:** Tesouro, CDB, Poupança
• 🟡 **Médio:** Fundos mistos, FIIs
• 🔴 **Alto:** Ações individuais, Cripto

**Regras de Ouro:**
1. 🚫 Nunca invista dinheiro que precisa em < 2 anos
2. 📊 Diversifique entre classes de ativos
3. 📚 Só invista no que entende
4. ⏰ Tempo é seu maior aliado

**Lembre-se:** Maior risco = maior retorno potencial (mas também maior chance de perda)."""
    
    # 🌍 DIVERSIFICAÇÃO (outras variações além da pergunta específica)
    elif any(word in msg for word in ["diversificar", "diversificação", "carteira", "portfolio"]):
        return """🌍 **Diversificação Inteligente:**
        
**Carteira Balanceada:**
• 🏛️ 40% Renda Fixa (Tesouro + CDB)
• 🇧🇷 30% Ações Brasil (BOVA11 ou individuais)
• 🇺🇸 20% Ações Exterior (IVVB11)
• 🏢 10% FIIs (Fundos imobiliários)

**Por Idade:**
• 👶 20-30 anos: 70% ações + 30% renda fixa
• 👨‍💼 30-50 anos: 50% ações + 50% renda fixa  
• 👴 50+ anos: 30% ações + 70% renda fixa

**Rebalanceamento:** Ajuste a carteira a cada 6-12 meses."""
    
    # 💎 CRIPTOMOEDAS
    if any(word in msg for word in ["bitcoin", "crypto", "cripto", "btc", "ethereum"]):
        return """💎 **Criptomoedas - Alto Risco:**
        
**⚠️ ATENÇÃO:** Extremamente volátil!
• 📈 Pode valorizar 100%+ em meses
• 📉 Pode desvalorizar 80%+ também
• 🎲 Considere apenas 5-10% da carteira

**Se for investir:**
• 🏦 Use exchanges regulamentadas (Mercado Bitcoin, Binance)
• 💰 Bitcoin e Ethereum são as mais estabelecidas
• ⏰ Pense em anos, não dias

**Regra:** Só invista o que pode perder 100% sem afetar sua vida!"""
    
    # 🏠 FINANCIAMENTO IMOBILIÁRIO
    if any(word in msg for word in ["casa", "apartamento", "imóvel", "financiamento", "própria"]):
        return """🏠 **Casa Própria vs Investimento:**
        
**Vantagens da Casa Própria:**
• 🛡️ Segurança emocional
• 🏠 Patrimônio tangível
• 📈 Proteção contra inflação do aluguel

**Análise Financeira:**
• 💰 Compare: prestação vs aluguel + investimento
• 🧮 Considere: IPTU, condomínio, manutenção
• ⏰ Imóvel demora para se valorizar (10+ anos)

**Dica:** Se prestação > 30% da renda, melhor alugar + investir a diferença em ações/fundos."""
    
    # 📚 EDUCAÇÃO FINANCEIRA
    if any(word in msg for word in ["aprender", "estudar", "livro", "curso", "educação"]):
        return """📚 **Educação Financeira:**
        
**Livros Essenciais:**
• 📖 "Pai Rico, Pai Pobre" - Robert Kiyosaki
• 💰 "O Investidor Inteligente" - Benjamin Graham  
• 🧠 "Psicologia Financeira" - Morgan Housel

**Canais YouTube:**
• 🎥 Primo Rico, Me Poupe!, Gustavo Cerbasi

**Cursos Gratuitos:**
• 🏦 CVM (Comissão de Valores Mobiliários)
• 📱 Apps: GuiaBolso, Organizze

**Dica:** 30min/dia de estudo = grande diferença em 1 ano!"""
    
    # 🚨 GOLPES E FRAUDES
    if any(word in msg for word in ["golpe", "fraude", "pirâmide", "esquema", "fácil", "garantido"]):
        return """🚨 **ALERTA: Como Evitar Golpes:**
        
**Sinais de GOLPE:**
• 🎯 Promessas de 20%+ ao mês
• ⚡ "Ganhos rápidos e garantidos"
• 👥 Pirâmides financeiras
• 💎 "Oportunidade única"

**NUNCA:**
• Empreste CPF para "investimentos"
• Invista sem entender
• Acredite em "fórmulas mágicas"
• Ignore a regulamentação CVM/BC

**SEMPRE verifique:** Empresa regulamentada, registros na CVM, reputação no Reclame Aqui."""
    
    # 📱 TECNOLOGIA E APPS
    if any(word in msg for word in ["app", "aplicativo", "plataforma", "corretora", "conta"]):
        return """📱 **Melhores Plataformas:**
        
**Corretoras Recomendadas:**
• 🏆 XP Investimentos (completa)
• 💎 Rico (foco renda fixa)  
• 🚀 Clear (day trade)
• 🏦 Inter Invest (banco digital)

**Apps Úteis:**
• 📊 Status Invest (análises)
• 💰 TradeMap (acompanhamento)
• 📈 Yahoo Finanças (cotações)

**Dicas:** 
• Compare taxas antes de escolher
• Prefira taxa zero para pessoa física
• Teste a plataforma com pouco dinheiro primeiro"""
    
    # 🎯 OBJETIVOS FINANCEIROS
    if any(word in msg for word in ["objetivo", "meta", "aposentadoria", "independência", "liberdade"]):
        return """🎯 **Planejamento de Objetivos:**
        
**Independência Financeira:**
• 💰 Meta: 25x seus gastos anuais investidos
• 📈 Retorno 4% ao ano = viver de renda
• ⏰ Com R$ 2.000/mês investidos: ~20 anos

**Aposentadoria:**
• 🏦 INSS: máximo R$ 7.500/mês  
• 💼 Previdência privada como complemento
• 📊 Carteira própria: mais flexibilidade

**Fórmula do Sucesso:** Gastar < Ganhar + Investir a diferença + Tempo + Juros compostos"""
    
    # 🔄 REBALANCEAMENTO
    if any(word in msg for word in ["rebalancear", "rebalanceamento", "ajustar", "revisar"]):
        return """🔄 **Rebalanceamento de Carteira:**
        
**Quando fazer:**
• ⏰ A cada 6-12 meses
• 📊 Quando algum ativo sair 5%+ do target
• 💰 Quando aportar valores grandes

**Como fazer:**
• 📈 Venda ativos que subiram muito
• 📉 Compre ativos que caíram
• 💵 Use novos aportes para equilibrar

**Exemplo:** Se ações subiram de 30% para 45% da carteira, venda até voltar aos 30%."""
    
    # 📊 ANÁLISE TÉCNICA
    if any(word in msg for word in ["análise", "gráfico", "indicador", "suporte", "resistência"]):
        return """📊 **Análise de Investimentos:**
        
**Para Ações - Análise Fundamentalista:**
• 💰 P/L: Preço/Lucro (prefira < 15)
• 📈 ROE: Retorno sobre patrimônio (> 15%)
• 💵 Dividend Yield: Dividendos/Preço (> 5%)

**Indicadores Macroeconômicos:**
• 🏛️ Taxa Selic: Afeta renda fixa
• 📊 IPCA: Inflação oficial
• 💱 Dólar: Impacta ações e importações

**Dica:** Para pessoa física, análise fundamentalista > técnica. Foque no longo prazo!"""
    
    # 💡 CASES DE SUCESSO / EXEMPLOS
    if any(word in msg for word in ["exemplo", "simulação", "caso", "prática", "real"]):
        return """💡 **Exemplo Prático - Carteira R$ 1.000/mês:**
        
**Distribuição Mensal:**
• 🏛️ R$ 400 - Tesouro IPCA+ 2029 (40%)
• 🇧🇷 R$ 300 - BOVA11 (ETF Ibovespa - 30%)  
• 🇺🇸 R$ 200 - IVVB11 (ETF S&P500 - 20%)
• 🏢 R$ 100 - HGLG11 (FII - 10%)

**Projeção 10 anos (7% a.a.):**
• 💰 Investido: R$ 120.000
• 📈 Valor final: ~R$ 170.000
• 🎯 Ganho: R$ 50.000

**Resultado:** Patrimônio para gerar R$ 850/mês de renda passiva!"""

    # 🤖 SOBRE O BOT
    if any(word in msg for word in ["quem é você", "bot", "ia", "inteligência", "robô"]):
        return """🤖 **Sobre o InvestBot:**
        
Sou uma IA especializada em educação financeira e consultoria de investimentos! 
        
**Posso ajudar com:**
• 📚 Educação financeira básica
• 💰 Sugestões de investimentos 
• 📊 Análise de carteiras
• ⚠️ Orientação sobre riscos
• 🎯 Planejamento financeiro

**⚠️ Importante:** Minhas orientações são educativas. Sempre consulte um especialista antes de grandes decisões financeiras!"""
    
    # 📞 CONTATO E SUPORTE
    if any(word in msg for word in ["ajuda", "suporte", "contato", "dúvida"]):
        return """📞 **Como posso ajudar mais:**
        
**Pergunte sobre:**
• 💰 "Como investir R$ 5.000?"
• 📊 "Qual a melhor carteira para iniciante?"
• 🏠 "Vale a pena comprar casa própria?"
• ⚠️ "Quais os riscos das ações?"
• 🎯 "Como planejar aposentadoria?"

**Ou use os botões de perguntas rápidas acima!** 
        
Estou aqui 24/7 para turbinar sua educação financeira! 🚀"""
    
    # 🔍 PESQUISA/BUSCA GENÉRICA
    if any(word in msg for word in ["pesquisar", "buscar", "encontrar", "procurar"]):
        return """🔍 **O que gostaria de pesquisar?**
        
**Tópicos populares:**
• 💰 Investimentos para iniciantes
• 📈 Ações vs Fundos de investimento  
• 🏛️ Renda fixa vs Renda variável
• 🏠 Casa própria vs Aluguel + Investimento
• ⚠️ Como avaliar riscos de investimento
• 🎯 Planejamento para aposentadoria

Digite sua dúvida específica que eu explico detalhadamente! 💡"""
    
    # ❓ RESPOSTA PADRÃO INTELIGENTE
    else:
        return f"""🤔 **Interessante pergunta sobre:** "{user_message}"
        
Ainda estou aprendendo sobre esse tópico específico! Mas posso ajudar com:

**💰 Investimentos Básicos:**
• Tesouro Direto, CDBs, Fundos, Ações
• Como começar a investir
• Análise de riscos

**📊 Planejamento Financeiro:**  
• Organização de gastos
• Metas de investimento
• Aposentadoria

**Reformule sua pergunta ou escolha um dos temas acima!** 
        
*Exemplo: "Como investir R$ 1.000 por mês?" ou "Qual o melhor investimento para iniciantes?"* 🎯"""

@app.route('/api/chat', methods=['POST'])
def chat():
    data=request.get_json()
    user_message=data.get('message', '')
    ai_text = get_ai_response(user_message)

    return jsonify({
        'status': 'success',
        'response': ai_text
    })

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
