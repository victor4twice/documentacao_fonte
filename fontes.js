/* ============================================================
   LISTA DE FONTES  —  edite este arquivo no VS Code e salve.
   Depois é só atualizar a página (F5) no navegador.

   COMO ADICIONAR UMA FONTE
   ------------------------------------------------------------
   1) Fonte do Google Fonts (precisa de internet):
        {name:"Cinzel", cat:"Serifada"},
      O "name" tem que ser igual ao nome no site fonts.google.com.

   2) Fonte da empresa (arquivo .ttf, .otf, .woff ou .woff2):
      coloque o arquivo na pasta "fonts" e escreva:
        {name:"Minha Fonte", cat:"Script", file:"fonts/MinhaFonte.ttf"},

   3) Automático (só com o servidor, iniciar.bat / server.py):
      basta soltar o arquivo da fonte dentro da pasta "fonts".
      Se colocar numa subpasta, o nome da subpasta vira a categoria:
        fonts/Script/Allura.ttf  ->  categoria "Script"
      Não precisa editar este arquivo nesse caso.

   COMO REMOVER: apague a linha (ou coloque // na frente).
   CATEGORIA: pode ser qualquer texto; as categorias do filtro
   são criadas automaticamente a partir daqui.
   ============================================================ */

const FONTES = [

  // ---------- Sem serifa ----------
  {name:"Montserrat", cat:"Sem serifa"},
  {name:"Roboto", cat:"Sem serifa"},
  {name:"Raleway", cat:"Sem serifa"},
  {name:"Oswald", cat:"Sem serifa"},
  {name:"Bebas Neue", cat:"Sem serifa"},

  // ---------- Serifada ----------
  {name:"Playfair Display", cat:"Serifada"},
  {name:"Cinzel", cat:"Serifada"},
  {name:"Libre Baskerville", cat:"Serifada"},
  {name:"Lora", cat:"Serifada"},

  // ---------- Script / cursiva ----------
  {name:"Great Vibes", cat:"Script"},
  {name:"Dancing Script", cat:"Script"},
  {name:"Allura", cat:"Script"},
  {name:"Alex Brush", cat:"Script"},
  {name:"Parisienne", cat:"Script"},
  {name:"Satisfy", cat:"Script"},
  {name:"Pacifico", cat:"Script"},

  // ---------- Decorativa ----------
  {name:"Abril Fatface", cat:"Decorativa"},
  {name:"Lobster", cat:"Decorativa"},
  {name:"Special Elite", cat:"Decorativa"},

  // ---------- Fontes da empresa (exemplo — tire o // para usar) ----------
  // {name:"Minha Fonte", cat:"Script", file:"fonts/MinhaFonte.ttf"},

];
