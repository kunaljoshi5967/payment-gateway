from django.contrib import admin
from django.urls import path, include  # ✅ This line is required

from django.http import JsonResponse  # For optional welcome message

def home(request):
    return JsonResponse({'message': 'Welcome to the Payment Gateway API'})

urlpatterns = [
    path('', home),  # 👈 Optional root route
    path('admin/', admin.site.urls),
    path('payment/', include('payment.urls')),  # 👈 Includes payment URLs
]
