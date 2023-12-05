from rest_framework.response import Response

from lms.models import Payment
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from lms.serializers.payment import PaymentSerializer
from lms.services import create_payment_intent, get_retrieve_payment


class PaymentListAPIView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('payment_method',)
    ordering_filter = ('payment_date',)

    def get_queryset(self):
        queryset = Payment.objects.all()
        return queryset


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer

    def perform_create(self, serializer):
        payment = serializer.save()

        payment_response = create_payment_intent(payment.payment_amount)
        payment.payment_id = payment_response.id
        payment.save()

        return super().perform_create(serializer)


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        payments_retrieve = get_retrieve_payment(obj.payment_id)

        return Response({
            'status': payments_retrieve.status,
            'body': payments_retrieve
        })

        