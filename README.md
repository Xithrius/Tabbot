<h1 align="center">Tabbot</h1>
<h3 align="center">Small amounts of chaos through meowing.</h3>

# Setup:
*NOTE*:
- This guide assumes you've copied the template from `.env-example` to a file called `.env` that you've created yourself.
- The placeholder in the postgres command is your password that you must put into your `.env` file.
```shell script
$ docker pull postgres
$ docker run --name postgres -e POSTGRES_PASSWORD=PLACEHOLDER_PASSWORD -d postgres
docker-compose up --build
```
