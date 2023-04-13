from django.test import TestCase, Client
from django.urls import reverse
from .models import Shop

class MyViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('shop:create_shop')
        self.my_model = Shop.objects.create(shop_name='Shop10', latitude='40.712776', longitude='-74.005974')
    def test_my_view_renders_template_with_dynamic_content(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'shop_list.html')