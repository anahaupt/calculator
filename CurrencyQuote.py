#This script returns the quotation of a currency (quotation in Reais (BRL)) from the data of the Brazilian Central Bank

import requests
import json

#Set Inputs
inputData = str(input('Insira a data no formato MM-DD-AAAA:'))
currencyCode = str(input('Insira o código da moeda (ex: USD, EUR, GBP, CAD):'))

#Formatting inputs
initialData = f'\'{inputData}\''
finalData = initialData
currencyInput = f'\'{currencyCode}\''

#Set Parameters
parameters = {
    '@codigoMoeda': currencyInput,
    '@dataInicialCotacao': initialData,
    '@dataFinalCotacao': finalData
}

#Request data
res = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodoFechamento(codigoMoeda=@codigoMoeda,dataInicialCotacao=@dataInicialCotacao,dataFinalCotacao=@dataFinalCotacao)", parameters)

#Accessing the gross return
#print(res.text)

#Accessing the structured return
result = json.loads(res.text)
#print(result)

#Accessing a specific return data
## It is important to pay attention to the nesting of the objects
cotacaoVenda = result['value'][0]['cotacaoVenda']
cotacaoCompra = result['value'][0]['cotacaoCompra']


#Final
print('Cotação do',currencyInput,' em',initialData,':')
print('Cotação de venda: ',cotacaoVenda)
print('Cotação de compra: ',cotacaoCompra)


#--the next steps are to create a script to return in cases of error.
#   common mistakes:
#    - Date is not a business day and therefore does not have PTAX registered
#    - The date was not entered in the correct format
#    - The currency was not informed in the correct format