from django.test import TestCase
from simpleblog.posts.models import Post
from http import HTTPStatus
from model_bakery import baker
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class PostModelTest(TestCase):
    def test_post_model_exist(self):
        posts = Post.objects.count()
        self.assertEqual(posts, 0)

    def test_string_rep_of_objects(self):
        post = baker.make(Post)

        self.assertEqual(str(post), post.title)
        self.assertTrue(isinstance(post, Post))


class HomePageTest(TestCase):
    def setUp(self):
        self.post_one = baker.make(Post)
        self.post_two = baker.make(Post)

    def test_homepage_returns_correct_response(self):
        response = self.client.get("/")

        self.assertTemplateUsed(response, "posts/index.html",)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_homepage_returns_post_list(self):
        response = self.client.get("/")

        self.assertContains(response, self.post_one.title)
        self.assertContains(response, self.post_two.title,)


class DetailPageTest(TestCase):
    def setUp(self):
        self.post = baker.make(Post)

    def test_detail_page_returns_correct_response(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed("posts/detail.html")

    def test_detail_page_returns_correct_content(self):
        response = self.client.get(self.post.get_absolute_url())

        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.content)


class PostAuthorTest(TestCase):
    def setUp(self):
        self.user = baker.make(UserModel)
        self.post = Post.objects.create(
            title='Test title',
            content='Test content',
            author=self.user,
        )

    def test_author_isinstance_of_user_model(self):
        self.assertTrue(isinstance(self.user, UserModel))
    
    def test_post_belongs_to_user(self):
        self.assertTrue(hasattr(self.post, 'author'))
        self.assertEqual(self.post.author, self.user)