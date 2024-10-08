from django.utils.deprecation import MiddlewareMixin
from .models import VisitorCount

class VisitorCountMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if 'admin' not in request.path:  # ถ้าไม่ใช่ admin page
            # เพิ่มจำนวนผู้เข้าชม
            visitor, created = VisitorCount.objects.get_or_create(id=1)
            visitor.count += 1
            visitor.save()