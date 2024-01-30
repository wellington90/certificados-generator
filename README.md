
# Gerador de Certificados

## Descrição
Este script em Python gera certificados a partir dos dados de uma planilha Excel e salva as imagens resultantes usando um modelo de certificado.

## Requisitos
Certifique-se de ter as bibliotecas necessárias instaladas antes de executar o script. Você pode instalá-las usando o seguinte comando.

1. Clone este repositório:

```bash
git clone https://github.com/wellington90/gerador-certificados.git
cd gerador-certificados
```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv
source venv/bin/activate  # no Windows, use "venv\Scripts\activate"
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o script:

```bash
python gerar_certificados.py planilha_alunos.xlsx certificado_padrao.jpg
```

Opcionalmente, você pode fornecer um caminho de saída para os certificados gerados:

```bash
python gerar_certificados.py planilha_alunos.xlsx certificado_padrao.jpg --output ./certificados
```

## Estrutura do Projeto
- `gerar_certificados.py`: O script principal que realiza a geração de certificados.
- `planilha_alunos.xlsx`: Exemplo de planilha Excel contendo os dados dos participantes.
- `certificado_padrao.jpg`: Modelo de certificado que será preenchido.
- `requirements.txt`: Lista de dependências do projeto.

## Contribuição
Sinta-se à vontade para contribuir para este projeto. Basta abrir uma issue ou enviar um pull request.

