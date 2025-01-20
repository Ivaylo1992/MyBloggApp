from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse
from simpleblog.posts.models import Post
from model_bakery import baker


class HomePageTest(TestCase):
    def setUp(self):
        self.post_one = baker.make(Post)
        self.post_two = baker.make(Post)

    def test_homepage_returns_correct_response(self):
        response = self.client.get(reverse('homepage'))

        self.assertTemplateUsed(response, "posts/index.html",)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get(reverse('homepage'))

        self.assertContains(response, self.post_one.title)
        self.assertContains(response, self.post_two.title,)