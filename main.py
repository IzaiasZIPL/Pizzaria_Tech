from chatbot import iniciar_chatbot
from utils import limpar_tela, exibir_menu_principal
from database import inicializar_arquivos

def main():
    inicializar_arquivos()
    while True:
        limpar_tela()
        opcao = exibir_menu_principal()

        if opcao == "1": 
            iniciar_chatbot()
        elif opcao == "2":
            print("\n📄 Informações da Empresa:")
            print("Empresa: Pizzaria Tech")
            print("Horário: Segunda a Sexta, 10h às 22h")
            print("Contato: (99) 99999-9999")
            input("\nPressione Enter para voltar ao menu...")
        elif opcao == "3":
            print("\n🚪 Encerrando... Até mais!")
            break
        else:
            print("\n❌ Opção inválida. Tente novamente.")
            input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()