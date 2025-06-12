import json
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Получаем логгер для JavaScript ошибок
js_logger = logging.getLogger('django.template')

@csrf_exempt
@require_POST
def log_js_error(request):
    """
    Эндпоинт для логирования JavaScript ошибок
    """
    try:
        data = json.loads(request.body)
        error_message = data.get('error', '')
        url = data.get('url', '')
        line = data.get('line', '')
        column = data.get('column', '')
        
        # Форматируем сообщение об ошибке
        log_message = f"JavaScript Error: {error_message} at {url}:{line}:{column}"
        
        # Логируем ошибку
        js_logger.error(log_message)
        
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400) 