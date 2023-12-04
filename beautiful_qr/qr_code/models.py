from django.db import models


class QR(models.Model):
    link = models.TextField(
        "Ссылка",
        help_text='Введите текст поста'
    )
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        "Картинка",
        help_text='Прикрепите картинку',
        upload_to="",
    )
    qurl = models.TextField("Путь к коду", blank=True)
    qr = models.ImageField("QR-код", blank=True)
