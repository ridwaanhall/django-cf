from django.http import JsonResponse
from django.views import View

class SimpleJsonView(View):
    def get(self, request, *args, **kwargs):
        data = {
            "message": "Hello, this is a JSON response for Django Cloudflare!"
        }
        return JsonResponse(data)