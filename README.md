# Courses API

- Aplicação desenvolvida para compartilhamento de cursos entre estudantes. Ao cadastrar um curso na aplicação, é inserido a url e as informações inerentes a ele. É possível avaliá-lo com a nota de 1 a 5 e será mostrado a média das avaliações, possibilitando ao aluno saber se é um bom curso ou não. Podem ser compartilhados tanto cursos pagos como gratuitos e isso é indicado na hora do cadastro. A ideia é compartilhar o máximo de conhecimento e conteúdo bom possível para ajudar-mos nossa comunidade!

--------------------------------------------------------------------------------

## Como configurar o ambiente local:

- Tenha instalado na sua máquina o python na versão 3.x.x (https://www.python.org/downloads/)

- Tenha instalado na sua máquina o gerenciador de pacotes pip3. No linux basta rodar o comando abaixo:
    ```bash
    sudo apt-get install python3-pip
    ```

- Na pasta do projeto, crie um venv com o comando abaixo:
    ```bash
    python3 -m venv venv
    ```

- Ative o ambiente virutal criado:
    ```bash
    source venv/bin/activate 
    ```

- Instale as dependências necessárias para rodar o projeto:
    ```bash
    pip3 install -r requirements.txt
    ```

- Rode as migrations:
    ```bash
    python3 manage.py migrate
    ```

- Pronto, agora basta subir o servidor:
    ```bash
    python3 manage.py runserver
    ```

--------------------------------------------------------------------------------

## Como configurar o ambiente na máquina da AWS:

### 1 Passo:

- Baixar o arquivo `.pem` e conectar-se via ssh com a instância da aws:
    ```bash
    chmod 400 labsuser.pem
    ```
    ```bash
    ssh -i labsuser.pem ec2-user@ipv4_publico_bastion_host
    ```

### 2 Passo:

- Instalar o projeto e o ambiente na instancia da aws:
    ```bash
    sudo yum install git \
    && git clone https://github.com/gabriel-amorim1/courses-api.git \
    && cd courses-api \
    && python3 -m venv venv \
    && source venv/bin/activate \
    && pip3 install -r requirements.txt \
    && sudo yum install MySQL-python \
    && pip3 install pymysql \
    && sudo yum install python-devel mysql-devel python3-devel \
    && pip3 install mysql-connector-python \
    && sudo yum install gcc libxml2-devel libxslt-devel python-devel \
    && pip install mysqlclient \
    && pip3 install djangorestframework_simplejwt
    ```

### 3 Passo:

- Criar instancia de bando de dados na aws

- Configurar no `project/settings.py` os DATABASES com os dados abaixo:
    ```python
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco',
        'USER': 'nome_de_usuário',
        'PASSWORD': 'senha_do_banco',
        'HOST': 'url_do_banco',
        'PORT': 3306,
    }
    ```

- Liberar a porta 8000 do EC2 e a porta 3306 do RDS

- Configurar os ALLOWED_HOSTS com o DNS IPv4 público da instância do EC2

### 4 Passo:

- Volte para a pasta raiz do projeto e rode os seguintes comandos:
    ```bash
    python3 manage.py migrate
    ```
    ```bash
    python3 manage.py runserver 0.0.0.0:8000
    ```

- Não usar HTTPS quando for conectar com o EC2

--------------------------------------------------------------------------------

## Rotas da aplicação:

### Autenticação (Auth):
- POST `auth/register/`
    - Rota referente ao cadastro de usuário na plataforma. 
    - Body:
        ```Json
        {
            "username": "fakeuser",
            "password": "password",
            "password2": "password",
            "email": "user@test.com",
            "first_name": "Fake",
            "last_name": "User"
        }
        ```
    - Response:
        - Status: 
            `201`
        - Body:
            ```Json
            {
                "id": 1,
                "username": "fakeuser",
                "email": "user@test.com",
                "first_name": "Fake",
                "last_name": "User"
            }
            ```

- POST `auth/login/`
    - Rota referente ao login do usuário na plataforma. Retorna um access token e um refresh token que devem ser mandados como forma de bearer token no cabeçalho das requisições.
    - Body:
        ```Json
        {
            "username": "fakeuser",
            "password": "password"
        }
        ```
    - Response:
        - Status: 
            `200`
        - Body:
            ```Json
            {
                "refresh": "string",
                "access": "string"
            }
            ```

- POST `auth/login/refresh/`
    - Rota referente a criação de um access token com maior duração. Deve ser mandado o refresh token da rota acima.
    - Body:
        ```Json
        {
            "refresh": "string"
        }
        ```
    - Response:
        - Status: 
            `200`
        - Body:
            ```Json
            {
                "access": "string"
            }
            ```

- POST `auth/change_password/user_id/`
    - Rota referente a troca de senha do usuário.
    - Body:
        ```Json
        {
            "password": "new_password",
            "password2": "new_password",
            "old_password": "old_password"
        }
        ```
    - Response:
        - Status: 
            `200`
        - Body:
            ```Json
            {}
            ```

- GET `auth/retrieve_self_profile/`
    - Retorna os dados do usuário de acordo com o token.
    - Response:
        - Status: 
            `200`
        - Body:
            ```Json
            {
                "id": 1,
                "username": "fakeuser",
                "first_name": "Fake",
                "last_name": "User",
                "email": "user@test.com"
            }
            ```

### Cursos (Courses):
- POST `courses/`
    - Cria um curso. 
    - Body:
        ```Json
        {
            "name": "Nome do curso",
            "author": "Autor do curso",
            "release_year": 2021,
            "description": "Descrição do curso",
            "url": "https://www.teste.com/",
            "is_free": true,
            "price": "0.00"
        }
        ```
    - Response:
        - Status: 
            `201`
        - Body:
            ```Json
            {
                "id_course": "2f006f13-ca88-4586-a0f4-5a6f2cb2b94c",
                "name": "Nome do curso",
                "author": "Autor do curso",
                "release_year": 2021,
                "description": "Descrição do curso",
                "is_free": true,
                "price": "0.00",
                "rating": "0.00",
                "quantity_of_ratings": 0,
                "created_at": "2021-11-22",
                "owner": 1
            }
            ```

- GET `courses/`
    - Retorna todos os cursos cadastrados.
    - Response:
        - Status: 
            `200`
        - Body:
            ```Json
            [
                {
                    "id_course": "2f006f13-ca88-4586-a0f4-5a6f2cb2b94c",
                    "name": "Nome do curso",
                    "author": "Autor do curso",
                    "release_year": 2021,
                    "description": "Descrição do curso",
                    "is_free": true,
                    "price": "0.00",
                    "rating": "0.00",
                    "quantity_of_ratings": 0,
                    "created_at": "2021-11-22",
                    "owner": 1
                }
            ]
            ```

- GET `courses/course_id/`
    - Retorna um curso pelo id.
    - Response:
        - Status: 
            `200`
        - Body:
            ```Json
            {
                "id_course": "2f006f13-ca88-4586-a0f4-5a6f2cb2b94c",
                "name": "Nome do curso",
                "author": "Autor do curso",
                "release_year": 2021,
                "description": "Descrição do curso",
                "is_free": true,
                "price": "0.00",
                "rating": "0.00",
                "quantity_of_ratings": 0,
                "created_at": "2021-11-22",
                "owner": 1
            }
            ```

- PUT `courses/course_id/`
    - Atualiza um curso pelo id. 
    - Body:
        ```Json
        {
            "name": "Nome do curso",
            "author": "Autor do curso",
            "release_year": 2021,
            "description": "Descrição do curso",
            "url": "https://www.teste.com/",
            "is_free": true,
            "price": "0.00"
        }
        ```
    - Response:
        - Status: 
            `200`
        - Body:
            ```Json
            {
                "id_course": "2f006f13-ca88-4586-a0f4-5a6f2cb2b94c",
                "name": "Nome do curso",
                "author": "Autor do curso",
                "release_year": 2021,
                "description": "Descrição do curso",
                "is_free": true,
                "price": "0.00",
                "rating": "0.00",
                "quantity_of_ratings": 0,
                "created_at": "2021-11-22",
                "owner": 1
            }
            ```
        
- DELETE `courses/course_id/`
    - Deleta um curso pelo id.
    - Response:
        - Status: 
            `204`

### Avaliações (Ratings):
- POST `ratings/`
    - Cria uma avaliação. 
    - Body:
        ```Json
        {
            "value": 5,
            "course": "2f006f13-ca88-4586-a0f4-5a6f2cb2b94c"
        }
        ```
    - Response:
        - Status: 
            `201`
        - Body:
            ```Json
            {
                "id_rating": "a3ad4328-6994-4456-aff3-d0c32f94c22d",
                "course": "2f006f13-ca88-4586-a0f4-5a6f2cb2b94c",
                "value": 5,
                "created_at": "2021-11-22",
                "owner": 1
            }
            ```

- GET `ratings/`
    - Retorna todas as avaliações cadastradas.
    - Response:
        - Status: 
            `200`
        - Body:
            ```Json
            [
                {
                    "id_rating": "a3ad4328-6994-4456-aff3-d0c32f94c22d",
                    "course": "2f006f13-ca88-4586-a0f4-5a6f2cb2b94c",
                    "value": 5,
                    "created_at": "2021-11-22",
                    "owner": 1
                }
            ]
            ```

- GET `ratings/rating_id/`
    - Retorna uma avaliação pelo id.
    - Response:
        - Status: 
            `200`
        - Body:
            ```Json
            {
                "id_rating": "a3ad4328-6994-4456-aff3-d0c32f94c22d",
                "course": "2f006f13-ca88-4586-a0f4-5a6f2cb2b94c",
                "value": 5,
                "created_at": "2021-11-22",
                "owner": 1
            }
            ```

- PUT `ratings/rating_id/`
    - Atualiza uma avaliação pelo id. 
    - Body:
        ```Json
        {
            "id_rating": "a3ad4328-6994-4456-aff3-d0c32f94c22d",
            "course": "2f006f13-ca88-4586-a0f4-5a6f2cb2b94c",
            "value": 5,
            "created_at": "2021-11-22",
            "owner": 1
        }
        ```
    - Response:
        - Status: 
            `200`
        - Body:
            ```Json
            {
                "id_rating": "a3ad4328-6994-4456-aff3-d0c32f94c22d",
                "course": "2f006f13-ca88-4586-a0f4-5a6f2cb2b94c",
                "value": 5,
                "created_at": "2021-11-22",
                "owner": 1
            }
            ```
        
- DELETE `ratings/rating_id/`
    - Deleta uma avaliação pelo id.
    - Response:
        - Status: 
            `204`

--------------------------------------------------------------------------------
