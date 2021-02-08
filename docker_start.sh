#!/bin/bash

export COLUMNS=80
flower -A app.client --address=0.0.0.0 --port=8080 --basic_auth=admin:fellow1234

exec "$@"