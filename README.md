# Requisicao API dados historicos fluvial ANA

## Site base
- Requisicao do site: https://dadosabertos.ana.gov.br/documents/fb3426be2d4a4f9abfa90fb87b30bd4f/about
- Fornece os dados históricos disponiveis no site da ANA, por meio de requisição HTTP

## Modulos necessários
- tkinter
- requests
- csv
- xml.etree.ElementTree

## Comandos necessários para utilização
```
pip install -r requirements.txt
```

## Tutorial
- Executar interface.py

- Inserir ID do reservatorio (Obtido no Site da ANA)
- Inserir data de inicio da análise (Não inserir, pega desde a primeira coleta cadastrada)
- Inserir data de fim da análise (Não inserir, pega até a ultima coleta cadastrada)
- Selecionar o tipo de dados (Cotas/Chuvas/Vazões)
- Selecionar Nível de consistência (Bruto/Consistido)
