import customtkinter as ctk
import pyautogui

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry("500x400") 
janela.title("Lista De Tarefa ")


def acao_botao() :
    tarefa_digitada = enttrada.get()
    tarefa_label = ctk.CTkCheckBox(janela, text=f"{tarefa_digitada}")
    tarefa_label.pack(pady = 40)
    
    
    
nome_tela =  ctk.CTkLabel(janela, text= "Minhas Tarefas ", fg_color="RED", text_color="black")
nome_tela.pack(pady= 10)

enttrada = ctk.CTkEntry(janela, placeholder_text="Digite a Tarefa Que Deseja Adicionar A Lista: ", width = 270)
enttrada.pack(pady= 20, padx= 100)


botao = ctk.CTkButton(janela, text='Enviar medidas', fg_color="blue", border_color="black", text_color="Black", command=acao_botao )
botao.pack(pady=30)


janela.mainloop()   


def checkbox_event():
    print("checkbox toggled, current value:", check_var.get())

check_var = customtkinter.StringVar(value="on")
checkbox = customtkinter.CTkCheckBox(app, text="CTkCheckBox", command=checkbox_event,
                                     variable=check_var, onvalue="on", offvalue="off")

lista_frame = ctk.CTkScrollableFrame(
    master=janela, 
    width=400, 
    height=200, 
    label_text="Tarefas Pendentes" 
)
lista_frame.pack(pady=20, padx=20)