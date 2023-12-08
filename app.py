from PIL import Image, ImageDraw, ImageFont
from PyInquirer import prompt

#Calcular Coordenada do Icone para Facebook
def calcular_coordenada_icon(nivel_rio):
    valor_calculado = ((nivel_rio - 840) / 0.10) * 17
    coordenada_final = 100 + valor_calculado
    return coordenada_final

#Calcular Coordenada do Icone para instagram
def calcular_coordenada_icon_insta(nivel_rio):
    valor_calculado = ((nivel_rio - 840) / 0.10) * 19
    coordenada_final2 = 100 + valor_calculado
    return coordenada_final2


#Obter os Icones do Tempo
def obter_icone_tempo_path(condicao_tempo):
    if condicao_tempo.lower() == 'chuvoso':
        return 'C:\\Users\gerente\\Desktop\\python-monitoramento\\icones-tempo\\chuva.png'
    elif condicao_tempo.lower() == 'sol':
        return 'C:\\Users\gerente\\Desktop\\python-monitoramento\\icones-tempo\\icone-sol.png'
    elif condicao_tempo.lower() == 'nublado':
        return 'C:\\Users\\gerente\\Desktop\\python-monitoramento\\icones-tempo\\nuvens.png'
    else:
        return 'C:\\Users\\gerente\\Desktop\\python-monitoramento\\icone-padrao.png'

def inserir_info_na_imagem(imagem_path,imagem_path_insta, icone_path, coordenada_data_hora, coordenada_data_hora2, data_hora, nivel_rio, condicao_tempo, minima, maxima, coordenada_minima, coordenada_maxima,coordenada_minima2, coordenada_maxima2):
    imagem = Image.open(imagem_path)
    imagem2 = Image.open(imagem_path_insta)
    desenhador = ImageDraw.Draw(imagem)
    desenhador2 = ImageDraw.Draw(imagem2)

    fonte = ImageFont.truetype(r'C:\Users\gerente\Desktop\python-monitoramento\metropolis-extrabold.otf', size=20)
    fonte_data_hora = ImageFont.truetype(r'C:\Users\gerente\Desktop\python-monitoramento\metropolis-extrabold.otf', size=55)
    fonte_minima_maxima = ImageFont.truetype(r'C:\Users\gerente\Desktop\python-monitoramento\metropolis-bold.otf', size=40)

    icone_tempo_path = obter_icone_tempo_path(condicao_tempo)
    icone_tempo_path_insta = obter_icone_tempo_path(condicao_tempo)
    icone_tempo = Image.open(icone_tempo_path).resize((80,80))
    icone_temp_insta = Image.open(icone_tempo_path_insta).resize((110,110))
    imagem.paste(icone_tempo, (518, 703), icone_tempo)
    imagem2.paste(icone_temp_insta, (253, 1405), icone_temp_insta)

    
    if nivel_rio == 840:

        icone = Image.open(icone_path)
        imagem.paste(icone, (100, 411), icone)
        imagem2.paste(icone, (110, 729), icone)
        coordenada_nivel_rio = (145, 411)
        coordenada_nivel_rio_2 = (155,729) 

    elif nivel_rio == 841.5:
        icone = Image.open(icone_path)
        imagem.paste(icone, (353, 394), icone)
        imagem2.paste(icone, (388, 729), icone)
        coordenada_nivel_rio = (398, 394)
        coordenada_nivel_rio_2 = (433,729) 

    elif nivel_rio == 843:
        icone = Image.open(icone_path)
        imagem.paste(icone, (609, 394), icone)
        imagem2.paste(icone, (676, 729), icone)
        coordenada_nivel_rio = (654, 394)
        coordenada_nivel_rio_2 = (721,729)  

    elif nivel_rio != 840  and nivel_rio and 841.5 and nivel_rio != 843:
     # Calcular a coordenada do ícone com base no nível do rio
        coordenada_icone = calcular_coordenada_icon(nivel_rio)
        coordenada_icone2 = calcular_coordenada_icon_insta(nivel_rio)
        # Adicionar ícone à imagem
        icone = Image.open(icone_path)
        imagem.paste(icone, (int(coordenada_icone), 409), icone)
        imagem2.paste(icone, (int(coordenada_icone2), 745), icone)
        coordenada_nivel_nova = coordenada_icone + 45
        coordenada_nivel_nova_insta = coordenada_icone2 + 45
        coordenada_nivel_rio = (int(coordenada_nivel_nova),409)
        coordenada_nivel_rio_2 = (int(coordenada_nivel_nova_insta),745)

    cor_pillow = (53, 92, 147)
    cor_black = (64, 63, 65)
    desenhador.text(coordenada_data_hora, f"{data_hora}", fill=cor_pillow, font=fonte_data_hora)
    desenhador.text(coordenada_nivel_rio, f"NÍVEL\nATUAL\n({nivel_rio} m)", fill=cor_pillow, font=fonte)
    desenhador.text(coordenada_minima, f"{minima}", fill=cor_black, font=fonte_minima_maxima)
    desenhador.text(coordenada_maxima, f"{maxima}", fill=cor_black, font=fonte_minima_maxima)
    desenhador2.text(coordenada_data_hora2, f"{data_hora}", fill=cor_pillow, font=fonte_data_hora)
    desenhador2.text(coordenada_nivel_rio_2, f"NÍVEL\nATUAL\n({nivel_rio} m)", fill=cor_pillow, font=fonte)
    desenhador2.text(coordenada_minima2, f"{minima}", fill=cor_black, font=fonte_minima_maxima)
    desenhador2.text(coordenada_maxima2, f"{maxima}", fill=cor_black, font=fonte_minima_maxima)

    imagem.save('C:\\Users\\gerente\\Desktop\\python-monitoramento\\imagem_modificada-ok.png')
    imagem2.save('C:\\Users\\gerente\\Desktop\\python-monitoramento\\imagem_modificada_insta-ok.png')
    imagem.show()
    imagem2.show()

def main():
    imagem_path = 'C:\\Users\\gerente\\Desktop\\python-monitoramento\\imagem_modificada.png'
    imagem_path_insta = 'C:\\Users\\gerente\\Desktop\\python-monitoramento\\monitoramento-rio-insta.png'
    icone_path = 'C:\\Users\\gerente\\Desktop\\python-monitoramento\\icone-regua.png'
    coordenada_data_hora = (260, 320)
    coordenada_minima = (692, 712)
    coordenada_maxima = (845, 712)
    coordenada_minima2 = (510, 1416)
    coordenada_maxima2 = (738, 1416)
    coordenada_data_hora2 = (320, 567)

    nivel_rio_atual = float(input("Informe o nível do rio:  "))
    data_hora = "07/12/2023 08h"
    minima = "18"
    maxima = "30"
    #nivel_rio_atual = 840

     # Opções para a condição do tempo
    opcoes_tempo = [
        {'name': 'Chuvoso'},
        {'name': 'Sol'},
        {'name': 'Nublado'}
    ]
    pergunta_tempo = [
        {
            'type': 'list',
            'name': 'condicao_tempo',
            'message': 'Selecione a condição do tempo:',
            'choices': opcoes_tempo
        }
    ]

    resposta_tempo = prompt(pergunta_tempo)
    condicao_tempo = resposta_tempo['condicao_tempo'].lower()

    #condicao_tempo = input("Informe a condição do tempo (chuvoso, sol, nublado): ")

    inserir_info_na_imagem(imagem_path,imagem_path_insta, icone_path, coordenada_data_hora, coordenada_data_hora2, data_hora, nivel_rio_atual, condicao_tempo, minima, maxima, coordenada_minima, coordenada_maxima, coordenada_maxima2, coordenada_minima2)
    print(f'Path da imagem: {imagem_path}')
    print(f'Path da imagem: {imagem_path_insta}')

if __name__ == "__main__":
    main()