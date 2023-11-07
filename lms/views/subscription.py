from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from lms.models import Subscription
from lms.serializers.subscription import SubscriptionSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [AllowAny]

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.user == request.user:
            pass
