from datetime import datetime

from rest_framework.pagination import CursorPagination
from rest_framework.response import Response


class CustomCursorPagination(CursorPagination):
    ordering = 'created_at'

    def get_paginated_response(self, data):
        super_response = super().get_paginated_response(data).data
        super_response['data'] = super_response.pop('results')

        return Response({
            **super_response,
            'now': str(datetime.now())
        })