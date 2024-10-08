from django.utils.deprecation import MiddlewareMixin
from .models import Visitor

class VisitorTrackingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = self.get_client_ip(request)
        language = request.COOKIES.get('django_language', 'en')

        # Fetch or create a visitor record based on IP and language
        visitor, created = Visitor.objects.get_or_create(ip_address=ip, language=language)

        # Update the visit count
        visitor.visit_count += 1
        visitor.save()

        # Set cookies
        request.session['visit_count'] = visitor.visit_count

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip