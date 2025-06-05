from utils import limpar_tela, obter_data_hora, formatar_linha
from database import salvar_log, salvar_registro, carregar_faq

def iniciar_chatbot():
    limpar_tela()
    print(formatar_linha("💬 BEM-VINDO AO ATENDIMENTO DA PIZZARIA TECH"))

    nome = input("\nPor favor, informe seu nome: ").strip()
    conversa = []

    conversa.append(f"Início do atendimento - Cliente: {nome}")

    while True:
        limpar_tela()
        print(formatar_linha(f"👋 Olá {nome}, como posso ajudar?"))
        print("1 - Fazer um pedido")
        print("2 - Perguntas Frequentes")
        print("3 - Encerrar atendimento")

        opcao = input("\nDigite a opção: ")

        if opcao == "1":
            fazer_pedido(nome, conversa)
        elif opcao == "2":
            perguntas_frequentes(conversa)
        elif opcao == "3":
            print(f"\n✅ Atendimento encerrado. Obrigado, {nome}!")
            conversa.append("Atendimento encerrado.")
            salvar_log(conversa, nome)
            input("\nPressione Enter para voltar ao menu principal...")
            break
        else:
            print("\n❌ Opção inválida.")
            input("\nPressione Enter para tentar novamente...")

def fazer_pedido(nome, conversa):
    limpar_tela()
    print(formatar_linha("🍕 FAZER PEDIDO"))

    print("\nEscolha o sabor da pizza:")
    print("1 - Calabresa")
    print("2 - Frango com Catupiry")
    print("3 - Portuguesa")
    print("4 - Marguerita")

    opcoes = {
        "1": "Calabresa",
        "2": "Frango com Catupiry",
        "3": "Portuguesa",
        "4": "Marguerita"
    }

    opcao = input("\nDigite a opção: ")

    if opcao in opcoes:
        sabor = opcoes[opcao]
        print(f"\n🍕 Pizza de {sabor} adicionada ao pedido.")
        conversa.append(f"Pedido: Pizza de {sabor}")

        salvar_registro({
            "nome": nome,
            "pedido": sabor,
            "data": obter_data_hora()
        })

        input("\n✅ Pedido realizado! Pressione Enter para continuar...")
    else:
        print("\n❌ Opção inválida.")
        input("\nPressione Enter para tentar novamente...")

def perguntas_frequentes(conversa):
    limpar_tela()
    print(formatar_linha("❓ PERGUNTAS FREQUENTES"))

    faq = carregar_faq()

    if not faq:
        print("Nenhuma pergunta cadastrada.")
        input("\nPressione Enter para voltar...")
        return

    for idx, (pergunta, _) in enumerate(faq, 1):
        print(f"{idx} - {pergunta}")

    try:
        opcao = int(input("\nEscolha uma pergunta (número) ou 0 para voltar: "))
        if opcao == 0:
            return
        pergunta, resposta = faq[opcao - 1]
        print(f"\n📌 {pergunta}")
        print(f"💡 {resposta}")
        conversa.append(f"Perguntou: {pergunta}")
    except (ValueError, IndexError):
        print("\n❌ Opção inválida.")
    input("\nPressione Enter para continuar...")