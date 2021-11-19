# Courses API

## Como configurar o ambiente local:

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

## Como configurar o ambiente na máquina da AWS:
    
        sudo yum install git

        git clone https://github.com/gabriel-amorim1/courses-api.git

        python3 -m venv venv

        source venv/bin/activate

        pip3 install -r requirements.txt

        sudo yum install MySQL-python

        pip3 install pymysql

        sudo yum install python-devel mysql-devel python3-devel

        pip3 install mysql-connector-python

        sudo yum install gcc libxml2-devel libxslt-devel python-devel

        pip install mysqlclient

        pip3 install djangorestframework_simplejwt

        python3 manage.py migrate

        python3 manage.py runserver 0.0.0.0:8000
    
Configurar os ALLOWED_HOSTS com a url da instância do EC2

Configurar os DATABASES com os dados abaixo:
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco',
        'USER': 'nome_de_usuário',
        'PASSWORD': 'senha_do_banco',
        'HOST': 'url_do_banco',
        'PORT': 3306,

Lembrar de liberar a porta 8000 do EC2 e a porta 3306 do RDS
Não usar HTTPS quando for conectar com o EC2