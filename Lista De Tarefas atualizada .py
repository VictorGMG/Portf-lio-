import customtkinter as ctk

class AppTarefa(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Lista de Tarefas Pro 2026")
        self.geometry("500x450")
        ctk.set_appearance_mode("dark")

        self.label_titulo = ctk.CTkLabel(self, text="Minhas Tarefas", font=("Arial", 20, "bold"))
        self.label_titulo.pack(pady=20)

        self.frame_input = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_input.pack(pady=10)

        self.entrada_tarefa = ctk.CTkEntry(self.frame_input, placeholder_text="O que precisa fazer?", width=300)
        self.entrada_tarefa.pack(side="left", padx=10)

        self.botao_add = ctk.CTkButton(self.frame_input, text="Adicionar", width=80, command=self.adicionar_tarefa)
        self.botao_add.pack(side="left")

        self.lista_frame = ctk.CTkScrollableFrame(self, width=400, height=200, label_text="Tarefas Pendentes")
        self.lista_frame.pack(pady=20, padx=20)

        self.botao_limpar = ctk.CTkButton(self, text="Limpar Todas as Tarefas", fg_color="red", hover_color="#8B0000", command=self.limpar_lista)
        self.botao_limpar.pack(pady=10)

    def adicionar_tarefa(self):
        texto = self.entrada_tarefa.get()
        if texto != "":
            nova_tarefa = ctk.CTkCheckBox(self.lista_frame, text=texto)
            nova_tarefa.pack(pady=5, padx=10, anchor="w") 
            self.entrada_tarefa.delete(0, 'end')
        else:
            self.entrada_tarefa.configure(placeholder_text_color="red")

    def limpar_lista(self):
        for widget in self.lista_frame.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = AppTarefa()
    app.mainloop()
