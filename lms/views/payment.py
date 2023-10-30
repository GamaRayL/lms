from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics
from lms.serializers.payment import PaymentSerializer

from lms.models import Payment


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    # filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # filterset_class = PaymentFilter
    # ordering_fields = ['payment_date']

    def get_queryset(self):
        queryset = Payment.objects.all()
        return queryset