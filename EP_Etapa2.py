#!/usr/bin/python3
# |Contribuidores              | No. USP |
# |----------------------------|---------|
# |Christian M. T. Takagi      | 7136971 |
# |Cinthia M Tanaka            | 5649479 |
# |Daniel A. Nagata            | 7278048 |
# |Fernando T. Tanaka          | 6920230 |
# ------------------------------------------------------------------------------
# Disciplina: Laboratório de Programação II       
# Prof. Alfredo Goldman
# Exercicio Programa - Etapa 2
# Arquivo: app.py
# ------------------------------------------------------------------------------

import sys
import app
import cliente


if __name__ == '__main__':
    if sys.argv[1] == '--server':
       app.main()
    if sys.argv[1] == '--client':
       cliente.main()
