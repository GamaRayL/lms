from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from lms.models import Subscription
from lms.serializers.subscription import SubscriptionSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [AllowAny]

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()

        obj.is_active = False
        obj.save()
        serializer = SubscriptionSerializer(obj)
        return Response(serializer.data)



