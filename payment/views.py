from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt  # Disables CSRF check for testing purposes
def process_payment(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            amount = data.get('amount')
            method = data.get('method')

            if not amount or not method:
                return JsonResponse({'status': 'error', 'message': 'Missing amount or method'}, status=400)

            # Dummy logic
            return JsonResponse({'status': 'success', 'message': 'Payment processed', 'amount': amount})

        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'message': 'Only POST allowed'}, status=405)

