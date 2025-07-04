from django.http import JsonResponse
from finanzas.fin_repository.fin_list_expedientes_file import get_list_expdientes
from finanzas.fin_repository.p_and_r_file import payments_and_receipts
from froxa.utils.utilities.suzdal_logger import SuzdalLogger


def fin_default_controller(request, action, entity, code, description): 

    action      = str(action).strip().lower()   
    entity      = str(entity).strip().lower()           
    code        = str(code).strip().lower()
    description = str(description).strip().lower()
    

    # <str:action>/<str:entity>/<str:code>/<str:description>/
    switch_query = {
        'expedientes_importacion': lambda: get_list_expdientes(request),  # http://127.0.0.1:8000/finanzas/get/0/0/expedientes_importacion/
        
        'payments_and_receipts': lambda: payments_and_receipts(request),  # http://127.0.0.1:8000/finanzas/get/0/0/payments_and_receipts/
    }

    try:
        query_func = switch_query.get(description)
        result = query_func()
        return JsonResponse({"status": 200, 'message': 'ok', "data": result})
    except Exception as e:
        SuzdalLogger.log(f"❌ Error en consulta: str{e} ❌")
        return JsonResponse({"status": 500,"message": "Ha ocurrido un error en el servidor.","error": str(e)}, status=500)