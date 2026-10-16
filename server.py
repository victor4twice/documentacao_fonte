#!/usr/bin/env python3
"""
Servidor local do Painel de Gravações.

- Serve os arquivos desta pasta em http://localhost:8000
- Expõe /api/fontes: lista automaticamente as fontes soltas na pasta "fonts"
  (a subpasta vira a categoria; arquivos na raiz ficam em "Minhas fontes").
- Só aceita conexões deste computador (127.0.0.1).

Uso:  python server.py        (ou py server.py no Windows)
      python server.py 9000   (para usar outra porta)
Para parar: Ctrl+C ou feche a janela.
"""
import http.server
import json
import os
import re
import sys
import threading
import webbrowser
from urllib.parse import urlparse

BASE = os.path.dirname(os.path.abspath(__file__))
FONTS_DIR = os.path.join(BASE, "fonts")
EXTENSOES = (".ttf", ".otf", ".woff", ".woff2")
PORTA_INICIAL = int(sys.argv[1]) if len(sys.argv) > 1 else int(os.environ.get("PORT", 8000))


def nome_da_fonte(arquivo):
    """GreatVibes-Regular.ttf -> 'Great Vibes'; minha_fonte.otf -> 'minha fonte'."""
    nome = os.path.splitext(arquivo)[0]
    nome = re.sub(r"[-_ ]?Regular$", "", nome, flags=re.I)
    nome = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", nome)  # separa CamelCase
    nome = re.sub(r"[_\-]+", " ", nome)
    nome = re.sub(r"[\"'<>&]", "", nome).strip()  # evita caracteres que quebram o HTML
    return nome or arquivo


def listar_fontes():
    fontes = []
    if not os.path.isdir(FONTS_DIR):
        return fontes
    for raiz, pastas, arquivos in os.walk(FONTS_DIR):
        pastas.sort()
        for arq in sorted(arquivos):
            if not arq.lower().endswith(EXTENSOES):
                continue
            caminho = os.path.join(raiz, arq)
            rel = os.path.relpath(caminho, BASE).replace(os.sep, "/")
            sub = os.path.relpath(raiz, FONTS_DIR)
            cat = "Minhas fontes" if sub == "." else sub.split(os.sep)[0]
            fontes.append({"name": nome_da_fonte(arq), "cat": cat, "file": rel})
    return fontes


class Handler(http.server.SimpleHTTPRequestHandler):
    extensions_map = {
        **http.server.SimpleHTTPRequestHandler.extensions_map,
        ".js": "text/javascript",
        ".woff2": "font/woff2",
        ".woff": "font/woff",
        ".otf": "font/otf",
        ".ttf": "font/ttf",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE, **kwargs)

    def do_GET(self):
        if urlparse(self.path).path == "/api/fontes":
            corpo = json.dumps(listar_fontes(), ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(corpo)))
            self.end_headers()
            self.wfile.write(corpo)
            return
        super().do_GET()

    def end_headers(self):
        # sem cache: ao editar fontes.js / index.html, o F5 já mostra a mudança
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        # mostra só erros, para a janela ficar limpa
        if len(args) > 1 and str(args[1]).startswith(("4", "5")):
            super().log_message(fmt, *args)


def main():
    servidor = None
    for porta in range(PORTA_INICIAL, PORTA_INICIAL + 10):
        try:
            servidor = http.server.ThreadingHTTPServer(("127.0.0.1", porta), Handler)
            break
        except OSError:
            print(f"Porta {porta} ocupada, tentando a próxima...")
    if servidor is None:
        print("Não foi possível abrir nenhuma porta. Feche outras janelas do painel e tente de novo.")
        sys.exit(1)

    url = f"http://localhost:{servidor.server_address[1]}"
    print()
    print("  Painel de Gravações rodando em:", url)
    print(f"  Fontes detectadas na pasta 'fonts': {len(listar_fontes())}")
    print("  Para encerrar: Ctrl+C ou feche esta janela.")
    print()
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
    finally:
        servidor.server_close()


if __name__ == "__main__":
    main()
