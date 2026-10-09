import tkinter as tk
from tkinter import messagebox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Python")
        self.root.geometry("300x450")
        self.root.configure(bg="#2c3e50")

        self.equacao = ""
        self.display_var = tk.StringVar()

        # --- Tela de Exibição ---
        self.tela = tk.Entry(
            root, 
            textvariable=self.display_var, 
            font=("Arial", 24), 
            bg="#ecf0f1", 
            fg="#2c3e50", 
            borderwidth=10, 
            relief="flat", 
            justify="right"
        )
        self.tela.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=20)

        # --- Configuração dos Botões ---
        botoes = [
            'C', '(', ')', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '=', ''
        ]

        # Estilo base (sem o 'bg' para podermos customizar individualmente)
        estilo_base = {
            "font": ("Arial", 14, "bold"),
            "fg": "#ffffff",
            "borderwidth": 0,
            "activebackground": "#1abc9c",
            "cursor": "hand2"
        }

        linha = 1
        coluna = 0

        for botao in botoes:
            if botao == "": continue
            
            # Lógica de cores e comandos
            cor_padrao = "#34495e"
            comando = lambda x=botao: self.clicar(x)

            if botao == "=":
                cor_padrao = "#e67e22" # Laranja
                comando = self.calcular
            elif botao == "C":
                cor_padrao = "#e74c3c" # Vermelho
                comando = self.limpar
            elif botao in ['/', '*', '-', '+']:
                cor_padrao = "#5dade2" # Azul para operadores

            # Criar o botão usando o estilo base + a cor definida
            btn = tk.Button(
                root, 
                text=botao, 
                bg=cor_padrao, 
                command=comando,
                **estilo_base
            )

            btn.grid(row=linha, column=coluna, sticky="nsew", padx=2, pady=2)
            
            coluna += 1
            if coluna > 3:
                coluna = 0
                linha += 1

        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
        for i in range(1, 6):
            root.grid_rowconfigure(i, weight=1)

    def clicar(self, char):
        self.equacao += str(char)
        self.display_var.set(self.equacao)

    def limpar(self):
        self.equacao = ""
        self.display_var.set("")

    def calcular(self):
        try:
            # Avalia a expressão matemática
            resultado = str(eval(self.equacao))
            self.display_var.set(resultado)
            self.equacao = resultado
        except ZeroDivisionError:
            messagebox.showerror("Erro", "Divisão por zero!")
            self.limpar()
        except Exception:
            messagebox.showerror("Erro", "Expressão Inválida")
            self.limpar()

if __name__ == "__main__":
    root = tk.Tk()
    Calculadora(root)
    root.mainloop()
    