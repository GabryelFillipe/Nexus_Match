from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_data = {
            "status": "error",
            "status_code": response.status_code,
            "message": "Erro na requisição", 
            "details": response.data
        }
        
        if response.status_code == 404:
            custom_data['message'] = "Recurso não encontrado."
        elif response.status_code == 400:
            custom_data['message'] = "Dados inválidos. Verifique os campos."
        elif response.status_code == 401:
            custom_data['message'] = "Você precisa estar logado."
            
        response.data = custom_data

    else:
        logger.error(f"Erro inesperado: {exc}", exc_info=True)
        
        return Response({
            "status": "error",
            "status_code": 500,
            "message": "Erro interno do servidor. Nossa equipe foi notificada.",
            "details": str(exc)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response