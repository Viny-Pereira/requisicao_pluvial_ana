import requests
import csv
import xml.etree.ElementTree as ET

class DadosRequisicao:
    def obter_dados_hidrologicos(self, cod_estacao, data_inicio, data_fim,tipo_dados=2,nivel_consistencia = 1, nome_arquivo_saida="dados_hidrologicos"):
        url = f"https://telemetriaws1.ana.gov.br/ServiceANA.asmx/HidroSerieHistorica?codEstacao={cod_estacao}&dataInicio={data_inicio}&dataFim={data_fim}&tipoDados={tipo_dados}&nivelConsistencia={nivel_consistencia}"

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
            nome_arquivo_saida = f"{nome_arquivo_saida}"

            # Escrever os dados para o arquivo de saída especificado
            with open(nome_arquivo_saida, "w", newline="") as csvfile:
                fieldnames = data_list[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data_list)

            return nome_arquivo_saida
        else:
            return f"Erro: A solicitação GET não foi bem-sucedida. Código de status: {response.status_code}"


if __name__ == "__main__":
    cod_estacao = "00539053"
    data_inicio = ""
    data_fim = ""
    tipo_dados = 2  # Tipo de dados (por exemplo, 2 para chuvas)
    nivel_consistencia = 1  # Nível de consistência (por exemplo, 1 para bruto)
    nome_arquivo_saida = "dados.csv"

    dados = DadosRequisicao()
    arquivo_saida = dados.obter_dados_hidrologicos(cod_estacao, data_inicio, data_fim,tipo_dados,nivel_consistencia, nome_arquivo_saida)
    print(f"Arquivo de saída: {arquivo_saida}")