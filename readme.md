# Configurar
### Baixar o driver para o Google Chrome v 114
https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/

para windows ou outro OS https://chromedriver.chromium.org/downloads

Instale o python 3 e o Pip

Informe os dados abaixo no arquivo `send.py`

### LNDg Credentials
lndg_url = "http://192.168.0.63:8889/"
lndg_user = "lndg-admin"
lndg_pass = "PASSWORD"

### Umbrel Credentials
umbrel_login_url = "http://192.168.0.63:8889/"
umbrel_pass = "PASSWORD"

# Executar
execute o scraping com `python ambos.py`
execute o sender com `python send.py`

Você pode parar o scraping a qualquer momento, ele irá gravar um arquivo chamado lista.txt, o send irá usar esse arquivo e gerará um chamado success.txt para os peers que tiverem sucesso.