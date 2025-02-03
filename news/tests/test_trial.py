from django.test import TestCase
from news.models import News

# Импортируем декоратор skip из unittest
from unittest import skip

# Используем декоратор skip для пропуска всего класса тестов
@skip("Эти тесты временно отключены")
class TestNews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.news = News.objects.create(
            title='Заголовок новости',
            text='Тестовый текст',
        )

    def test_successful_creation(self):
        news_count = News.objects.count()
        self.assertEqual(news_count, 1)

    def test_title(self):
        self.assertEqual(self.news.title, 'Заголовок новости')