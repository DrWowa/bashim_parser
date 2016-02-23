# -*- coding: utf-8 -*-
from django.db import models


class BashImData(models.Model):
    number = models.PositiveIntegerField('Номер цитаты')
    text = models.TextField('Текст цитаты')

    class Meta:
        verbose_name = 'Цитата bash.im'
        verbose_name_plural = 'Цитаты bash.im'

    def __str__(self):
        return 'Цитата #{}'.format(self.number)
