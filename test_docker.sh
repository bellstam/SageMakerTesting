#!/bin/bash

PACKAGE=$1

docker build -t $PACKAGE:test $PACKAGE/
docker run --name test_docker_app -p 8080:8080 $PACKAGE:test
