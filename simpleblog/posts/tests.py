from django.test import TestCase
from simpleblog.posts.models import Post
from http import HTTPStatus


class PostModelTest(TestCase):
    def test_post_model_exist(self):
        posts = Post.objects.count()
        self.assertEqual(posts, 0)

    def test_string_rep_of_objects(self):
        post = Post.objects.create(
            title="test post",
            content="test content",
        )

        self.assertEqual(str(post), post.title)


class HomePageTest(TestCase):
    def setUp(self):
        post_one = Post.objects.create(
            title="post 1",
            content="Django REST framework is a powerful\
                  and flexible toolkit for building Web APIs.",
        )

        post_two = Post.objects.create(
            title="post 2",
            content="Django REST framework is a powerful\
                  and flexible toolkit for building Web APIs.",
        )

    def test_homepage_returns_correct_response(self):
        response = self.client.get("/")

        self.assertTemplateUsed(
            response,
            "posts/index.html",
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get("/")

        self.assertContains(
            response,
            'post 1'
        )
        
        self.assertContains(
            response,
            'post 2',
        )
