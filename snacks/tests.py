from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from snacks.models import Snack


class TestSnacks(TestCase):

  def setUp(self):
    self.user = get_user_model().objects.create(
      username='tester',
      email = 'tester@email.com',
      password = 'fish'
    )

    self.snack = Snack.objects.create(
      name = 'fishcakes',
      purchaser = self.user,
      description = 'yummy'
    )
  
  def test_template(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    self.assertTemplateUsed(response, 'base.html')
    self.assertTemplateUsed(response, 'snack_list.html')

  def test_status_code(self):
    url = reverse('snack_list')
    response = self.client.get(url)
    assert response.status_code == 200

  def test_snack_string(self):
    self.assertEqual((self.snack.name), 'fishcakes')
    self.assertEqual(str(self.snack), 'fishcakes')

  def test_user_name(self):
    self.assertEqual(self.user.username, 'tester')

  def test_user_email(self):
    self.assertEqual(self.user.email, 'tester@email.com')

  def test_user_password(self):
    self.assertEqual(self.user.password, 'fish')

  def test_user_password_not(self):
    self.assertNotEqual(self.user.password, 'incorrect password')

  def test_snack_purchaser(self):
    self.assertEqual(str(self.snack.purchaser), self.user.username)

  def test_snack_description(self):
    self.assertEqual(self.snack.description, 'yummy')

  def test_snack_description_not(self):
    self.assertNotEqual(self.snack.description, 'so gross') 