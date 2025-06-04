from flask import Flask, request
from flask_cors import CORS
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import os
import tempfile

app = Flask(__name__)

CORS(app)
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})

def remover_underline(texto):
    return texto.replace("_", " ") 

def quebrar_linhas(texto, limite):
    palavras = texto.split()
    linhas = []
    linha_atual = ""

    for palavra in palavras:
        if len(linha_atual) + len(palavra) + (1 if linha_atual else 0) <= limite:
            if linha_atual:
                linha_atual += " "
            linha_atual += palavra
        else:
            linhas.append(linha_atual)
            linha_atual = palavra  

    if linha_atual:
        linhas.append(linha_atual)

    return linhas

def gerar_pdf(arraydestring):
    largura_mm = 80
    altura_mm = 30  
    largura_pts = largura_mm * mm
    altura_pts = altura_mm * mm

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    caminho_arquivo = temp_file.name

    c = canvas.Canvas(caminho_arquivo, pagesize=(largura_pts, altura_pts))
    c.setFont("Helvetica-Bold", 18)

    nome = remover_underline(arraydestring[0]) 
    instituicao = remover_underline(arraydestring[1]) 
    evento = remover_underline(arraydestring[2]) 

    linhas_nome = quebrar_linhas(nome, 30)
    linhas_instituicao = quebrar_linhas(instituicao, 30)
    linhas_evento = quebrar_linhas(evento, 30) 

    pos_y = altura_pts / 2 + 14 
    
    for linha in linhas_nome:
        largura_texto = c.stringWidth(linha, "Helvetica-Bold", 18) 
        pos_x = (largura_pts - largura_texto) / 2 
        c.drawString(pos_x, pos_y, linha)
        pos_y -= 18

    c.setFont("Helvetica", 15)

    for linha in linhas_instituicao:
        largura_texto = c.stringWidth(linha, "Helvetica", 15)
        pos_x = (largura_pts - largura_texto) / 2
        c.drawString(pos_x, pos_y, linha)
        pos_y -= 15

    for linha in linhas_evento:
        largura_texto = c.stringWidth(linha, "Helvetica", 15)
        pos_x = (largura_pts - largura_texto) / 2
        c.drawString(pos_x, pos_y, linha)
        pos_y -= 15

    c.showPage()
    c.save()

    return caminho_arquivo

def imprimir_pdf(caminho_arquivo):
    print("aqui")
    os.startfile(caminho_arquivo, "print")

@app.route('/gerar_e_imprimir_pdf')
def gerar_e_imprimir_pdf():
    nome = request.args.get('nome')
    instituicao = request.args.get('instituicao')
    evento = request.args.get('evento')

    if not nome or not instituicao or not evento:
        return "Por favor, forneça os parâmetros 'nome', 'instituicao' e 'evento' na URL."

    arraydestring = [nome, instituicao, evento]

    caminho_pdf = gerar_pdf(arraydestring)
    imprimir_pdf(caminho_pdf)

    return f"PDF gerado e enviado para a impressora. O arquivo foi salvo em: {caminho_pdf}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
