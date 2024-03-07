#!/bin/bash

# Nao esquecer de autorizar o arquivo antes 
#   =>  chmod +x run_tests.sh
# Depois para executar
#   => ./run_tests.sh

python3 -m pytest test_fib.py

python3 -m pytest fib2.py

