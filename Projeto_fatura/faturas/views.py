from django.shortcuts import render

faturas = [
    {
        'Vendedor': "EDP",
        'Data': "28/03/2019",
        'imagem': 'imagem1',
        'Descricao': 'Fatura da Luz',
        'Valor': "70,90€"
    },
    {
        'Vendedor': "Ipbeja",
        'Data': "15/02/2019",
        'imagem': 'imagem1',
        'Descricao': 'Propina do mês 12/2018',
        'Valor': '67,90€'
    },
    {
        'Vendedor': "Ipbeja",
        'Data': "15/01/2019",
        'imagem': 'imagem1',
        'Descricao': 'Propina do mês 11/2018',
        'Valor': '67,90€'
    },
    {
        'Vendedor': "Ipbeja",
        'Data': "15/12/2018",
        'imagem': 'imagem1',
        'Descricao': 'Propina do mês 10/2018',
        'Valor': '67,90€'
    }
]


def home(request):
    return render(request, 'faturas/home.html', {'title': "Faturação", 'fatura': faturas})


def about(request):
    return render(request, 'faturas/sobre.html')
