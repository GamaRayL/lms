from lms.models import Payment
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from lms.serializers.payment import PaymentSerializer
from lms.services import create_payment_intent


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('payment_method', 'paid_course_or_lesson')
    ordering_filter = ('payment_date')

    def get_queryset(self):
        queryset = Payment.objects.all()
        return queryset


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save()
        
        create_payment_intent(payment)
        
        return super().perform_create(serializer)
        