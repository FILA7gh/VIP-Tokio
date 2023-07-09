from django.utils import timezone


class UpdateLastVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            request.user.last_visit = timezone.now()
            request.user.save()

        response = self.get_response(request)

        return response
