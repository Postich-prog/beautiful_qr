from django.test import TestCase, Client
from django.urls import reverse
from ..models import QR


class StaticURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.qr = QR.objects.create(
            link='тестовая ссылка'
        )

    def setUp(self):
        # Устанавливаем данные для тестирования
        # Создаём экземпляр клиента. Он неавторизован.
        self.guest_client = Client()

    def test_qr_detail_pages_authorized_uses_correct_template(self):
        """URL-адреса используют шаблон qr_code_detail.html."""
        response = self.guest_client.\
            get(reverse('qr_code_detail', kwargs={'pk': self.qr.id}))
        self.assertTemplateUsed(response, 'qr_code_detail.html')

    def test_qr_detail_show_correct_context(self):
        """Шаблон qr_code_detail сформирован с правильным контекстом."""
        response = self.guest_client.get(reverse(
            'qr_code_detail',
            kwargs={'pk': self.qr.id})
        )
        first_object_id = response.context['qr'].pk
        self.assertEqual(first_object_id, self.qr.id)
