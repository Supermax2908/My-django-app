from django_filters import FilterSet, CharFilter

from lessons.models import Lesson


class LessonFilterSet(FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    cash__gte = CharFilter(field_name='cash', lookup_expr='gte')
    cash__lte = CharFilter(field_name='cash', lookup_expr='lte')

    cheap = CharFilter(method='filter_cheap')

    def filter_cheap(self, queryset, name, value):
        if value:
            return queryset.filter(cash__lt=20)
        return queryset

    category = CharFilter(field_name='category__name', lookup_expr='icontains')

    class Meta:
        model = Lesson
        fields = ['name', 'cash', 'category']