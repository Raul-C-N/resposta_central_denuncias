import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import re

SECCIONAIS = {
    "1ª Seccional Centro": {
        "nome": "Carlos Eduardo Duarte de Carvalho"+"\n"+"M.D. DELEGADO DE POLÍCIA TITULAR DA 1ª DELEGACIA SECCIONAL DE POLÍCIA - CENTRO",
        "email": "carlosecarvalho@sp.gov.br"
    },
    "2ª Seccional Sul": {
        "nome": "Elaine Maria Biasoli"+"\n"+"M.D. DELEGADA DE POLÍCIA TITULAR DA 2ª DELEGACIA SECCIONAL DE POLÍCIA - SUL",
        "email": "ebiasoli@sp.gov.br"
    },
    "3ª Seccional Oeste": {
        "nome": "Jurandir Correia de Sant’ Anna"+"\n"+"M.D. DELEGADO DE POLÍCIA TITULAR DA 3ª DELEGACIA SECCIONAL DE POLÍCIA - OESTE",
        "email": "jsantanna@sp.gov.br"
    },
    "4ª Seccional Norte": {
        "nome": "Adalberto Henrique Barbosa"+"\n"+"M.D. DELEGADO DE POLÍCIA TITULAR DA 4ª DELEGACIA SECCIONAL DE POLÍCIA - NORTE",
        "email": "ahbarbosa@sp.gov.br"
    },
    "5ª Seccional Leste": {
        "nome": "Jose Aparecido Sanches Severo"+"\n"+"M.D. DELEGADO DE POLÍCIA TITULAR DA 5ª DELEGACIA SECCIONAL DE POLÍCIA - LESTE",
        "email": "jsevero@sp.gov.br"
    },
    "6ª Seccional Santo Amaro": {
        "nome": "Génesio Leo Júnior"+"\n"+"M.D. DELEGADO DE POLÍCIA TITULAR DA 6ª DELEGACIA SECCIONAL DE POLÍCIA - SANTO AMARO",
        "email": "gljunior@sp.gov.br"
    },
    "7ª Seccional Itaquera": {
        "nome": "Antonio Jose Pereira"+"\n"+"M.D. DELEGADO DE POLÍCIA TITULAR DA 7ª DELEGACIA SECCIONAL DE POLÍCIA - ITAQUERA",
        "email": "ajopereira@sp.gov.br"
    },
    "8ª Seccional São Mateus": {
        "nome": "Valter Sergio de Abreu"+"\n"+"M.D. DELEGADO DE POLÍCIA TITULAR DA 8ª DELEGACIA SECCIONAL DE POLÍCIA - SÃO MATEUS",
        "email": "vabreu@sp.gov.br"
    }
}

def gerar_texto():
    protocolo = protocolo_var.get().strip()
    mensagem = mensagem_var.get().strip()
    canal = canal_var.get()
    endereco = endereco_var.get().strip()
    seccional = seccional_var.get()
    
    if not protocolo:
        messagebox.showwarning("Atenção", "Informe o número do protocolo.")
        return
    if not mensagem:
        messagebox.showwarning("Atenção", "Informe o número da mensagem.")
        return
        
    if canal == "Central 180":
        cabecalho = f"PROTOCOLO – {protocolo} – CENTRAL 180"
        origem = "CENTRAL DE ATENDIMENTO À MULHER – LIGUE 180"
    else:
        cabecalho = f"PROTOCOLO – {protocolo} – DISQUE 100"
        origem = "MINISTÉRIO DOS DIREITOS HUMANOS – DISQUE 100"
        
    dados = SECCIONAIS[seccional]
    
    texto_com_tags = f"""<NEGRITO>{cabecalho}</NEGRITO>
<NEGRITO>MENSAGEM Nº {mensagem}/2026 UIP/DECAP</NEGRITO>
<NEGRITO>REF.: PROTOCOLO NÚMERO {protocolo}</NEGRITO>
<NEGRITO>ORIGEM: {origem}</NEGRITO>
<NEGRITO>ENDEREÇO: {endereco}</NEGRITO>
<NEGRITO>ÁREA CIRCUNSCRICIONAL: {seccional}</NEGRITO>
<NEGRITO>EXMO.(A) SR.(A) DR.(A)</NEGRITO>
<NEGRITO>{dados['nome']}</NEGRITO>

De ordem do Excelentíssimo Senhor Doutor Delegado de Polícia Diretor, encaminho a Vossa Excelência o expediente aqui recepcionado de forma eletrônica, para conhecimento e providências pertinentes, servindo-se, ainda, promover as anotações e comunicações oficiais de praxe.

Solicito, por oportuno, que <NEGRITO>cópia recibada das informações prestadas ao Órgão interessado</NEGRITO> seja encaminhada <NEGRITO>pela Unidade responsável</NEGRITO> a essa honrosa Delegacia Seccional de Polícia, <NEGRITO>para auditoria em âmbito correcional</NEGRITO> e, após constatada a regularidade do expediente, V. Exa. providencie a remessa <NEGRITO>exclusivamente</NEGRITO> ao endereço eletrônico uip.decap@policiacivil.sp.gov.br, visando os registros pertinentes e que permitam sua rastreabilidade.

<NEGRITO>PRAZO: 07 DIAS</NEGRITO>

At.te

------------------------------------------------------
DELEGADO(A) SECCIONAL
Nome: {dados['nome']}
E-mail: {dados['email']}"""

    txt_resultado.delete("1.0", tk.END)
    
    # Processa as tags de negrito inserindo o texto limpo e mapeando as posições
    padrao = re.compile(r"<NEGRITO>(.*?)</NEGRITO>", re.DOTALL)
    ultimo_indice = 0
    
    for match in padrao.finditer(texto_com_tags):
        # Insere o texto normal que veio antes do padrão de negrito
        txt_resultado.insert(tk.END, texto_com_tags[ultimo_indice:match.start()])
        
        # Guarda a posição de início do negrito
        pos_inicio = txt_resultado.index(tk.CURRENT)
        # Insere apenas o conteúdo interno da tag
        txt_resultado.insert(tk.END, match.group(1))
        # Guarda a posição de fim do negrito
        pos_fim = txt_resultado.index(tk.CURRENT)
        
        # Aplica a tag de negrito no trecho correspondente
        txt_resultado.tag_add("negrito", pos_inicio, pos_fim)
        ultimo_indice = match.end()
        
    # Insere o restante do texto que ficou após a última tag
    txt_resultado.insert(tk.END, texto_com_tags[ultimo_indice:])

    # --- SISTEMA DE COR NO TKINTER --- #
    trechos_para_colorir = [
        "para auditoria em âmbito correcional",
        "PRAZO: 07 DIAS"
    ]
    
    for trecho in trechos_para_colorir:
        inicio = "1.0"
        while True:
            posicao = txt_resultado.search(trecho, inicio, stopindex=tk.END)
            if not posicao:
                break
            fim = f"{posicao}+{len(trecho)}c"
            txt_resultado.tag_add("vermelho", posicao, fim)
            inicio = fim

def copiar_texto():
    janela.clipboard_clear()
    janela.clipboard_append(txt_resultado.get("1.0", tk.END).strip())
    messagebox.showinfo("Sucesso", "Texto copiado para a área de transferência.")

# Janela principal
janela = tk.Tk()
janela.title("Resposta Central 180 / Disque 100")
janela.geometry("900x700")

# Variáveis
protocolo_var = tk.StringVar()
mensagem_var = tk.StringVar()
endereco_var = tk.StringVar()
canal_var = tk.StringVar(value="Central 180")
seccional_var = tk.StringVar(value=list(SECCIONAIS.keys())[0])

# Frame entrada
frame = ttk.Frame(janela, padding=10)
frame.pack(fill="x")

ttk.Label(frame, text="Número do Protocolo:").grid(row=0, column=0, sticky="w")
ttk.Entry(frame, textvariable=protocolo_var, width=40).grid(row=0, column=1, pady=5)

ttk.Label(frame, text="Número da Mensagem:").grid(row=1, column=0, sticky="w")
ttk.Entry(frame, textvariable=mensagem_var, width=40).grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Canal de Atendimento:").grid(row=2, column=0, sticky="w")
ttk.Combobox(frame, textvariable=canal_var, values=["Central 180", "Disque 100"], state="readonly", width=37).grid(row=2, column=1, pady=5)

ttk.Label(frame, text="Endereço:").grid(row=3, column=0, sticky="w")
ttk.Entry(frame, textvariable=endereco_var, width=60).grid(row=3, column=1, pady=5)

ttk.Label(frame, text="Área Circunscricional:").grid(row=4, column=0, sticky="w")
ttk.Combobox(frame, textvariable=seccional_var, values=list(SECCIONAIS.keys()), state="readonly", width=37).grid(row=4, column=1, pady=5)

ttk.Button(frame, text="Gerar Texto", command=gerar_texto).grid(row=5, column=0, pady=15)
ttk.Button(frame, text="Copiar Texto", command=copiar_texto).grid(row=5, column=1, pady=15, sticky="w")

# Resultado
txt_resultado = scrolledtext.ScrolledText(janela, wrap=tk.WORD, font=("Calibri", 11))
txt_resultado.pack(fill="both", expand=True, padx=10, pady=10)

# Configurações globais de tags de estilo do componente de texto
txt_resultado.tag_config("vermelho", foreground="red")
txt_resultado.tag_config("negrito", font=("Calibri", 11, "bold"))

janela.mainloop()
