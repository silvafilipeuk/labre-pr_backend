# LABRE-PR API

- labre-pr.org.br new API written in python for learning purposes.

- It will replace the old backend functionality of the website that is written in PHP and needs new functionality.

- Environment Variable database.env contains the database information and should be created locally as per below:

MYSQL_HOST=hostname

MYSQL_USER=mysql_username

MYSQL_PASSWORD=db_password

MYSQL_DB=database_name

# Endpoints

- GET /associates

&ensp;&ensp;&ensp;&ensp;&ensp; Return a JSON with all associates and their informations.

- GET /associates/callsign

&ensp;&ensp;&ensp;&ensp;&ensp; Return a JSON with the specific associate passed in callsign

&ensp;&ensp;&ensp;&ensp;&ensp; i.e: /associates/py5mw
