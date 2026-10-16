# Painel de Gravações (protótipo)

Site local com duas abas: **Documentação** (padronização de gravações) e **Fontes** (como cada letra fica, preenchida).

## Arquivos

| Arquivo | Para quê |
|---|---|
| `index.html` | O site (visual e documentação) |
| `fontes.js` | **Lista de fontes — é aqui que você adiciona/remove fontes** |
| `server.py` | Servidor local (localhost) |
| `iniciar.bat` | Atalho para ligar o servidor no Windows |
| `fonts/` | Pasta para os arquivos de fonte da empresa |

## Como rodar

- **Windows:** dois cliques em `iniciar.bat`. Abre sozinho em http://localhost:8000 (precisa do Python instalado).
- **Terminal / VS Code:** na pasta do projeto, `python server.py` (no Windows pode ser `py server.py`).
- **Sem Python:** abra o `index.html` direto no navegador, ou use a extensão *Live Server* do VS Code. Nesse modo só vale a lista do `fontes.js`.

Para parar o servidor: `Ctrl+C` ou fechar a janela.

## Como adicionar uma fonte

**Jeito 1 – editar o `fontes.js` no VS Code** (funciona em qualquer modo):

```js
{name:"Cinzel", cat:"Serifada"},                                  // Google Fonts (precisa de internet)
{name:"Minha Fonte", cat:"Script", file:"fonts/MinhaFonte.ttf"},  // arquivo da empresa
```

Salve e atualize a página (F5).

**Jeito 2 – soltar o arquivo na pasta `fonts/`** (só com o servidor rodando): ele aparece sozinho após F5. Subpastas viram categorias (`fonts/Script/Allura.ttf` → categoria "Script"). O nome vem do arquivo (`GreatVibes-Regular.ttf` → "Great Vibes").

## Como editar a documentação

Edite o texto dentro de `<article id="article">` no `index.html`. Os valores atuais são só exemplos.
O checklist fica na lista `ITENS`, no final do `index.html`.
