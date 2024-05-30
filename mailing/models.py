from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(verbose_name='email')
    name = models.CharField(max_length=150, verbose_name='Имя')
    surname = models.CharField(max_length=150, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=150, verbose_name='Отчество')
    comment = models.TextField(verbose_name='комментарий')

    def __str__(self):
        return f'{self.surname} {self.name}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    subject = models.CharField(max_length=150, verbose_name='тема письма')
    message = models.TextField(verbose_name='сообщение')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'сообщение для рассылки'
        verbose_name_plural = 'сообщения для рассылки'


class Mailing(models.Model):
    CREATED = 'created'
    COMPLETED = 'completed'
    STARTED = 'started'
    STATUS_VARIANTS = {
        CREATED: 'создана',
        COMPLETED: 'завершена',
        STARTED: 'запущена',
    }

    DAILY = 'daily'
    WEEKLY = 'weekly'
    MONTHLY = 'monthly'
    REGULARITY_VARIANTS = {
        DAILY: 'раз в день',
        WEEKLY: 'раз в неделю',
        MONTHLY: 'раз в месяц',
    }
    mail_time = models.DateTimeField(verbose_name='дата и время рассылки')
    regularity = models.CharField(max_length=50, choices=REGULARITY_VARIANTS, verbose_name='периодичность')

    status = models.CharField(max_length=50, choices=STATUS_VARIANTS, default=CREATED, verbose_name='статус рассылки')

    message = models.ForeignKey(Message, on_delete=models.SET_NULL, **NULLABLE, verbose_name='сообщение')
    client = models.ManyToManyField(Client, verbose_name='клиент')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class MailingAttempts(models.Model):
    SUCCESS = 'successful'
    FAIL = 'failed'
    STATUS_VARIANTS = {
        SUCCESS: 'успешно',
        FAIL: 'неуспешно',
    }

    last_attempt_time = models.DateTimeField(verbose_name='дата и время последней попытки')
    status = models.CharField(max_length=50, choices=STATUS_VARIANTS, verbose_name='статус рассылки')
    server_response = models.CharField(max_length=150, verbose_name='ответ почтового сервера')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='рассылка')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'попытка рассылки'
        verbose_name_plural = 'попытки рассылки'
