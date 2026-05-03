from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny
from .models import Appeal
from .serializers import AppealSerializer


class AppealCreateView(generics.CreateAPIView):
    """
    Public endpoint — no session auth, no CSRF check.
    Setting authentication_classes=[] prevents DRF's SessionAuthentication
    from enforcing CSRF when an admin session cookie happens to be present.
    """
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
    authentication_classes = []   # <-- no session auth → no CSRF enforcement
    permission_classes = [AllowAny]
