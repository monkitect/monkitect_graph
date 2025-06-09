from django.db import connection
from django.http import JsonResponse


def health_check(request):
    # Basic health check data
    data = {'status': 'ok'}

    # Check database connection
    try:
        connection.ensure_connection()
        data['database'] = 'ok'
    except Exception as e:
        data['database'] = str(e)
        data['status'] = 'error'

    # Add more checks here (e.g., cache server, external services)

    return JsonResponse(data)
