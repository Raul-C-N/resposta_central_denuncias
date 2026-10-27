import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

SECCIONAIS = {
    "1ª Seccional Centro": {
        "nome": "Carlos Eduardo Duarte de Carvalho",
        "email": "carlosecarvalho@sp.gov.br"
    },
    "2ª Seccional Sul": {
        "nome": "Elaine Maria Biasoli",
        "email": "ebiasoli@sp.gov.br"
    },
    "3ª Seccional Oeste": {
        "nome": "Jurandir Correia de Sant’ Anna",
        "email": "jsantanna@sp.gov.br"
    },
    "4ª Seccional Norte": {
        "nome": "Adalberto Henrique Barbosa",
        "email": "ahbarbosa@sp.gov.br"
    },
    "5ª Seccional Leste": {
        "nome": "Jose Aparecido Sanches Severo",
        "email": "jsevero@sp.gov.br"
    },
    "6ª Seccional Santo Amaro": {
        "nome": "Génesio Leo Júnior",
        "email": "gljunior@sp.gov.br"
    },
    "7ª Seccional Itaquera": {
        "nome": "Antonio Jose Pereira",
        "email": "ajopereira@sp.gov.br"
    },
    "8ª Seccional São Mateus": {
        "nome": "Valter Sergio de Abreu",
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

    texto = f"""
{cabecalho}

MENSAGEM Nº {mensagem}/2026 UIP/DECAP
REF.: PROTOCOLO NÚMERO {protocolo}
ORIGEM: {origem}
ENDEREÇO: {endereco}
ÁREA CIRCUNSCRICIONAL: {seccional}

EXMO.(A) SR.(A) DR.(A)
{dados['nome']}

De ordem do Excelentíssimo Senhor Doutor Delegado de Polícia Diretor, encaminho a Vossa Excelência o expediente aqui recepcionado de forma eletrônica, para conhecimento e providências pertinentes, servindo-se, ainda, promover as anotações e comunicações oficiais de praxe.

Solicito, por oportuno, que cópia recibada das informações prestadas ao Órgão interessado seja encaminhada pela Unidade responsável a essa honrosa Delegacia Seccional de Polícia, para auditoria em âmbito correcional e, após constatada a regularidade do expediente, V. Exa. providencie a remessa exclusivamente ao endereço eletrônico uip.decap@policiacivil.sp.gov.br, visando os registros pertinentes e que permitam sua rastreabilidade.


PRAZO: 07 DIAS

At.te

------------------------------------------------------

DELEGADO(A) SECCIONAL
Nome: {dados['nome']}
E-mail: {dados['email']}
"""

    txt_resultado.delete("1.0", tk.END)
    txt_resultado.insert(tk.END, texto)


def copiar_texto():
    janela.clipboard_clear()
    janela.clipboard_append(txt_resultado.get("1.0", tk.END))
    messagebox.showinfo(
        "Sucesso",
        "Texto copiado para a área de transferência."
    )


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

ttk.Label(frame, text="Número do Protocolo:").grid(
    row=0, column=0, sticky="w"
)
ttk.Entry(
    frame,
    textvariable=protocolo_var,
    width=40
).grid(row=0, column=1, pady=5)

ttk.Label(frame, text="Número da Mensagem:").grid(
    row=1, column=0, sticky="w"
)
ttk.Entry(
    frame,
    textvariable=mensagem_var,
    width=40
).grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Canal de Atendimento:").grid(
    row=2, column=0, sticky="w"
)
ttk.Combobox(
    frame,
    textvariable=canal_var,
    values=["Central 180", "Disque 100"],
    state="readonly",
    width=37
).grid(row=2, column=1, pady=5)

ttk.Label(frame, text="Endereço:").grid(
    row=3, column=0, sticky="w"
)
ttk.Entry(
    frame,
    textvariable=endereco_var,
    width=60
).grid(row=3, column=1, pady=5)

ttk.Label(frame, text="Área Circunscricional:").grid(
    row=4, column=0, sticky="w"
)
ttk.Combobox(
    frame,
    textvariable=seccional_var,
    values=list(SECCIONAIS.keys()),
    state="readonly",
    width=37
).grid(row=4, column=1, pady=5)

ttk.Button(
    frame,
    text="Gerar Texto",
    command=gerar_texto
).grid(row=5, column=0, pady=15)

ttk.Button(
    frame,
    text="Copiar Texto",
    command=copiar_texto
).grid(row=5, column=1, pady=15, sticky="w")

# Resultado
txt_resultado = scrolledtext.ScrolledText(
    janela,
    wrap=tk.WORD,
    font=("Calibri", 11)
)
txt_resultado.pack(fill="both", expand=True, padx=10, pady=10)

janela.mainloop()