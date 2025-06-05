import os

def inicializar_arquivos():
    os.makedirs('dados', exist_ok = True)
    arquivos = ['faq.txt', 'logis.txt', 'registros.txt']
    for arquivo in arquivos:
        caminho = os.path.join('dados', arquivo)
        if not os.path.exists(caminho):
            with open(caminho, 'w', encoding='utf-8') as f:
                if arquivo == 'faq.txt':
                    f.write('Qual o horário de funcionamento?|De segunda a sexta, das 10h às 22h. \n')
                    f.write('Vocês fazem entregas?|Sim, entregamos em toda a cidade. \n')
                    f.write('Qual o tempo médio de entrega?|Entre 30 a 45 minutos. \n')

def salvar_log(conversa, nome):
    with open('dados/logs.txt', 'a', encoding='utf-8') as f:
        for linha in conversa:
            f.write(f'[{nome}] {linha}\n')
        f.write('-' * 40 + '\n')

