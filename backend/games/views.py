from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def teste_api(request):
    # Criamos um dicionário que simula dados do NexusMatch
    dados_teste = {
        "projeto": "NexusMatch",
        "status": "Backend configurado com sucesso!",
        "versao": "1.0",
        "funcionalidade": "Teste de API para React"
    }
    return Response(dados_teste)

@api_view(['GET'])
def ola(request):
    dados_ola= {
        "projeto": "NexusMatch",
        "status": "Backend configurado com sucesso!",
        "versao": "1.0",
        "funcionalidade": "Olá mundo!"
    }
    return Response(dados_ola)