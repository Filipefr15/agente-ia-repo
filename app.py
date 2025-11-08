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
        return """💡 <strong>Primeiros Passos para Investir:</strong><br><br>
        
1. 🎯 <strong>Reserve sua emergência</strong> - 6 meses de gastos em poupança<br>
2. 📚 <strong>Estude o básico</strong> - Renda fixa vs variável<br>
3. 🏦 <strong>Abra conta em corretora</strong> - XP, Rico, Clear, Inter<br>
4. 💵 <strong>Comece pequeno</strong> - R$ 100/mês já faz diferença<br>
5. 📊 <strong>Diversifique</strong> - Não coloque tudo em um lugar<br><br>

<strong>Sugestão inicial:</strong> Tesouro IPCA+ (inflação) + algum fundo de ações. Quer saber sobre algum específico?"""
    
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
        return """📈 <strong>Investimento em Ações:</strong><br><br>
        
<strong>Vantagens:</strong><br>
• Potencial de altos retornos<br>
• Liquidez diária<br>
• Proteção contra inflação<br><br>

<strong>Riscos:</strong><br>
• Volatilidade alta<br>
• Pode perder dinheiro no curto prazo<br>
• Precisa de conhecimento<br><br>

<strong>Dica de ouro:</strong> Invista apenas o que pode ficar parado por 5+ anos. Considere ETFs para diversificação automática (IVVB11, BOVA11).<br><br>

Quer analisar alguma ação específica?"""
    
    # 🏛️ RENDA FIXA
    elif any(word in msg for word in ["renda fixa", "tesouro", "cdb", "lci", "lca", "selic", "ipca"]):
        return """🏛️ <strong>Renda Fixa - Investimentos Seguros:</strong><br><br>
        
<strong>Tesouro Direto:</strong><br>
• 💚 Selic (juros curto prazo): 13,25% ao ano<br>
• 📊 IPCA+ (inflação): IPCA + 6% ao ano<br>
• 📅 Prefixado: Taxa fixa conhecida<br><br>

<strong>CDBs de Bancos:</strong><br>
• 🏦 Grandes bancos: 95-100% do CDI<br>
• 🚀 Bancos digitais: até 120% do CDI<br>
• 🛡️ Garantia FGC até R$ 250 mil<br><br>

<strong>Recomendação:</strong> 60% Tesouro IPCA+ / 40% CDB 120% CDI para começar."""
    
    # 📊 FUNDOS DE INVESTIMENTO
    elif any(word in msg for word in ["fundo", "fundos", "fii", "etf", "cotas"]):
        return """📊 <strong>Fundos de Investimento:</strong><br><br>
        
<strong>ETFs (Recomendados):</strong><br>
• 🇺🇸 IVVB11: S&P 500 (ações americanas)<br>
• 🇧🇷 BOVA11: Ibovespa (ações brasileiras)<br>
• 💰 FIXA11: Renda fixa brasileira<br><br>

<strong>Fundos Imobiliários (FIIs):</strong><br>
• 🏢 Dividendos mensais<br>
• 🏠 Exposição ao mercado imobiliário<br>
• ⚠️ Risco médio-alto<br><br>

<strong>Taxa de administração:</strong> Prefira fundos com taxa &lt; 1% ao ano. ETFs costumam ter as menores taxas!"""
    
    # 💵 VALORES E QUANTO INVESTIR
    elif "quanto" in msg or "valor" in msg or "dinheiro" in msg or "reais" in msg or "mil" in msg or "salário" in msg or re.findall(r'r\$?\s*(\d+(?:\.\d{3})*(?:,\d{2})?|\d+)', msg):
        return """💵 <strong>Quanto Investir:</strong><br><br>
        
<strong>Regra 50-30-20:</strong><br>
• 50% gastos essenciais<br>
• 30% gastos pessoais<br>
• 20% investimentos + emergência<br><br>

<strong>Por faixa de renda:</strong><br>
• 📱 Até R$ 3.000: R$ 200/mês - Tesouro + CDB<br>
• 💼 R$ 3-8.000: R$ 500/mês - 70% renda fixa + 30% ações<br>
• 🚀 Acima R$ 8.000: R$ 1.000+ - Diversificação completa<br><br>

<strong>Meta:</strong> Acumular 12x seus gastos mensais em 5-10 anos!"""
    
    # ⚠️ RISCOS E SEGURANÇA  
    elif any(word in msg for word in ["risco", "riscos", "seguro", "perder", "prejuízo", "perigoso"]):
        return """⚠️ <strong>Gestão de Riscos:</strong><br><br>
        
<strong>Níveis de Risco:</strong><br>
• 🟢 <strong>Baixo:</strong> Tesouro, CDB, Poupança<br>
• 🟡 <strong>Médio:</strong> Fundos mistos, FIIs<br>
• 🔴 <strong>Alto:</strong> Ações individuais, Cripto<br><br>

<strong>Regras de Ouro:</strong><br>
1. 🚫 Nunca invista dinheiro que precisa em &lt; 2 anos<br>
2. 📊 Diversifique entre classes de ativos<br>
3. 📚 Só invista no que entende<br>
4. ⏰ Tempo é seu maior aliado<br><br>

<strong>Lembre-se:</strong> Maior risco = maior retorno potencial (mas também maior chance de perda)."""
    
    # 🌍 DIVERSIFICAÇÃO (outras variações além da pergunta específica)
    elif any(word in msg for word in ["diversificar", "diversificação", "carteira", "portfolio"]):
        return """🌍 <strong>Diversificação Inteligente:</strong><br><br>
        
<strong>Carteira Balanceada:</strong><br>
• 🏛️ 40% Renda Fixa (Tesouro + CDB)<br>
• 🇧🇷 30% Ações Brasil (BOVA11 ou individuais)<br>
• 🇺🇸 20% Ações Exterior (IVVB11)<br>
• 🏢 10% FIIs (Fundos imobiliários)<br><br>

<strong>Por Idade:</strong><br>
• 👶 20-30 anos: 70% ações + 30% renda fixa<br>
• 👨‍💼 30-50 anos: 50% ações + 50% renda fixa<br>
• 👴 50+ anos: 30% ações + 70% renda fixa<br><br>

<strong>Rebalanceamento:</strong> Ajuste a carteira a cada 6-12 meses."""
    
    # 💎 CRIPTOMOEDAS
    if any(word in msg for word in ["bitcoin", "crypto", "cripto", "btc", "ethereum"]):
        return """💎 <strong>Criptomoedas - Alto Risco:</strong><br><br>
        
<strong>⚠️ ATENÇÃO:</strong> Extremamente volátil!<br>
• 📈 Pode valorizar 100%+ em meses<br>
• 📉 Pode desvalorizar 80%+ também<br>
• 🎲 Considere apenas 5-10% da carteira<br><br>

<strong>Se for investir:</strong><br>
• 🏦 Use exchanges regulamentadas (Mercado Bitcoin, Binance)<br>
• 💰 Bitcoin e Ethereum são as mais estabelecidas<br>
• ⏰ Pense em anos, não dias<br><br>

<strong>Regra:</strong> Só invista o que pode perder 100% sem afetar sua vida!"""
    
    # 🏠 FINANCIAMENTO IMOBILIÁRIO
    if any(word in msg for word in ["casa", "apartamento", "imóvel", "financiamento", "própria"]):
        return """🏠 <strong>Casa Própria vs Investimento:</strong><br><br>
        
<strong>Vantagens da Casa Própria:</strong><br>
• 🛡️ Segurança emocional<br>
• 🏠 Patrimônio tangível<br>
• 📈 Proteção contra inflação do aluguel<br><br>

<strong>Análise Financeira:</strong><br>
• 💰 Compare: prestação vs aluguel + investimento<br>
• 🧮 Considere: IPTU, condomínio, manutenção<br>
• ⏰ Imóvel demora para se valorizar (10+ anos)<br><br>

<strong>Dica:</strong> Se prestação &gt; 30% da renda, melhor alugar + investir a diferença em ações/fundos."""
    
    # 📚 EDUCAÇÃO FINANCEIRA
    if any(word in msg for word in ["aprender", "estudar", "livro", "curso", "educação"]):
        return """📚 <strong>Educação Financeira:</strong><br><br>
        
<strong>Livros Essenciais:</strong><br>
• 📖 "Pai Rico, Pai Pobre" - Robert Kiyosaki<br>
• 💰 "O Investidor Inteligente" - Benjamin Graham<br>
• 🧠 "Psicologia Financeira" - Morgan Housel<br><br>

<strong>Canais YouTube:</strong><br>
• 🎥 Primo Rico, Me Poupe!, Gustavo Cerbasi<br><br>

<strong>Cursos Gratuitos:</strong><br>
• 🏦 CVM (Comissão de Valores Mobiliários)<br>
• 📱 Apps: GuiaBolso, Organizze<br><br>

<strong>Dica:</strong> 30min/dia de estudo = grande diferença em 1 ano!"""
    
    # 🚨 GOLPES E FRAUDES
    if any(word in msg for word in ["golpe", "fraude", "pirâmide", "esquema", "fácil", "garantido"]):
        return """🚨 <strong>ALERTA: Como Evitar Golpes:</strong><br><br>
        
<strong>Sinais de GOLPE:</strong><br>
• 🎯 Promessas de 20%+ ao mês<br>
• ⚡ "Ganhos rápidos e garantidos"<br>
• 👥 Pirâmides financeiras<br>
• 💎 "Oportunidade única"<br><br>

<strong>NUNCA:</strong><br>
• Empreste CPF para "investimentos"<br>
• Invista sem entender<br>
• Acredite em "fórmulas mágicas"<br>
• Ignore a regulamentação CVM/BC<br><br>

<strong>SEMPRE verifique:</strong> Empresa regulamentada, registros na CVM, reputação no Reclame Aqui."""
    
    # 📱 TECNOLOGIA E APPS
    if any(word in msg for word in ["app", "aplicativo", "plataforma", "corretora", "conta"]):
        return """📱 <strong>Melhores Plataformas:</strong><br><br>
        
<strong>Corretoras Recomendadas:</strong><br>
• 🏆 XP Investimentos (completa)<br>
• 💎 Rico (foco renda fixa)<br>
• 🚀 Clear (day trade)<br>
• 🏦 Inter Invest (banco digital)<br><br>

<strong>Apps Úteis:</strong><br>
• 📊 Status Invest (análises)<br>
• 💰 TradeMap (acompanhamento)<br>
• 📈 Yahoo Finanças (cotações)<br><br>

<strong>Dicas:</strong><br>
• Compare taxas antes de escolher<br>
• Prefira taxa zero para pessoa física<br>
• Teste a plataforma com pouco dinheiro primeiro"""
    
    # 🎯 OBJETIVOS FINANCEIROS
    if any(word in msg for word in ["objetivo", "meta", "aposentadoria", "independência", "liberdade"]):
        return """🎯 <strong>Planejamento de Objetivos:</strong><br><br>
        
<strong>Independência Financeira:</strong><br>
• 💰 Meta: 25x seus gastos anuais investidos<br>
• 📈 Retorno 4% ao ano = viver de renda<br>
• ⏰ Com R$ 2.000/mês investidos: ~20 anos<br><br>

<strong>Aposentadoria:</strong><br>
• 🏦 INSS: máximo R$ 7.500/mês<br>
• 💼 Previdência privada como complemento<br>
• 📊 Carteira própria: mais flexibilidade<br><br>

<strong>Fórmula do Sucesso:</strong> Gastar &lt; Ganhar + Investir a diferença + Tempo + Juros compostos"""
    
    # 🔄 REBALANCEAMENTO
    if any(word in msg for word in ["rebalancear", "rebalanceamento", "ajustar", "revisar"]):
        return """🔄 <strong>Rebalanceamento de Carteira:</strong><br><br>
        
<strong>Quando fazer:</strong><br>
• ⏰ A cada 6-12 meses<br>
• 📊 Quando algum ativo sair 5%+ do target<br>
• 💰 Quando aportar valores grandes<br><br>

<strong>Como fazer:</strong><br>
• 📈 Venda ativos que subiram muito<br>
• 📉 Compre ativos que caíram<br>
• 💵 Use novos aportes para equilibrar<br><br>

<strong>Exemplo:</strong> Se ações subiram de 30% para 45% da carteira, venda até voltar aos 30%."""
    
    # 📊 ANÁLISE TÉCNICA
    if any(word in msg for word in ["análise", "gráfico", "indicador", "suporte", "resistência"]):
        return """📊 <strong>Análise de Investimentos:</strong><br><br>
        
<strong>Para Ações - Análise Fundamentalista:</strong><br>
• 💰 P/L: Preço/Lucro (prefira &lt; 15)<br>
• 📈 ROE: Retorno sobre patrimônio (&gt; 15%)<br>
• 💵 Dividend Yield: Dividendos/Preço (&gt; 5%)<br><br>

<strong>Indicadores Macroeconômicos:</strong><br>
• 🏛️ Taxa Selic: Afeta renda fixa<br>
• 📊 IPCA: Inflação oficial<br>
• 💱 Dólar: Impacta ações e importações<br><br>

<strong>Dica:</strong> Para pessoa física, análise fundamentalista &gt; técnica. Foque no longo prazo!"""
    
    # 💡 CASES DE SUCESSO / EXEMPLOS
    if any(word in msg for word in ["exemplo", "simulação", "caso", "prática", "real"]):
        return """💡 <strong>Exemplo Prático - Carteira R$ 1.000/mês:</strong><br><br>
        
<strong>Distribuição Mensal:</strong><br>
• 🏛️ R$ 400 - Tesouro IPCA+ 2029 (40%)<br>
• 🇧🇷 R$ 300 - BOVA11 (ETF Ibovespa - 30%)<br>
• 🇺🇸 R$ 200 - IVVB11 (ETF S&P500 - 20%)<br>
• 🏢 R$ 100 - HGLG11 (FII - 10%)<br><br>

<strong>Projeção 10 anos (7% a.a.):</strong><br>
• 💰 Investido: R$ 120.000<br>
• 📈 Valor final: ~R$ 170.000<br>
• 🎯 Ganho: R$ 50.000<br><br>

<strong>Resultado:</strong> Patrimônio para gerar R$ 850/mês de renda passiva!"""

    # 🤖 SOBRE O BOT
    if any(word in msg for word in ["quem é você", "bot", "ia", "inteligência", "robô"]):
        return """🤖 <strong>Sobre o InvestBot:</strong><br><br>
        
Sou uma IA especializada em educação financeira e consultoria de investimentos!<br><br>
        
<strong>Posso ajudar com:</strong><br>
• 📚 Educação financeira básica<br>
• 💰 Sugestões de investimentos<br>
• 📊 Análise de carteiras<br>
• ⚠️ Orientação sobre riscos<br>
• 🎯 Planejamento financeiro<br><br>

<strong>⚠️ Importante:</strong> Minhas orientações são educativas. Sempre consulte um especialista antes de grandes decisões financeiras!"""
    
    # 📞 CONTATO E SUPORTE
    if any(word in msg for word in ["ajuda", "suporte", "contato", "dúvida"]):
        return """📞 <strong>Como posso ajudar mais:</strong><br><br>
        
<strong>Pergunte sobre:</strong><br>
• 💰 "Como investir R$ 5.000?"<br>
• 📊 "Qual a melhor carteira para iniciante?"<br>
• 🏠 "Vale a pena comprar casa própria?"<br>
• ⚠️ "Quais os riscos das ações?"<br>
• 🎯 "Como planejar aposentadoria?"<br><br>

<strong>Ou use os botões de perguntas rápidas acima!</strong><br><br>
        
Estou aqui 24/7 para turbinar sua educação financeira! 🚀"""
    
    # 🔍 PESQUISA/BUSCA GENÉRICA
    if any(word in msg for word in ["pesquisar", "buscar", "encontrar", "procurar"]):
        return """🔍 <strong>O que gostaria de pesquisar?</strong><br><br>
        
<strong>Tópicos populares:</strong><br>
• 💰 Investimentos para iniciantes<br>
• 📈 Ações vs Fundos de investimento<br>
• 🏛️ Renda fixa vs Renda variável<br>
• 🏠 Casa própria vs Aluguel + Investimento<br>
• ⚠️ Como avaliar riscos de investimento<br>
• 🎯 Planejamento para aposentadoria<br><br>

Digite sua dúvida específica que eu explico detalhadamente! 💡"""
    
    # ❓ RESPOSTA PADRÃO INTELIGENTE
    else:
        return f"""🤔 <strong>Interessante pergunta sobre:</strong> "{user_message}"<br><br>
        
Ainda estou aprendendo sobre esse tópico específico! Mas posso ajudar com:<br><br>

<strong>💰 Investimentos Básicos:</strong><br>
• Tesouro Direto, CDBs, Fundos, Ações<br>
• Como começar a investir<br>
• Análise de riscos<br><br>

<strong>📊 Planejamento Financeiro:</strong><br>
• Organização de gastos<br>
• Metas de investimento<br>
• Aposentadoria<br><br>

<strong>Reformule sua pergunta ou escolha um dos temas acima!</strong><br><br>
        
<em>Exemplo: "Como investir R$ 1.000 por mês?" ou "Qual o melhor investimento para iniciantes?"</em> 🎯"""

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
