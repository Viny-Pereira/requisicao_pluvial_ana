import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from dados_requisicao import DadosRequisicao
import webbrowser

class InterfaceUsuario:
    def __init__(self, root, dados_requisicao):
        self.root = root
        self.root.title("Obter Dados Hidrológicos")

        # Defina o tamanho da janela e centralize-a na tela
        largura_janela = 400
        altura_janela = 350
        largura_tela = root.winfo_screenwidth()
        altura_tela = root.winfo_screenheight()
        x = (largura_tela - largura_janela) // 2
        y = (altura_tela - altura_janela) // 2
        root.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

        self.dados_requisicao = dados_requisicao

        self.cod_estacao_label = tk.Label(root, text="Código da Estação:")
        self.cod_estacao_label.pack()

        self.cod_estacao_entry = tk.Entry(root)
        self.cod_estacao_entry.pack()

        self.data_inicio_label = tk.Label(root, text="Data de Início (dd/mm/yyyy):")
        self.data_inicio_label.pack()

        self.data_inicio_entry = tk.Entry(root)
        self.data_inicio_entry.pack()

        self.data_fim_label = tk.Label(root, text="Data de Fim (dd/mm/yyyy):")
        self.data_fim_label.pack()

        self.data_fim_entry = tk.Entry(root)
        self.data_fim_entry.pack()

        # ComboBox para selecionar o tipo de dados
        self.tipo_dados_label = tk.Label(root, text="Tipo de Dados:")
        self.tipo_dados_label.pack()
        # Adicione os valores de exibição e correspondência interna
        tipo_dados_valores = ["Cotas", "Chuvas", "Vazões"]
        self.tipo_dados_combobox = ttk.Combobox(root, values=tipo_dados_valores)
        self.tipo_dados_combobox.pack()

        # ComboBox para selecionar o nível de consistência
        self.nivel_consistencia_label = tk.Label(root, text="Nível de Consistência:")
        self.nivel_consistencia_label.pack()
        # Adicione os valores de exibição e correspondência interna
        nivel_consistencia_valores = ["1", "2"]
        self.nivel_consistencia_combobox = ttk.Combobox(root, values=nivel_consistencia_valores)
        self.nivel_consistencia_combobox.pack()

        self.obter_dados_button = tk.Button(root, text="Obter Dados e Salvar CSV", command=self.obter_dados_e_salvar)
        self.obter_dados_button.pack(pady=10)

        self.mensagem_label = tk.Label(root, text="")
        self.mensagem_label.pack()

        # Rótulo "Sobre"
        self.sobre_label = tk.Label(root, text="Sobre | Feito por Viny Pereira.", font=("Arial", 8), fg="black")
        self.sobre_label.pack(side="bottom", fill="x")
        self.sobre_label.bind("<Button-1>", self.abrir_link_repositorio)

        # Rótulo "Saiba mais"
        self.saiba_mais_label = tk.Label(root, text="Saiba mais", font=("Arial", 8), fg="blue", cursor="hand2")
        self.saiba_mais_label.pack(side="bottom", fill="x")
        self.saiba_mais_label.bind("<Button-1>", self.abrir_link_repositorio)

    def obter_dados_e_salvar(self):
        cod_estacao = self.cod_estacao_entry.get()
        data_inicio = self.data_inicio_entry.get()
        data_fim = self.data_fim_entry.get()

        # Obter os valores selecionados das ComboBoxes
        tipo_dados = self.tipo_dados_combobox.get()
        nivel_consistencia = self.nivel_consistencia_combobox.get() or "1"  # Define 1 como padrão se nenhum valor for selecionado

        # Mapeie os valores de exibição para correspondência interna
        tipo_dados_mapeamento = {
            "Cotas": "1",
            "Chuvas": "2",
            "Vazões": "3"
        }
        tipo_dados = tipo_dados_mapeamento.get(tipo_dados, tipo_dados)

        dados_requisicao = DadosRequisicao()

        # Abre a caixa de diálogo para escolher a pasta e o nome do arquivo
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Arquivos CSV", "*.csv")])

        if file_path:
            resultado = dados_requisicao.obter_dados_hidrologicos(cod_estacao, data_inicio, data_fim, tipo_dados, nivel_consistencia, nome_arquivo_saida=file_path)
            if resultado and resultado.endswith(".csv"):
                mensagem = f"Os dados foram salvos em '{resultado}'."
            else:
                mensagem = resultado
        else:
            mensagem = "Operação de salvamento cancelada pelo usuário."

        self.mensagem_label.config(text=mensagem)

    def abrir_link_repositorio(self, event):
        webbrowser.open("https://github.com/Viny-Pereira/requisicao_pluvial_ana")

if __name__ == "__main__":
    root = tk.Tk()
    dados_requisicao = DadosRequisicao()
    app = InterfaceUsuario(root, dados_requisicao)
    root.mainloop()
