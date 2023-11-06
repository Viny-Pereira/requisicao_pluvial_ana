import tkinter as tk
from dados_requisicao import DadosRequisicao

class InterfaceUsuario:
    def __init__(self, root, dados_requisicao):
        self.root = root
        self.root.title("Obter Dados Hidrológicos")

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

        self.obter_dados_button = tk.Button(root, text="Obter Dados e Salvar CSV", command=self.obter_dados_e_salvar)
        self.obter_dados_button.pack(pady=10)

        self.mensagem_label = tk.Label(root, text="")
        self.mensagem_label.pack()

    def obter_dados_e_salvar(self):
        cod_estacao = self.cod_estacao_entry.get()
        data_inicio = self.data_inicio_entry.get()
        data_fim = self.data_fim_entry.get()

        dados_requisicao = DadosRequisicao()
        resultado = dados_requisicao.obter_dados_hidrologicos(cod_estacao, data_inicio, data_fim)

        if resultado and resultado.endswith(".csv"):
            mensagem = f"Os dados foram salvos em '{resultado}'."
        else:
            mensagem = resultado

        self.mensagem_label.config(text=mensagem)

if __name__ == "__main__":
    root = tk.Tk()
    dados_requisicao = DadosRequisicao()
    app = InterfaceUsuario(root, dados_requisicao)
    root.mainloop()