from django.urls import path
from django.http import JsonResponse

# Define a simple API view
def api_endpoint(request):
    data_from_frontend = {
        'message': 'Data received from the frontend.',
        'received_data': request.GET.get('data', None)
    }
    return JsonResponse(data_from_frontend)

# Define your API routes
urlpatterns = [
    path('api/endpoint/', api_endpoint, name='api-endpoint'),
]
