from django.test import TestCase, Client
from django.urls import reverse
from .models import Shop

class MyViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('shop:create_shop')
        self.my_model = Shop.objects.create(shop_name='Shop10', latitude='40.712776', longitude='-74.005974')
        print("modellllllllllllllllllll id", self.my_model.id)
    def test_my_view_renders_template_with_dynamic_content(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'shop_list.html')
        self.assertContains(response, self.my_model.shop_name)
        # self.assertContains(response, self.my_model.latitude)
        # self.assertContains(response, self.my_model.longitude)
        
    # def test_my_view_returns_404_for_nonexistent_object(self):
    #     nonexistent_id = self.my_model.id + 1
    #     url = reverse('my-view-detail', args=[nonexistent_id])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 404)
        
    def test_my_view_updates_object_and_redirects_to_detail_view(self):
        url = reverse('shop:update_shop', args=[self.my_model.id])
        print("urlssssssssssssssssssssss",url)
        new_shop_name = 'New shop'
        new_latitude = '1219.1229'
        new_longitude = '-30.433'
        data = {'name': new_shop_name, 'latitude': new_latitude, 'longitude':new_longitude}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)
        updated_model = Shop.objects.get(id=self.my_model.id)
        print("dsdsdsdfsdfsdfsdf", updated_model)
        print("updated model", updated_model)
        self.assertEqual(updated_model.shop_name, new_shop_name)
        self.assertEqual(updated_model.latitude, new_latitude)
        self.assertEqual(updated_model.longitude, new_longitude)
        
    # def test_my_view_deletes_object_and_redirects_to_list_view(self):
    #     url = reverse('my-view-delete', args=[self.my_model.id])
    #     response = self.client.post(url)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertFalse(Shop.objects.filter(id=self.my_model.id).exists())








# from django.test import TestCase
# from django.urls import reverse

# from .models import Shop

# class AuthorListViewTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#       Shop.objects.create(
#           shop_name='Shop10',
#           latitude='40.712776',
#           longitude='-74.005974',
#       )

#     def test_view_url_exists_at_desired_location(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)

#     # def test_view_uses_correct_template(self):
#     #     response = self.client.get(reverse('authors'))
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertTemplateUsed(response, 'catalog/author_list.html')

#     # def test_pagination_is_ten(self):
#     #     response = self.client.get(reverse('authors'))
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertTrue('is_paginated' in response.context)
#     #     self.assertTrue(response.context['is_paginated'] == True)
#     #     self.assertEqual(len(response.context['author_list']), 10)

#     # def test_lists_all_authors(self):
#     #     # Get second page and confirm it has (exactly) remaining 3 items
#     #     response = self.client.get(reverse('authors')+'?page=2')
#     #     self.assertEqual(response.status_code, 200)
#     #     self.assertTrue('is_paginated' in response.context)
#     #     self.assertTrue(response.context['is_paginated'] == True)
#     #     self.assertEqual(len(response.context['author_list']), 3)
