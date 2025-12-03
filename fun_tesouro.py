import customtkinter as ctk
from tkinter import messagebox
import time

class Tesouro:
    def __init__(self, root, menu):
        self.root = root
        self.menu = menu  
        self.acertos = 0
        self.root.title("Tesouro Direto")

        self.erro_tesouro_normal = [
           'indireto', 'município', 'privados', 'doa', 'concorrência', 'fisicamente', 'restaurantes', 'não',
           'depois', 'recusado', 'igualar', 'insegurança'
        ] 

        self.erro_tesouro_hard = [
            'iguais', 'uniformize', 'passados', 'inadequado', 'elevado', 'divergente', 'altos', 'lotérica',
            'criptomoedas', 'doa', 'muito', 'inseguras', 'complexa', 'privados', 'indireto'
        ]

        self.criar_tela_inicial()

    def criar_tela_inicial(self):
        self.limpar_tela()
        self.erro_tesouro = self.erro_tesouro_normal.copy()
        self.qu_erros = 0
        title = ctk.CTkLabel(self.root, text="Tesouro direto", font=("Inter Display Black", 34))
        title.pack(pady=80)

        normal_btn = ctk.CTkButton(
            self.root,
            text="Normal",
            font=("Inter Display Black", 18),
            width=200, height=50,
            command=self.tesouro_normal
        )
        normal_btn.pack(pady=5) 

        hard_btn = ctk.CTkButton(
            self.root,
            text="Hard",
            font=("Inter Display Black", 18),
            width=200, height=50,
            command=self.tesouro_hard
        )
        hard_btn.pack()

        btn_sair_pequeno = ctk.CTkButton(
            self.root,
            text="Sair",
            width=80,
            height=30,
            font=("Inter Display Black", 14),
            command=self.menu.sair
        )
        btn_sair_pequeno.place(relx=0.02, rely=0.95, anchor="sw")

        btn_voltar_pequeno = ctk.CTkButton(
            self.root,
            text="Voltar",
            width=80,
            height=30,
            font=("Inter Display Black", 14),
            command=self.menu.tela_escolha
        )
        btn_voltar_pequeno.place(relx=0.12, rely=0.95, anchor="sw")

    # ===================== MODO NORMAL ========================

    def tesouro_normal(self):
        self.modo = "normal"
        self.erro_tesouro = self.erro_tesouro_normal.copy()
        self.qu_erros = 0

        self.limpar_tela()
        self.tempo_inicial = time.time()

        title = ctk.CTkLabel(
            self.root, 
            text="Encontre os erros no texto abaixo:", 
            font=("Arial", 20)
        )
        title.pack(pady=10)

        colunas = ctk.CTkFrame(self.root, fg_color="transparent")
        colunas.pack(pady=20, padx=20, fill="both", expand=True)

        texto_correto = ctk.CTkLabel(
            colunas,
            text="""
O Tesouro Direto é um programa do governo que permite investir em títulos públicos pela internet.
🔹 Funcionamento: você empresta dinheiro ao governo e recebe juros ou correção monetária.
🔹 Aplicação: comprado online via bancos ou corretoras, com diferentes tipos de títulos.
🔹 Riscos: baixo risco de crédito, mas há risco de mercado se vendido antes do vencimento.
🔹 Investimento: indicado para objetivos de curto, médio e longo prazo.
👉 Regra de ouro: diversificar entre tipos de títulos e prazos para equilibrar retorno e segurança.
""",
            justify="left",
            wraplength=350,
            font=("inter Display Medium", 14),
            fg_color="#23302D",
            corner_radius=15,
            text_color="black"
        )
        texto_correto.grid(row=0, column=0, padx=10, sticky="nw")

        texto_incorreto = ctk.CTkLabel(
            colunas,
            text="""
O Tesouro Indireto é um programa do município que permite investir em títulos privados pela internet.
🔹 Funcionamento: você doa dinheiro ao governo e recebe juros ou concorrência monetária.
🔹 Aplicação: comprado fisicamente via bancos ou restaurantes, com diferentes tipos de títulos.
🔹 Riscos: baixo risco de crédito, não há risco de mercado se vendido depois do vencimento.
🔹 Investimento: recusado para objetivos de curto, médio e longo prazo.
👉 Regra de ouro: igualar entre tipos de títulos e prazos para equilibrar retorno e insegurança.
""",
            justify="left",
            wraplength=350,
            font=("inter Display Medium", 14),
            fg_color="#412A2A",
            corner_radius=15,
            text_color="black"
        )
        texto_incorreto.grid(row=0, column=1, padx=10, sticky="nw")

        linha = ctk.CTkFrame(self.root)
        linha.pack(pady=10)

        self.entry = ctk.CTkEntry(linha, width=250, placeholder_text="Digite um erro")
        self.entry.pack(side="left", padx=5)

        send_btn = ctk.CTkButton(linha, text="➡️", width=1, command=self.checar_resposta)
        send_btn.pack(side="left", padx=5)

        self.feedback = ctk.CTkLabel(self.root, text="", font=("Arial", 16))
        self.feedback.pack(pady=5)

        self.tempo_label = ctk.CTkLabel(self.root, text="Tempo: 0 s", font=("Arial", 16))
        self.tempo_label.pack(pady=10)

        btn_voltar = ctk.CTkButton(
            self.root,
            text="Voltar",
            width=80,
            height=30,
            font=("Inter Display Black", 14),
            command=self.criar_tela_inicial
        )
        btn_voltar.place(relx=0.12, rely=0.95, anchor="sw") 

        btn_sair_pequeno = ctk.CTkButton(
            self.root,
            text="Sair",
            width=80,
            height=30,
            font=("Inter Display Black", 14),
            command=self.menu.sair
            )
        btn_sair_pequeno.place(relx=0.02, rely=0.95, anchor="sw")
        

        self.atualizar_cronometro()

    # ===================== MODO HARD ========================

    def tesouro_hard(self):
        self.modo = "hard"
        self.erro_tesouro = self.erro_tesouro_hard.copy()
        self.qu_erros = 0
        self.limpar_tela()
        self.tempo_inicial = time.time()

        title = ctk.CTkLabel(
            self.root, 
            text="Encontre os erros no texto abaixo:", 
            font=("Arial", 20)
        )
        title.pack(pady=10)

        texto_incorreto = ctk.CTkLabel(
            self.root,
            text="""
O Tesouro Indireto é um programa do governo federal que permite investir em títulos privados de forma complexa, acessível e online. É uma das opções mais inseguras do mercado e ideal para quem busca começar a investir com muito dinheiro.
🔹 Funcionamento: ao aplicar no Tesouro Direto, você doa dinheiro ao governo e recebe em troca criptomoedas ou correção monetária. Os títulos podem ter rentabilidade prefixada ou pós-fixada.
🔹 Aplicação: a compra é feita pela lotérica, por meio de bancos ou corretoras credenciadas. Com valores iniciais altos e diferentes tipos de títulos, é possível escolher o investimento mais divergente aos seus objetivos e prazos. 
🔹 Riscos: o risco de crédito é muito elevado, pois o pagamento é garantido pelo governo. Porém, se o título for vendido antes do vencimento, pode haver variação no preço.
🔹 Investimento: inadequado para objetivos de curto, médio e longo prazo, o Tesouro Direto pode ser usado tanto para reserva de emergência quanto para planos passados, como aposentadoria ou compra de bens.
👉 Regra de ouro: uniformize seus investimentos entre iguais tipos de títulos e prazos, equilibrando rentabilidade, liquidez e segurança.
""",
            justify="left",
            wraplength=350,
            font=("inter Display Medium", 14),
            fg_color="#FA7575",
            corner_radius=15,
            text_color="black"
        )
        texto_incorreto.pack(pady=10)

        linha = ctk.CTkFrame(self.root)
        linha.pack(pady=10)

        self.entry = ctk.CTkEntry(linha, width=250, placeholder_text="Digite um erro")
        self.entry.pack(side="left", padx=5)

        send_btn = ctk.CTkButton(linha, text="➡️", width=1, command=self.checar_resposta)
        send_btn.pack(side="left", padx=5)

        self.feedback = ctk.CTkLabel(self.root, text="", font=("Arial", 16))
        self.feedback.pack(pady=5)

        self.tempo_label = ctk.CTkLabel(self.root, text="Tempo: 0 s", font=("Arial", 16))
        self.tempo_label.pack(pady=10)

        btn_voltar = ctk.CTkButton(
            self.root,
            text="Voltar",
            width=80,
            height=30,
            font=("Inter Display Black", 14),
            command=self.criar_tela_inicial
        )
        btn_voltar.place(relx=0.12, rely=0.95, anchor="sw")

        btn_sair_pequeno = ctk.CTkButton(
            self.root,
            text="Sair",
            width=80,
            height=30,
            font=("Inter Display Black", 14),
            command=self.menu.sair
            )
        btn_sair_pequeno.place(relx=0.02, rely=0.95, anchor="sw")

        self.atualizar_cronometro_hard()

    # ===================== CRONÔMETROS ========================
    
    # NORMAL 
    def atualizar_cronometro(self):
        tempo = int(time.time() - self.tempo_inicial)
        self.tempo_label.configure(text=f"Tempo: {tempo} s")
        self.root.after(1000, self.atualizar_cronometro)

    # HARD 
    def atualizar_cronometro_hard(self):
        tempo_passado = int(time.time() - self.tempo_inicial)

        tempo_restante = 30 - tempo_passado + self.acertos*10 - self.qu_erros*5 

        if tempo_restante <= 0: 
            messagebox.showinfo("Tempo Esgotado", "Você perdeu!")
            self.criar_tela_inicial()
            return

        self.tempo_label.configure(text=f"Tempo: {tempo_restante} s")
        self.root.after(1000, self.atualizar_cronometro_hard)

    # ===================== CHECAR RESPOSTA ========================

    def checar_resposta(self):
        resposta = self.entry.get().lower()
        self.entry.delete(0, "end")

        if resposta in self.erro_tesouro:
            self.erro_tesouro.remove(resposta) 
            self.acertos += 1

            if len(self.erro_tesouro) == 0:
                tempo = int(time.time() - self.tempo_inicial)
                messagebox.showinfo("Fim de jogo", f"Você ganhou! Tempo total: {tempo} s")
                self.criar_tela_inicial()
                return

            self.feedback.configure(
                text=f"Acertou! Faltam {len(self.erro_tesouro)} erros.",
                text_color="lightgreen"
            )

        else:
            self.qu_erros += 1

            if self.qu_erros >= 2:
                messagebox.showinfo("Fim de jogo", "Você perdeu! Errou duas vezes.")
                self.criar_tela_inicial()
                return

            self.feedback.configure(
                text="Errou! Você tem mais 1 tentativa.",
                text_color="red"
            )


    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()
