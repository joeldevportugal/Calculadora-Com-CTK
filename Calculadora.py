import customtkinter

def btn_click(item):
    """Adiciona o número ou operador selecionado ao campo de entrada."""
    global expression
    expression += str(item)
    EEcra.delete(0, customtkinter.END)
    EEcra.insert(customtkinter.END, expression)


def clear():
    """Limpa o campo de entrada."""
    global expression
    expression = ""
    EEcra.delete(0, customtkinter.END)


def backspace():
    """Remove o último caractere do campo de entrada."""
    global expression
    expression = expression[:-1]
    EEcra.delete(0, customtkinter.END)
    EEcra.insert(customtkinter.END, expression)


def calculate():
    """Calcula a expressão inserida e atualiza o campo de entrada com o resultado."""
    global expression
    try:
        result = str(eval(expression))
        EEcra.delete(0, customtkinter.END)
        EEcra.insert(customtkinter.END, result)
    except Exception as e:
        clear()
        EEcra.insert(customtkinter.END, f"Erro: {e}")



def button_percent():
    """Calcula a porcentagem do primeiro número em EEcra e insere o resultado."""
    first_number = EEcra.get()
    
    try:
        # Avalia a expressão matemática
        eval_result = eval(first_number)
        if isinstance(eval_result, (int, float)):
            # Verifica se o resultado é um número
            percentage = eval_result / 100
            EEcra.delete(0, customtkinter.END)
            EEcra.insert(0, str(percentage))  # Insere a porcentagem no início
            
            # Impressão do valor de first_number quando a expressão é avaliada com sucesso
            #print("Valor de first_number:", first_number)
        else:
            EEcra.delete(0, customtkinter.END)
            EEcra.insert(0, "")  # Removendo a mensagem de erro
    except Exception:
        # Trata qualquer exceção que possa ocorrer durante a avaliação da expressão
        EEcra.delete(0, customtkinter.END)
        EEcra.insert(0, "")  # Removendo a mensagem de erro

def toggle_buttons_visibility():
    """Alterna a visibilidade dos botões."""
    global buttons_visible
    if buttons_visible:
        # Esconde os botões
        buttons_visible = False
        hide_buttons()
    else:
        # Mostra os botões
        buttons_visible = True
        show_buttons()

def hide_buttons():
    """Esconde os botões."""
    Btnclear.place_forget()
    btnBack.place_forget()
    btnModulo.place_forget()
    btnMul.place_forget()
    btnDiv.place_forget()
    btnSub.place_forget()
    btnSoma.place_forget()
    btnSete.place_forget()
    btnOito.place_forget()
    btnNove.place_forget()
    btnQuatro.place_forget()
    btnCinco.place_forget()
    btnSeis.place_forget()
    btnUM.place_forget()
    btnDois.place_forget()
    btnTres.place_forget()
    btnZero.place_forget()
    btnDecimal.place_forget()
    btnIgual.place_forget()

def show_buttons():
    """Mostra os botões."""
    Btnclear.place(x=10, y=42)
    btnBack.place(x=64, y=42)
    btnModulo.place(x=10, y=72)
    btnMul.place(x=64, y=72)
    btnDiv.place(x=163, y=72)
    btnSub.place(x=230, y=72)
    btnSoma.place(x=230, y=102)
    btnSete.place(x=10, y=102)
    btnOito.place(x=64, y=102)
    btnNove.place(x=163, y=102)
    btnQuatro.place(x=10, y=132)
    btnCinco.place(x=64, y=132)
    btnSeis.place(x=163, y=132)
    btnUM.place(x=10, y=162)
    btnDois.place(x=64, y=162)
    btnTres.place(x=163, y=162)
    btnZero.place(x=10, y=192)
    btnDecimal.place(x=64, y=192)
    btnIgual.place(x=163, y=192)        

# Inicializar a expressão globalmente para armazenar os inputs do usuário
expression = ""

# configurar a janela ---------------------------------------------------------------------
janela = customtkinter.CTk()
janela.geometry('300x270+100+100')
janela.resizable(False, False)
janela.title('Calc Dev Joel 2024 PT ©')
janela.config(bg='White')
janela.iconbitmap('C:\\Users\HP\\Desktop\\Python customtkinter\\Calculadora\\icon.ico')
#------------------------------------------------------------------------------------------
# criar O Ecra ----------------------------------------------------------------------------
EEcra= customtkinter.CTkEntry(janela, width=280, bg_color='white')
EEcra.place(x=10, y=10)
EEcra.configure(justify="right",font=("Arial", 14, 'bold'))
#------------------------------------------------------------------------------------------
# criar Os Botões -------------------------------------------------------------------------
Btnclear = customtkinter.CTkButton(janela, text='C', width=50, font=("Arial", 12, 'bold'),bg_color='white')
Btnclear.place(x=10,y=42)

btnBack = customtkinter.CTkButton(janela, text='←', width=95,font=("Arial", 12, 'bold'),bg_color='white')
btnBack.place(x=64,y=42)

BtnON = customtkinter.CTkButton(janela, text='ON', width=65, font=("Arial", 12, 'bold'),bg_color='white')
BtnON.place(x=163,y=42)

btnOFF = customtkinter.CTkButton(janela, text='OFF', width=55,font=("Arial", 12, 'bold'),bg_color='white')
btnOFF.place(x=230,y=42)

btnModulo = customtkinter.CTkButton(janela, text='%', width=50,font=("Arial", 12, 'bold'),bg_color='white')
btnModulo.place(x=10,y=72)

btnMul = customtkinter.CTkButton(janela, text='X', width=95,font=("Arial", 12, 'bold'),bg_color='white')
btnMul.place(x=64,y=72)

btnDiv = customtkinter.CTkButton(janela, text='/', width=65, font=("Arial", 12, 'bold'),bg_color='white')
btnDiv.place(x=163,y=72)

btnSub = customtkinter.CTkButton(janela, text='-', width=55, font=("Arial", 12, 'bold'),bg_color='white')
btnSub.place(x=230,y=72)

btnSete = customtkinter.CTkButton(janela, text='7', width=50,font=("Arial", 12, 'bold'),bg_color='white')
btnSete.place(x=10,y=102)

btnOito = customtkinter.CTkButton(janela, text='8', width=95,font=("Arial", 12, 'bold'),bg_color='white')
btnOito.place(x=64,y=102)

btnNove = customtkinter.CTkButton(janela, text='9', width=65,font=("Arial", 12, 'bold'),bg_color='white')
btnNove.place(x=163,y=102)

btnSoma = customtkinter.CTkButton(janela, text='+', width=55, height=117,font=("Arial", 12, 'bold'),bg_color='white')
btnSoma.place(x=230,y=102)

btnQuatro = customtkinter.CTkButton(janela, text='4', width=50, font=("Arial", 12, 'bold'),bg_color='white')
btnQuatro.place(x=10,y=132)

btnCinco = customtkinter.CTkButton(janela, text='5', width=95, font=("Arial", 12, 'bold'),bg_color='white')
btnCinco.place(x=64,y=132)

btnSeis = customtkinter.CTkButton(janela, text='6', width=65, font=("Arial", 12, 'bold'),bg_color='white')
btnSeis.place(x=163,y=132)

btnUM = customtkinter.CTkButton(janela, text='1', width=50, font=("Arial", 12, 'bold'),bg_color='white')
btnUM.place(x=10,y=162)

btnDois = customtkinter.CTkButton(janela, text='2', width=95, font=("Arial", 12, 'bold'),bg_color='white')
btnDois.place(x=64,y=162)

btnTres = customtkinter.CTkButton(janela, text='3', width=65, font=("Arial", 12, 'bold'),bg_color='white')
btnTres.place(x=163,y=162)

btnZero = customtkinter.CTkButton(janela, text='0', width=50, font=("Arial", 12, 'bold'),bg_color='white')
btnZero.place(x=10,y=192)

btnDecimal = customtkinter.CTkButton(janela, text=',', width=95, font=("Arial", 12, 'bold'),bg_color='white')
btnDecimal.place(x=64,y=192)

btnIgual = customtkinter.CTkButton(janela, text='=', width=65, font=("Arial", 12, 'bold'),bg_color='white')
btnIgual.place(x=163,y=192)
#----------------------------------------------------------------------------------------------
# criar a Label Autor -------------------------------------------------------------------------
LAutor = customtkinter.CTkLabel(janela, text='Dev Joel Portugal 2024 ©', font=("Arial", 20, 'bold'),bg_color='white')
LAutor.place(x=10, y=232)
#----------------------------------------------------------------------------------------------
# aqui vamos ficar os comandos para Ligar as funçoes ------------------------------------------
# Agora, atualizamos os botões para chamar as funções correspondentes
Btnclear.configure(command=lambda: clear())
btnBack.configure(command=lambda: backspace())
BtnON.configure(command=lambda: show_buttons()) 
btnOFF.configure(command=lambda: hide_buttons())
# Defina os comandos para os botões numéricos e operadores
btnModulo.configure(command=lambda: button_percent())
btnMul.configure(command=lambda: btn_click('*'))  # Use '*' como operador de multiplicação
btnDiv.configure(command=lambda: btn_click('/'))
btnSub.configure(command=lambda: btn_click('-'))
btnSoma.configure(command=lambda: btn_click('+'))
btnSete.configure(command=lambda: btn_click('7'))
btnOito.configure(command=lambda: btn_click('8'))
btnNove.configure(command=lambda: btn_click('9'))
btnQuatro.configure(command=lambda: btn_click('4'))
btnCinco.configure(command=lambda: btn_click('5'))
btnSeis.configure(command=lambda: btn_click('6'))
btnUM.configure(command=lambda: btn_click('1'))
btnDois.configure(command=lambda: btn_click('2'))
btnTres.configure(command=lambda: btn_click('3'))
btnZero.configure(command=lambda: btn_click('0'))
btnDecimal.configure(command=lambda: btn_click('.'))
btnIgual.configure(command=calculate)
#----------------------------------------------------------------------------------------------
# vamos Iniciar a Nossa Janela ----------------------------------------------------------------
janela.mainloop()
#----------------------------------------------------------------------------------------------