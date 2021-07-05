from django.http import HttpRequest
from django.shortcuts import render
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.template.loader import render_to_string

class HomePageTest(TestCase):
  def test_root_url_resolves_to_home_page_view(self):
    found = resolve('/')
    self.assertEqual(found.func, home_page)

  def test_home_page_uses_home_template(self):
    response = self.client.get('/')
    self.assertTemplateUsed(response, 'home.html')
