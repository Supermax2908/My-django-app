from django.contrib.auth.models import User
from django.test import TestCase

from orders.models import Order, OrderLesson
from orders.serializers import OrderSerializer
from lessons.models import Lesson


def paginated_response(order=None): 
    results = [] 
    if order: 
        results.append(OrderSerializer(order).data) 
        return {
            'count': len(results), 'next': None, 'previous': None, 'results': results 
        } 
        
class OrdersApiTestCase(TestCase): 
    def assertEmpty(self, response): 
        self.assertEqual(response.json(), paginated_response()) 
    def assertOrder(self, response): 
        self.assertEqual(response.json(), paginated_response(self.order)) 
    def setUp(self): 
        lesson = Lesson.objects.create(topic='Електромагнітні бурі', cash=123.45) 
        self.user = User.objects.create_user(username='admin') 
        self.order = Order.objects.create(user=self.user) 
        OrderLesson.objects.create(order=self.order, lesson=lesson, quantity=2) 
    def test_no_auth(self): 
        response = self.client.get('/api/orders/') 
        self.assertEqual(response.status_code, 403) 
    def test_all_ok(self): 
        self.client.force_login(self.user) 
        response = self.client.get('/api/orders/') 
        self.assertEqual(response.status_code, 200) 
        self.assertOrder(response) 
    def test_different_user(self): 
        another_user = User.objects.create_user(username='another') 
        self.client.force_login(another_user) 
        response = self.client.get('/api/orders/') 
        self.assertEqual(response.status_code, 200) 
        self.assertEmpty(response) 
    def test_different_user_but_superuser(self): 
        superuser = User.objects.create_superuser(username='another_superuser', password='password') 
        self.client.force_login(superuser) 
        response = self.client.get('/api/orders/') 
        self.assertEqual(response.status_code, 200) 
        self.assertOrder(response)