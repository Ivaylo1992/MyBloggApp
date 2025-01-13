from django.test import TestCase
from simpleblog.posts.models import Post
from django.db.models import QuerySet

class PostModelTest(TestCase):
    def test_post_model_exist(self):
        posts = Post.objects.count()
        self.assertEqual(posts, 0)
        
