#!/bin/bash

NAME=$1
sed -i -e "s/havrm/***/g" ${NAME}
