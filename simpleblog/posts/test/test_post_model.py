from django.test import TestCase
from simpleblog.posts.models import Post
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