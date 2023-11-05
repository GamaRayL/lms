from lms.models import Payment
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from lms.serializers.payment import PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('payment_method', 'paid_course_or_lesson')
    ordering_filter = ('payment_date')

    def get_queryset(self):
        queryset = Payment.objects.all()
        return queryset
