import openpyxl
from PIL import Image, ImageDraw, ImageFont

def gerar_certificados(planilha_path, certificado_padrao_path, output_path='./'):
    """
    Gera certificados a partir dos dados de uma planilha e salva as imagens resultantes.

    Parâmetros:
    - planilha_path (str): Caminho para a planilha Excel contendo os dados dos participantes.
    - certificado_padrao_path (str): Caminho para o modelo de certificado que será preenchido.
    - output_path (str, opcional): Caminho onde os certificados gerados serão salvos. Padrão é o diretório atual.

    Exemplo de uso:
    gerar_certificados('planilha_alunos.xlsx', 'certificado_padrao.jpg', output_path='./certificados')
    """

    # Abrir a planilha
    workbook_alunos = openpyxl.load_workbook(planilha_path)
    sheet_alunos = workbook_alunos['Sheet1']

    for indice, linha in enumerate(sheet_alunos.iter_rows(min_row=2)):
        # Cada célula que contém a informação que precisamos
        nome_curso = linha[0].value  # Nome do curso
        nome_participante = linha[1].value  # Nome do participante
        tipo_participacao = linha[2].value  # Tipo de participação
        carga_horaria = linha[5].value  # Carga horária

        data_inicio = linha[3].value  # Data início
        data_final = linha[4].value  # Data fim

        data_emissao = linha[6].value  # Data emissão

        # Transferir os dados da planilha para a imagem do certificado
        # Definindo a fonte a ser usada
        fonte_nome = ImageFont.truetype('./tahomabd.ttf', 90)
        fonte_geral = ImageFont.truetype('./tahoma.ttf', 80)
        fonte_data = ImageFont.truetype('./tahoma.ttf', 55)

        image = Image.open(certificado_padrao_path)
        desenhar = ImageDraw.Draw(image)

        desenhar.text((1020, 827), nome_participante, fill='black', font=fonte_nome)
        desenhar.text((1060, 950), nome_curso, fill='black', font=fonte_geral)
        desenhar.text((1435, 1065), tipo_participacao, fill='black', font=fonte_geral)
        desenhar.text((1480, 1182), str(carga_horaria), fill='black', font=fonte_geral)

        desenhar.text((750, 1770), data_inicio, fill='blue', font=fonte_data)
        desenhar.text((750, 1930), data_final, fill='blue', font=fonte_data)

        desenhar.text((2220, 1930), data_emissao, fill='blue', font=fonte_data)

        image.save(f'{output_path}/{indice} {nome_participante} certificado.png')



# Exemplo de uso:
gerar_certificados('planilha_alunos.xlsx', 'certificado_padrao.jpg', output_path='./certificados')
