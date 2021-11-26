from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Laptop
from django.conf import settings

        
class LaptopModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_laptop = Laptop.objects.create(
            owner = test_user,
            brand = 'Title of Blog',
            description = 'Words about the blog'
        )
        test_laptop.save()

    def test_blog_content(self):
        laptop = Laptop.objects.get(id=1)

        self.assertEqual(str(laptop.owner), 'tester')
        self.assertEqual(laptop.brand, 'Title of Blog')
        self.assertEqual(laptop.description, 'Words about the blog')

class APITest(APITestCase):
    def test_list(self):
        response = self.client.get(reverse('laptop_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_laptop = Laptop.objects.create(
            author = test_user,
            title = 'Title of Blog',
            body = 'Words about the blog'
        )
        test_laptop.save()

        response = self.client.get(reverse('laptop_detail', args=[1]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id':1,
            'brand': test_laptop.brand,
            'description': test_laptop.description,
            'owner': test_user.id,
        })


    def test_create(self):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        url = reverse('laptop_list')
        data = {
            "brand":"Testing is Fun!!!",
            "description":"when the right tools are available",
            "owner":test_user.id,
        }

        response = self.client.laptop(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED, test_user.id)

        self.assertEqual(Laptop.objects.count(), 1)
        self.assertEqual(Laptop.objects.get().title, data['title'])

    def test_update(self):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_laptop = Laptop.objects.create(
            owner = test_user,
            brand = 'Title of Blog',
            description = 'Words about the blog'
        )

        test_laptop.save()

        url = reverse('laptop_detail',args=[test_laptop.id])
        data = {
            "brand":"Testing is Still Fun!!!",
            "owner":test_laptop.owner.id,
            "description":test_laptop.description,
        }

        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK, url)

        self.assertEqual(Laptop.objects.count(), test_laptop.id)
        self.assertEqual(Laptop.objects.get().brand, data['brand'])


    def test_delete(self):
        """Test the api can delete a laptop."""

        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_laptop = Laptop.objects.create(
            owner = test_user,
            brand = 'Title of Blog',
            description = 'Words about the blog'
        )

        test_laptop.save()

        laptop = Laptop.objects.get()

        url = reverse('laptop_detail', kwargs={'pk': laptop.id})


        response = self.client.delete(url)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT, url)
