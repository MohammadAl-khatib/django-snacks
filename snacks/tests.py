from django.test import TestCase 
from django.urls import reverse

class SnacksTests(TestCase):

    def test_home_status_code(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # def test_snack_detail_status_code(self):
    #     url = 'http://127.0.0.1:8000/3'
    #     response = self.client.get(url)
    #     print (response)
    #     self.assertEqual(response.status_code, 200)
        
    def test_home_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "_base.html")

    # def test_snack_detail_page_template(self):
    #     url = reverse('snack_detail')
    #     response = self.client.get(url)
    #     self.assertTemplateUsed(response, "snack_detail.html")
    #     self.assertTemplateUsed(response, "_base.html")
