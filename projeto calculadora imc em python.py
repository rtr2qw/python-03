mport tkinter as tk

def calcular_imc():
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    peso = float(entry_peso.get())
    altura_cm = float(entry_altura.get())
    
    # Converter altura para metros
    altura_m = altura_cm / 100
    
    # Calcular IMC
    imc = peso / (altura_m ** 2)
    
    # Exibir resultado
    resultado.config(text=f"Nome: {nome}\nEndereço: {endereco}\nIMC: {imc:.2f}")

# Criar a janela
janela = tk.Tk()
janela.title("Calculadora de IMC")

# Criar widgets
label_nome = tk.Label(janela, text="Nome:")
label_endereco = tk.Label(janela, text="Endereço:")
label_peso = tk.Label(janela, text="Peso (kg):")
label_altura = tk.Label(janela, text="Altura (cm):")
entry_nome = tk.Entry(janela)
entry_endereco = tk.Entry(janela)
entry_peso = tk.Entry(janela)
entry_altura = tk.Entry(janela)
botao_calcular = tk.Button(janela, text="Calcular IMC", command=calcular_imc)
resultado = tk.Label(janela, text="Resultado: ")

# Organizar widgets na janela
label_nome.grid(row=0, column=0)
entry_nome.grid(row=0, column=1)
label_endereco.grid(row=1, column=0)
entry_endereco.grid(row=1, column=1)
label_peso.grid(row=2, column=0)
entry_peso.grid(row=2, column=1)
label_altura.grid(row=3, column=0)
entry_altura.grid(row=3, column=1)
botao_calcular.grid(row=4, column=0, columnspan=2)
resultado.grid(row=5, column=0, columnspan=2)

# Iniciar a interface gráfica
janela.mainloop()