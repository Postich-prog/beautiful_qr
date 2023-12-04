import shutil
import tempfile

from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase, override_settings
from django.urls import reverse
from qr_code.forms import QRForm
from qr_code.models import QR

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)


@override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
class QrCreateFormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.qr = QR.objects.create(
            link='Тестовая ссылка'
        )
        cls.form = QRForm()
        cls.small_pic = (
            b'\x47\x49\x46\x38\x39\x61\x02\x00'
            b'\x01\x00\x80\x00\x00\x00\x00\x00'
            b'\xFF\xFF\xFF\x21\xF9\x04\x00\x00'
            b'\x00\x00\x00\x2C\x00\x00\x00\x00'
            b'\x02\x00\x01\x00\x00\x02\x02\x0C'
            b'\x0A\x00\x3B'
        )

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)

    def setUp(self):
        # Устанавливаем данные для тестирования
        # Создаём экземпляр клиента. Он неавторизован.
        self.guest_client = Client()

    def test_create_qr(self):
        """Валидная форма создает QR-код"""
        qr_count = QR.objects.count()

        uploaded = SimpleUploadedFile(
            name='small.png',
            content=self.small_pic,
            content_type='image/png'
        )

        form_data = {
            'link': 'Тестовая ссылка 2',
            'image': uploaded,
        }
        response = self.guest_client.post(
            reverse('qr_create'),
            data=form_data,
            follow=True
        )
        self.assertRedirects(
            response,
            reverse(
                'qr_code_detail',
                kwargs={'pk': self.qr.id+1}
            )
        )
        self.assertEqual(QR.objects.count(), qr_count + 1)
        self.assertTrue(
            QR.objects.filter(
                link='Тестовая ссылка 2',
                image='small.png',
                qurl='smallQR.png'
            ).exists()
        )
