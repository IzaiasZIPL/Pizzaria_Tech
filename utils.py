import os
from datetime import datetime

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def obter_data_hora():
    return datetime.now().strftime('%Y-%m-%d %H:%M')

def formatar_linha(texto):
    return f"\n{'=' * 10} {texto} {'=' * 10}\n"

def exibir_menu_principal():
    print(formatar_linha("🤖 CHATBOT - PIZZARIA TECH"))
    print("1 - Iniciar Atendimento")
    print("2 - Sobre a Empresa")
    print("3 - Sair")
    return input("\nEscolha uma opção: ")