import re
import tkinter as tk
from tkinter import ttk, scrolledtext


def extrair_dados():
    texto = txt_entrada.get("1.0", tk.END)

    # Protocolo
    protocolo = ""
    match = re.search(
        r"Protocolo de atendimento:\s*(\d+)",
        texto,
        re.IGNORECASE
    )
    if match:
        protocolo = match.group(1)

    # Canal
    canal = "NÃO IDENTIFICADO"
    texto_maiusculo = texto.upper()

    if (
        "MINISTÉRIO DAS MULHERES" in texto_maiusculo
        or "LIGUE 180" in texto_maiusculo
        or "CENTRAL DE ATENDIMENTO À MULHER" in texto_maiusculo
    ):
        canal = "CENTRAL 180"

    elif (
        "MINISTÉRIO DOS DIREITOS HUMANOS" in texto_maiusculo
        or "DISQUE 100" in texto_maiusculo
    ):
        canal = "DISQUE 100"

    # Primeiro endereço encontrado
    endereco = ""
    match = re.search(
        r"Endereço:\s*(.*?)(?:Ponto de referência:|Nome:|$)",
        texto,
        re.IGNORECASE | re.DOTALL
    )
    if match:
        endereco = " ".join(match.group(1).split())

    resultado = (
        f"PROTOCOLO: {protocolo}\n"
        f"CANAL: {canal}\n"
        f"ENDEREÇO: {endereco}"
    )

    txt_saida.delete("1.0", tk.END)
    txt_saida.insert("1.0", resultado)


def copiar_resultado():
    janela.clipboard_clear()
    janela.clipboard_append(txt_saida.get("1.0", tk.END))


# Interface
janela = tk.Tk()
janela.title("Extrator de Dados - Central 180 / Disque 100")
janela.geometry("900x700")

frame = ttk.Frame(janela, padding=10)
frame.pack(fill="both", expand=True)

ttk.Label(
    frame,
    text="Cole o texto da denúncia:"
).pack(anchor="w")

txt_entrada = scrolledtext.ScrolledText(
    frame,
    height=20,
    wrap=tk.WORD
)
txt_entrada.pack(fill="both", expand=True, pady=5)

btn_frame = ttk.Frame(frame)
btn_frame.pack(fill="x", pady=10)

ttk.Button(
    btn_frame,
    text="Extrair Dados",
    command=extrair_dados
).pack(side="left", padx=5)

ttk.Button(
    btn_frame,
    text="Copiar Resultado",
    command=copiar_resultado
).pack(side="left", padx=5)

ttk.Label(
    frame,
    text="Resultado:"
).pack(anchor="w")

txt_saida = scrolledtext.ScrolledText(
    frame,
    height=8,
    wrap=tk.WORD
)
txt_saida.pack(fill="both", expand=True)

janela.mainloop()
