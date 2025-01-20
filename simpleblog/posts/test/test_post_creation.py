from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.http.request import HttpRequest
from model_bakery import baker
from django.contrib.auth import get_user_model

from simpleblog.posts.forms import PostCreationForm
from simpleblog.posts.models import Post

UserModel = get_user_model()


class PostCreationTest(TestCase):
    def setUp(self):
        self.url = reverse('create_post')
        self.template_name = 'posts/create_post.html'
        self.form_class = PostCreationForm
        self.title = 'Sample Title'
        self.content = 'Sample body for this sample post'

    def test_post_creation_page_exists(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, self.template_name)

        form = response.context.get('form', None)

        self.assertIsInstance(form, self.form_class)
    
    def test_post_creation_form_creates_post(self):
        post_request = HttpRequest()

        post_request.user = baker.make(UserModel)

        post_data = {
            'title': self.title,
            'content': self.content,
        }

        post_request.POST = post_data

        form = self.form_class(post_request.POST)
        self.assertTrue(form.is_valid())

        post_obj = form.save(commit=False)
        self.assertIsInstance(post_obj, Post)

        post_obj.author = post_request.user

        post_obj.save()

        self.assertEqual(Post.objects.count(), 1)