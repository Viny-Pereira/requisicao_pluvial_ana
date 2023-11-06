import requests
import csv
import xml.etree.ElementTree as ET

class DadosRequisicao:
    def obter_dados_hidrologicos(self, cod_estacao, data_inicio, data_fim, nome_arquivo_saida="dados_hidrologicos"):
        url = f"https://telemetriaws1.ana.gov.br/ServiceANA.asmx/HidroSerieHistorica?codEstacao={cod_estacao}&dataInicio={data_inicio}&dataFim={data_fim}&tipoDados=2&nivelConsistencia=1"

        # Realizar a solicitação HTTP GET
        response = requests.get(url)

        if response.status_code == 200:
            # Ler o conteúdo da resposta como XML
            xml_data = response.text

            # Analisar o XML
            try:
                root = ET.fromstring(xml_data)
            except ET.ParseError as e:
                return f"Erro ao analisar XML: {str(e)}"

            # Verificar se o XML contém um <Error>
            error_element = root.find(".//Error")
            if error_element is not None:
                error_message = error_element.text
                return f"Erro: {error_message}"

            # Extrair dados XML para uma lista de dicionários
            data_list = []
            for record in root.iter("SerieHistorica"):
                data = {}
                for element in record:
                    data[element.tag] = element.text
                data_list.append(data)

            # Acrescentar a extensão .csv ao nome do arquivo de saída
            nome_arquivo_saida = f"{nome_arquivo_saida}.csv"

            # Escrever os dados para o arquivo de saída especificado
            with open(nome_arquivo_saida, "w", newline="") as csvfile:
                fieldnames = data_list[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data_list)

            return nome_arquivo_saida
        else:
            return f"Erro: A solicitação GET não foi bem-sucedida. Código de status: {response.status_code}"
