# 🖨️ Gerador e Impressor de Etiquetas em PDF com Flask

Este projeto consiste em uma API backend, desenvolvida com **Flask**, que tem como objetivo receber dados via URL, gerar uma etiqueta de identificação em formato PDF e enviá-la diretamente para a impressora padrão configurada no servidor.

É uma solução leve e prática para cenários onde é necessário imprimir etiquetas ou crachás de forma automatizada, como em eventos, recepções ou sistemas de credenciamento.

---

## 🚀 Tecnologias Utilizadas

* **Python**: Linguagem principal da aplicação.
* **Flask**: Micro-framework web utilizado para construir a API.
* **ReportLab**: Biblioteca poderosa para a criação e manipulação programática de arquivos PDF.

---

## ✅ Funcionalidades Principais

* **API Simples**: Um único endpoint (`/gerar_e_imprimir_pdf`) que recebe os dados via query parameters.
* **Geração Dinâmica de PDF**: Cria um arquivo PDF formatado (80mm x 30mm) com os dados recebidos (nome, instituição e evento).
* **Formatação Automática**: O texto é centralizado e as linhas são quebradas automaticamente para caber nas dimensões da etiqueta.
* **Impressão Direta**: Envia o PDF gerado diretamente para a fila de impressão do sistema operacional do servidor.
