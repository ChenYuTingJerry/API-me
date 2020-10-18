# GN-API-me

GN-API-me is a API service of current user (called me). It mainly built by [Sanic](https://github.com/huge-success/sanic).


## Prerequisites

* python 3.6+
* AWS credentials

## Installation

```sh
$pip install -r requirements.txt
```

## Start the server

```sh
docker-compose up
```

## Check server health

```sh
$curl http://0.0.0.0:3000/health
{"status":"OK"}
```

## Stop the server

```sh
docker-compose down
```
