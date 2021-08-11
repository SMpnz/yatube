from django.test import Client, TestCase
from django.urls import reverse


class StaticViewsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.static_page = {
            'about:author': 'about/author.html',
            'about:tech': 'about/tech.html'
        }

    def setUp(self):
        self.guest_client = Client()

    def test_about_page_uses_correct_template(self):
        """При запросе к about
        применяется шаблон about/name.html."""
        for name, expected_template in StaticViewsTests.static_page.items():
            with self.subTest(name=name):
                response = self.guest_client.get(reverse(name))
                self.assertTemplateUsed(response, expected_template)
