from django.test import TestCase
from django.contrib.auth.models import User
from .models import Category, Post


class Test_Create_Post(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        test_user1 = User.objects.create_user(
            username='TestUser1', password='84020299aA!')
        test_post = Post.objects.create(
            category_id=1, title='Test_Post', excerpt='T_Post excerpt',
            content='T_Post content', slug='post-test', author_id=1,
            status='published',)

    def test_blog_content(self):
        post = Post.postobjects.get(id=1)
        category = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'TestUser1')
        self.assertEqual(title, 'Test_Post')
        self.assertEqual(excerpt, 'T_Post excerpt')
        self.assertEqual(content, 'T_Post content')
        self.assertEqual(status, 'published')
        self.assertEqual(str(post), 'Test_Post')
        self.assertEqual(str(category), 'django')
