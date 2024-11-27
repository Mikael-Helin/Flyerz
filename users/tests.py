from django.test import TestCase
from users.forms import UserRegisterForm

# Create your tests here.
class UserRegisterFormTest(TestCase):
    def test_valid_data(self):
        form = UserRegisterForm({
            'username': 'testuser',
            'email': 'test@email.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertTrue(form.is_valid())
        user = form.save()
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@email.com')

    def test_blank_data(self):
        form = UserRegisterForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'username': ['This field is required.'],
            'email': ['This field is required.'],
            'password1': ['This field is required.'],
            'password2': ['This field is required.'],
        })

    def test_invalid_email(self):
        form = UserRegisterForm({
            'username': 'testuser',
            'email': 'test',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'email': ['Enter a valid email address.'],
        }) 
    
    def test_unique_email(self):
        form = UserRegisterForm({
            'username': 'testuser',
            'email': 'test@email.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        form.save()
        form = UserRegisterForm({
            'username': 'testuser2',
            'email': 'test@email.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'email': ['This email is already in use.'],
        })

    def test_long_email(self):
        form = UserRegisterForm({
            'username': 'testuser',
            'email': 'a' * 245 + '@email.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'email': ['Ensure this value has at most 254 characters (it has 255).'],
        })

    def test_password_mismatch(self):
        form = UserRegisterForm({
            'username': 'testuser',
            'email': 'test@email.com',
            'password1': 'testpassword',
            'password2': 'wrongpassword'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'password2': ['The two password fields didn’t match.'],
        }) 

    def test_password_length(self):
        form = UserRegisterForm({
            'username': 'testuser',
            'email': 'testuser@email.com',
            'password1': 'short',
            'password2': 'short'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'password2': ['This password is too short. It must contain at least 8 characters.'],
        }) 
        

    def test_username_length(self):
        form = UserRegisterForm({
            'username': 'sh',
            'email': 'test@email.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'username': ['Your username must contain at least 3 characters.'],
        }) 
        
    def test_unique_username(self):
        form = UserRegisterForm({
            'username': 'testuser',
            'email': 'test@email.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        form.save()
        form = UserRegisterForm({
            'username': 'testuser',
            'email': 'test2@email.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'username': ['A user with that username already exists.'],
        }) 

    def test_invalid_username(self):
        form = UserRegisterForm({
            'username': 'testuser¤',
            'email': 'test@email.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'username': ['Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.'],
        })

    def test_long_username(self):
        form = UserRegisterForm({
            'username': 'a' * 151,
            'email': 'test@email.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        self.assertFalse(form.is_valid())