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

![image](https://github.com/Viny-Pereira/requisicao_pluvial_ana/assets/121204240/96b18fd0-a60f-4b18-afd5-39f20fb9ed98)


- Inserir ID do reservatorio (Obtido no Site da ANA)
- Inserir data de inicio da análise (Não inserir, pega desde a primeira coleta cadastrada)
- Inserir data de fim da análise (Não inserir, pega até a ultima coleta cadastrada)
- Selecionar o tipo de dados (Cotas/Chuvas/Vazões)
- Selecionar Nível de consistência (Bruto (Padrão)/Consistido)

- Clicar em obter dados salvar
- Salvar no local e com nome desejado

### Opcao 02

- Se preferir trabalhar sem interface é possivel executar diretamente o arquivo dados_requisicao.py

- Editar os valores segundo o que deseja, dentro do __name__ = "__main__"


## Saida
- Ambas as formas terão como retorno um arquivo .csv


## Executável

- Dentro da pasta dist existe o arquivo main.exe, que pode ser executado sem a presença do python. 
