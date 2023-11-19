from django.db import models


class QR(models.Model):
    link = models.TextField('Ссылка')
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        'Картинка',
        upload_to='',
    )
    qurl = models.TextField(
        'Путь к коду',
        blank=True
    )
    qr = models.ImageField(
        'QR-код',
        blank=True
    )
