from rest_framework import serializers

from lms.models import Payment


# class PaymentFilter(serializers.FilterSet):
#     min_date = filters.DateFilter(field_name="payment_date", lookup_expr='gte')
#     max_date = filters.DateFilter(field_name="payment_date", lookup_expr='lte')
#     course = filters.CharFilter(field_name="paid_course_or_lesson__name", lookup_expr='icontains')
#     payment_method = filters.CharFilter(field_name="payment_method", lookup_expr='icontains')
#
#     class Meta:
#         model = Payment
#         fields = ['min_date', 'max_date', 'course', 'payment_method']