#!/usr/bin/env python3
"""
Script de Auditoria Básica de Sistema
Gera um resumo do ambiente (Linux/Windows) em formato JSON.
"""

import json
import os
import platform
import socket
import sys
from datetime import datetime


def coletar_informacoes():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Obter nome do host e IP
    hostname = socket.gethostname()
    try:
        ip_local = socket.gethostbyname(hostname)
    except Exception:
        ip_local = "127.0.0.1"

    info = {
        "relatorio": {
            "gerado_em": timestamp,
            "sistema_operacional": platform.system(),
            "versao_so": platform.release(),
            "arquitetura": platform.machine(),
            "hostname": hostname,
            "ip_local": ip_local,
            "versao_python": sys.version.split()[0],
            "diretorio_atual": os.getcwd(),
        }
    }

    return info


def salvar_relatorio(dados, filename="relatorio_sistema.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)
    print(f"[+] Relatório gerado com sucesso: {filename}")


if __name__ == "__main__":
    print("Coletando informações do sistema...")
    dados = coletar_informacoes()

    # Exibe no terminal
    print(json.dumps(dados, indent=4, ensure_ascii=False))

    # Salva em arquivo
    salvar_relatorio(dados)

    