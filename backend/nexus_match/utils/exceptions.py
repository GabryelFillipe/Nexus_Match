from rest_framework.exceptions import APIException
from rest_framework import status

class BusinessRuleException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'A operação não pode ser completada devido a uma regra de negócio.'
    default_code = 'business_rule_error'

class NotFoundException(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'O recurso solicitado não foi encontrado.'
    default_code = 'not_found'

class ConflictException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'Já existe um registro com esses dados.'
    default_code = 'conflict'

class ExternalServiceError(APIException):
    status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    default_detail = 'O serviço externo está temporariamente indisponível.'
    default_code = 'service_unavailable'