from django.test import TestCase , Client
from django.urls import reverse
from .models import Post
from django.contrib.auth import get_user_model
# Create your tests here.

class PostTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'test',
            email = 'tomas@gmail.com',
            password = 'tomas',
        )

        self.post = Post.objects.create(
            title = 'good title',
            content = 'testing',
            author = self.user,
        )

    def test_string(self):
        post = Post(title='simple title')
        self.assertEqual(str(post), post.title)

    def test_content(self):
        self.assertEqual(f'{self.post.title}', 'good title')
        self.assertEqual(f'{self.post.author}', 'test')
        self.assertEqual(f'{self.post.content}', 'testing')

    def test_post_list_view(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code , 200)
        self.assertContains(res , 'testing')
        self.assertTemplateUsed(res , 'blog/home.html')

    def test_post_detail(self):
        res = self.client.get('/post/1/')
        no_res = self.client.get('/post/100000/')
        self.assertEqual(res.status_code , 200)
        self.assertEqual(no_res.status_code , 404)
        self.assertContains(res , 'testing')
        self.assertTemplateUsed(res,'blog/post_detail.html')
