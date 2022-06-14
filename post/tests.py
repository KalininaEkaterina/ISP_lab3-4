from cProfile import Profile
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from post.models import Nursery


class TestTestCase(TestCase):
    def test_registration(self):
        form_data = {'username': "test",  'email': 'test@mo.com', "password1": "passwors", 'password2': "passwors"}
        response = self.client.post("/register/", data=form_data)
        self.assertEqual(response.status_code, 302)

    @classmethod
    def setUpTestData(cls):
        Nursery.objects.create(name='Собака', descr='Куплю собаку')

    def test_login(self):
        form_data = {'username': "test", "password1": "passwors"}
        response = self.client.post("/login/", data=form_data)
        self.assertEqual(response.status_code, 200)

    def test_create(self):
        self.client.login(name='name', password='password')
        data = {"name": 'Names', 'descr': 'description'}
        response = self.client.post('/create', data, format="format")
        self.assertEqual(response.status_code, 302)

    def test_profile_get(self):
        response = self.client.get("/profile/test")
        self.assertEqual(response.status_code, 404)

    def test_name_label(self):
        director = Nursery.objects.get(id=1)
        field_label = director._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Название')

    def test_descr_label(self):
        director = Nursery.objects.get(id=1)
        field_label = director._meta.get_field('descr').verbose_name
        self.assertEquals(field_label, 'Описание')

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/create.html')


    def test_view_uses_correct_template2(self):
        response = self.client.get(reverse('pometkorgi'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/pometkorgi.html')

    def test_view_uses_correct_template3(self):
        response = self.client.get(reverse('our_dog'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post/our_dog.html')

