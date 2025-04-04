import pandas as pd

from src.extracttransform import requestApiBcb
from src.load import salvarCsv, salvarSQlite, salvarMySql

dadosBcb = requestApiBcb("20191")
# salvarCsv(dadosBcb, "meiodePagamento.csv", ';', '.')

# salvarSQlite(dadosBcb, "src/datasets/etlbcb.db","meios_pagamentos_tri")

salvarMySql(dadosBcb, "root", "root", "localhost", "etlbcb", "meiospagamentostri")