#!/bin/bash

NAME=$1
sed -i -e "s/***/***/g" ${NAME}
