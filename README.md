# DJHTMX

## Requisitos
* Python 3.8.0
* PostgreSQL >= 10
* PostGIS >=2.5.1

## Configurações do Banco de Dados Espaciais

É necessário criar um banco **PostgreSQL**, no terminal, faça:

```
createdb djhtmx
```

## Como desenvolver?

* Clone o repositório;
* Crie um virtualenv com Python 3.8.0;
* Ative o virtualenv;
* Instale as dependências do ambiente de desenvolvimento;
* Crie o banco de dados espacial como foi descrito acima.


```
git clone https://github.com/marcellobenigno/djhtmx.git
cd djhtmx
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

* Renomeie o arquivo `env-sample` para `.env`:

```
mv env-sample .env
```

* Preencha as informações do `.env` e rode os seguintes comandos:

```
python manage.py makemigrations
python manage.py migrate
```