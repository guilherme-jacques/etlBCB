import pandas as pd

from src.extracttransform import requestApiBcb
from src.load import salvarCsv

dadosBcb = requestApiBcb("20191")
salvarCsv(dadosBcb, "meiodePagamento.csv", ';', '.')
