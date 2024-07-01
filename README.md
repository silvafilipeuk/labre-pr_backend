# LABRE-PR API

- labre-pr.org.br new API written in python for learning purposes.

- It will replace the old backend functionality of the website that is written in PHP and needs new functionality.

- Environment Variable database.env contains the database information and should be created locally as per below:

MYSQL_HOST=hostname

MYSQL_USER=mysql_username

MYSQL_PASSWORD=db_password

MYSQL_DB=database_name

# Endpoints

&ensp;&ensp;&ensp;&ensp;&ensp; Endpoints are either public or authorization required. For the endpoints that contain private user informations, an admin authorization token is required.

- **GET** /associates

&ensp;&ensp;&ensp;&ensp;&ensp;**Authorization Token required** - Endpoint call example: /associates?auth_token=YOUR_ADMIN_TOKEN_HERE

&ensp;&ensp;&ensp;&ensp;&ensp; Return a JSON with all associates and their informations.

- **PATCH** /associates

&ensp;&ensp;&ensp;&ensp;&ensp;**Authorization Token required** - Endpoint call example: /associates?auth_token=YOUR_ADMIN_TOKEN_HERE

&ensp;&ensp;&ensp;&ensp;&ensp; Requires a JSON body with the key id and the keys for update.

&ensp;&ensp;&ensp;&ensp;&ensp; ```{
"id": "8",
"nome": "New Name"
}```

&ensp;&ensp;&ensp;&ensp;&ensp; Return a JSON with all associates and their updated informations.

- **POST** /associates

&ensp;&ensp;&ensp;&ensp;&ensp;**Authorization Token required** - Endpoint call example: /associates?auth_token=YOUR_ADMIN_TOKEN_HERE

&ensp;&ensp;&ensp;&ensp;&ensp; Requires a JSON body with the key new associate informations:

&ensp;&ensp;&ensp;&ensp;&ensp; ```{
    "nome": "New Test User",
    "cpf": "111.111.111-22",
    "rg": "1.111.111-2",
    "expedidor": "SSPPR",
    "local_nasc": "England",
    "data_nasc": "1950-01-01",
    "indicativo": "PY5ZZA",
    "classe": "A",
    "profissao": "Software Developer",
    "endereco": "111 Street",
    "bairro": "Downtown",
    "cep": "88888-888",
    "cidade": "London",
    "estado": "Londonshire",
    "telefone": "0778888888",
    "celular": "8888888888",
    "email": "user@test.co.uk",
    "password": "123456",
    "admin": 1,
    "data_assoc": "2024-07-01",
    "fistel": "12345324",
    "liberado": 1,
    "anuncio": 0,
    "remido": 0
}```

&ensp;&ensp;&ensp;&ensp;&ensp; Return a JSON with all associates and their updated informations.

- **GET** /associates/callsign

&ensp;&ensp;&ensp;&ensp;&ensp;**Authorization Token required** - Endpoint call example: /associates/callsign?auth_token=YOUR_ADMIN_TOKEN_HERE

&ensp;&ensp;&ensp;&ensp;&ensp; Return a JSON with the specific associate passed in callsign

&ensp;&ensp;&ensp;&ensp;&ensp; i.e: /associates/py5mw?auth_token=YOUR_ADMIN_TOKEN_HERE

- **GET** /news

&ensp;&ensp;&ensp;&ensp;&ensp;**Public**

&ensp;&ensp;&ensp;&ensp;&ensp; Return a JSON with all news in the system and their informations.

&ensp;&ensp;&ensp;&ensp;&ensp; **Queries available:** id, titulo (Get the news by id or title)

&ensp;&ensp;&ensp;&ensp;&ensp; i.e: /news?id=72

&ensp;&ensp;&ensp;&ensp;&ensp; i.e: /news?titulo=Labre Dx Contest
