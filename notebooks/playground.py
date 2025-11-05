import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium", auto_download=["html"])


app._unparsable_cell(
    r"""
                                                                                        import marimo as mo
        import requests
    """,
    name="_"
)


@app.cell
def _(requests):
    dfp_cia_aberta = lambda ano:f'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/dfp_cia_aberta_{ano}.zip'
    teste = dfp_cia_aberta(2023)
    filename = teste.split('/')[-1]
    response = requests.get(teste, stream=True, timeout=30)
    print(response.raise_for_status())
    return filename, response


@app.cell
def _():
    return


@app.cell
def _(filename, response):
    with open(filename, 'wb') as file:
        for chunck in response.iter_content(chunk_size=8192):
            if chunck:
                    file.write(chunck)
    return


if __name__ == "__main__":
    app.run()
