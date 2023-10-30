from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters, generics
#
# from lms.models import Payment
#
#
# class PaymentListView(generics.ListAPIView):
#     queryset = Payment.objects.all()
#     serializer_class = MyModelSerializer
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
#     filterset_class = PaymentFilter
#     ordering_fields = ['payment_date']  # Поля, по которым можно сортировать
#
#     def get_queryset(self):
#         queryset = Payment.objects.all()  # Базовый queryset
#         # Дополнительные фильтры, если нужно
#         return queryset