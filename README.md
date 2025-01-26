# Bot Automatizado no site ESCEX

## Descrição
Um bot automatizado simples para acessar e interagir com o site da ESCEX.

## Objetivo
Automatizar o acesso ao site da ESCEX (https://escex.tcema.tc.br/site/) e interagir com os elementos da página, como cliques, preenchimento de campos e navegação.

## Estrutura do Projeto

```bash
    bot_automatizado/ 
    ├── bot_automatizado.py # Script principal 
    ├── chromedriver.exe    # WebDriver Chrome
    ├── LICENSE             # Licença MIT
    ├── README.md           # Documentação do projeto
    └── requirements.txt    # Dependências do projeto
```

## Requisitos
- Python 3.7 ou superior
- Google Chrome ou outro navegador compatível
- ChromeDriver (ou WebDriver correspondente ao navegador escolhido)

## Instalação
1. Clone este repositório:

```bash
   git clone https://github.com/LuiSilvak/bot_automatizado.git
   cd bot_automatizado
```

2. Instale as dependências:

```bash
    pip install -r requirements.txt
```

3. Baixe o WebDriver para o navegador de sua preferência:

- ChromeDriver

4. Certifique-se de que o WebDriver esteja no mesmo diretório do projeto ou adicionado ao PATH do sistema.

## Configuração
- No arquivo bot_automatizado.py, substitua caminho/do/chromedriver (no caso deste projeto, inseri o 'chromedriver.exe' dentro do projeto) pelo caminho do seu WebDriver.
- Se necessário, ajuste os métodos de interação em interagir_com_elementos para atender às suas necessidades.

## Execução
- Para executar o bot, rode o seguinte comando:

```bash
    python bot_automatizado.py
```

## Personalização
- Adicione ou modifique interações no método interagir_com_elementos para atender aos requisitos específicos do site.

## Contribuições
- Contribuições são bem-vindas! Abra uma issue ou envie um pull request para melhorias.

## Licença
- Este projeto é open-source e está licenciado sob a MIT License.