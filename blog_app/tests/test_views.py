from django.test import TestCase, Client
from django.shortcuts import reverse
from django.contrib.auth.models import User
from blog_app.models import Post, Entry



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="abdulrahman", password='1Aa@14105810')
        self.client.login(username='abdulrahman', password='1Aa@14105810')
        self.object = Post.objects.create(
            title = 'test title',
            owner = self.user)
        # self.entry = Entry.objects.get_or_create(id=entry_id)



    def test_home(self):

        response = self.client.get(reverse('blog_app:index'))
        self.assertEquals(response.status_code, 200)



    def test_post(self):
        response = self.client.get(
            reverse('blog_app:post', kwargs={'post_id': self.object.id}))
        self.assertEquals(response.status_code, 200)


    def test_posts(self):
        response = self.client.get(reverse('blog_app:posts'))
        self.assertEquals(response.status_code, 200)


    def test_create_post(self):
        data = {
            'title': 'Created title',
        }

        response = self.client.post(
            reverse('blog_app:create_post'), data)
        self.assertEqual(response.status_code, 302)


    def test_edit_post(self):
        response = self.client.get(
            reverse('blog_app:edit_post', kwargs={'post_id': self.object.id}))
        self.assertEquals(response.status_code, 200)


    def test_delete_post(self):
        response = self.client.post(
            reverse('blog_app:delete_post', kwargs={'post_id': self.object.id}))
        self.assertEquals(response.status_code, 302)

    

    def test_create_entry(self):

        response = self.client.post(
            reverse('blog_app:new_entry', kwargs={'post_id': self.object.id}), {'text': 'The Catcher in the Rye'})

        self.assertEqual(response.status_code, 302)

    def test_edit_entry(self):

        # entry = Entry.objects.get(id)
        # post = Post.objects.create(
        #     title='test title',
        #     owner=self.user)
        # self.object = entry.self.object

        # post = entry.post
        # entry = Entry.objects.get(entry_id=id, post_id=self.object.id)


        response = self.client.post(
            reverse('blog_app:edit_entry', kwargs={'entry_id': id}), {'text': 'The Catcher', 'post_id': self.object.id})

        self.assertEqual(response.status_code, 302)
