from tkinter import *
from datetime import datetime
from usuals import UsualFunctions


def create_dashboard():
    white = '#FFFFFF'
    black = '#151515'
    red = "#9D0208"
    green = '#08A045'

    tela = Tk()
    tela.title('Dashboard')
    tela.geometry("750x480")
    tela.resizable(False, False)
    tela['background'] = black

    ## PORCENTAGENS
    total_ativos = int(UsualFunctions().get_active_cases().replace('.', ''))
    mild = int(UsualFunctions().get_mild_conditions().replace('.', ''))
    serious = int(UsualFunctions().get_serious_conditions().replace('.', ''))

    mild = (mild / total_ativos) * 100
    serious = (serious / total_ativos) * 100

    ## DATA
    hoje = datetime.now()
    data = f'{"%02d" % hoje.day}/{"%02d" % hoje.month}/{hoje.year}'

    ## HEADER
    titulo1 = Label(tela, text='Covid-19', font='Impact 40', bg=black, fg=white)
    titulo1.place(relx=0.5, rely=0.05, anchor=CENTER)

    titulo2 = Label(tela, text='Tracker', font='Impact 40', bg=black, fg=white)
    titulo2.place(relx=0.5, rely=0.18, anchor=CENTER)

    subtitulo = Label(tela, text='Dados da covid-19 no Brasil em tempo real', font='Roboto 16', bg=black, fg=green)
    subtitulo.place(relx=0.5, rely=0.27, anchor=CENTER)

    data_label = Label(tela, text=data, font='Roboto 12', bg=black, fg=white)
    data_label.place(relx=0.5, rely=0.32, anchor=CENTER)

    ## INFO
    casos_label = Label(tela, text="Total de casos:", font='Roboto 20', bg=black, fg=white)
    casos_label.place(relx=0.05, rely=0.4, anchor='w')

    casos_number = Label(tela, text=UsualFunctions().get_cases(), font='Roboto 30 bold', bg=black, fg=red)
    casos_number.place(relx=0.45, rely=0.4, anchor='w')

    recuperados_label = Label(tela, text="Total de recuperados:", font='Roboto 20', bg=black, fg=white)
    recuperados_label.place(relx=0.05, rely=0.5, anchor='w')

    recuperados_number = Label(tela, text=UsualFunctions().get_recovered(), font='Roboto 30 bold', bg=black, fg=green)
    recuperados_number.place(relx=0.45, rely=0.5, anchor='w')

    mortes_label = Label(tela, text="Total de mortes:", font='Roboto 20', bg=black, fg=white)
    mortes_label.place(relx=0.05, rely=0.6, anchor='w')

    mortes_number = Label(tela, text=UsualFunctions().get_deaths(), font='Roboto 30 bold', bg=black, fg=red)
    mortes_number.place(relx=0.45, rely=0.6, anchor='w')

    ativos_label = Label(tela, text="Total de casos ativos:", font='Roboto 20', bg=black, fg=white)
    ativos_label.place(relx=0.05, rely=0.7, anchor='w')

    ativos_number = Label(tela, text=UsualFunctions().get_active_cases(), font='Roboto 30 bold', bg=black, fg=white)
    ativos_number.place(relx=0.45, rely=0.7, anchor='w')

    casos_leves_label = Label(tela, text="dos ativos apresentam condições leves", font='Roboto 13', bg=black, fg=white)
    casos_leves_label.place(relx=0.05, rely=0.95, anchor='w')

    casos_leves_number = Label(tela, text=f'{"%.1f" % mild}%', font='Roboto 30 bold', bg=black, fg=green)
    casos_leves_number.place(relx=0.2, rely=0.85, anchor='w')

    casos_graves_label = Label(tela, text="dos ativos apresentam condições graves", font='Roboto 13', bg=black, fg=white)
    casos_graves_label.place(relx=0.55, rely=0.95, anchor='w')

    casos_graves_number = Label(tela, text=f'{"%.1f" % serious}%', font='Roboto 30 bold', bg=black, fg=red)
    casos_graves_number.place(relx=0.7, rely=0.85, anchor='w')

    tela.mainloop()