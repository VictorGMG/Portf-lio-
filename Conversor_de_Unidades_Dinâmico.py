import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

janela = ctk.CTk()
janela.geometry("500x400") # Aumentei um pouco a janela para caber tudo
janela.title("Conversor De Unidades")

def acao_botao():
    medida_digitada = float(medida.get())
    if medida_digitada:
        print(f'Medidas Recebida: {medida_digitada}')
        polegada =  medida_digitada  / 2.54
        metro =  medida_digitada / 100

        label_satus = ctk.CTkLabel(janela,text=f'O Comprimento {medida_digitada}cm Fica {polegada:.2f} em polegadas e {metro} em metros')
        label_satus.pack(pady=10)
        
    else:
        print("Digite A Medida Que Deseja Converter ")

lebel_medida = ctk.CTkLabel(janela, text="Digite Uma Medeida Em Cm: ")
lebel_medida.pack(pady=(20, 5))

medida = ctk.CTkEntry(janela, placeholder_text="Digite A medida em Cm Que Deseja Converter", width=200)
medida.pack(pady=10)
        

botao = ctk.CTkButton(janela, text='Enviar medidas', command=acao_botao)
botao.pack(pady=10)

janela.mainloop()