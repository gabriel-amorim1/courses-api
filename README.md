# Courses API

## Como configurar o ambiente:

- Tenha instalado na sua máquina o python na versão 3.x.x (https://www.python.org/downloads/)
- Tenha instalado na sua máquina o gerenciador de pacotes pip3. No linux basta rodar o comando abaixo:
    ```bash
        $ sudo apt-get install python3-pip
    ```
- Na pasta do projeto, crie um venv com o comando abaixo:
    ```bash
        $ python3 -m venv venv
    ```
- Ative o ambiente virutal criado:
    ```bash
        $ source venv/bin/activate 
    ```
- Instale as dependências necessárias para rodar o projeto:
    ```bash
        $ pip3 install -r requirements.txt
    ```
- Rode as migrations:
    ```bash
        $ python3 manage.py migrate
    ```
- Pronto, agora basta subir o servidor:
    ```bash
        $ python3 manage.py runserver
    ```

