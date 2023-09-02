import json

from django.http import HttpResponseServerError


class Handle500Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if response.status_code == 500:
            error_response = {
                "error": ["internal"]
            }
            response = HttpResponseServerError(
                json.dumps(error_response),
                content_type="application/json"
            )
        return response


