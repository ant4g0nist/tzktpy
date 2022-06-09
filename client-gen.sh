#!/bin/bash -x
codegen=swagger-codegen
language=python
# brew install swagger-codegen
# swagger-codegen generate -i https://api.tzkt.io/v1/swagger.json -l $python -o ./
if ! command -v $codegen &> /dev/null
then
    echo 'Installing swagger-codegen on macOS'
    brew install swagger-codegen
fi

swagger-codegen generate -i https://api.tzkt.io/v1/swagger.json -l $language -o ./ -c config.json