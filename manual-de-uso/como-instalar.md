## Como baixar, configurar e executar o codigo do projeto FishermanFriend ?

## No terminal da sua máquina, digite:

### Baixando o projeto no seu computador:

    git clone https://github.com/RamonBomfim/desafio-estagio-sti.git

### Criando seu ambiente virtual:
#### O python e o virtualenv já deve estar instalado. 

    cd fisherman_friend
    python -m venv venv
    cd venv/scripts
    activate
    
### Instale o PostgreSQL
    
    https://www.postgresql.org/download/
    
#### Obs.: Se tiver alguma dificuldade de como instalar e configurar 
#### o postgresql você pode seguir esse video https://youtu.be/Phkf71aZL7A
#### da Boson Treinamentos, é bem didático...


### Abra o seu Pgadmin e crie uma conexão:

    Nessa conexão crie um banco de dados vazio com o nome
    de fisherman_friend
    
    obs: no settings.py do seu projeto, altere todos os dados,
    de acordo com a sua máquina. 

### Instalando os modulos e dependencias do projeto FishermanFriend
##### Estando no terminal vá para o diretório raiz do seu
##### projeto e digite: 
    
    pip install -r requirements-dev.txt
    
### Aplicando as migrações no seu DB:

    python manage.py migrate
    
### Criando super usuario:

    python manage.py createsuperuser
    
### Executando o projeto pela primeira vez:

    python manage.py runserver
