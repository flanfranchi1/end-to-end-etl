import requests


dfp_cia_aberta = lambda ano:f'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_{ano}.zip'
itr_ciaberta = lambda ano: f'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/itr_cia_aberta_{ano}.zip'

year_range = list(range(2011, 2025))
for year in year_range:
    itr_url = itr_ciaberta(year)
    itr_filename = itr_url.split('/')[0]
    dfp_url = dfp_cia_aberta(year)
    dfp_filename = dfp_url.split('/')[0]