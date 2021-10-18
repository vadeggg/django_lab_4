from django.db import models

# Create your models here.
from django.utils import timezone
from django.db import models
from django.urls import reverse
# Create your models here.
# mysite /urls.py
class Category(models.Model):
    category = models.CharField('Категорія',
                                max_length=250, help_text='Максимум 250 символів')

    slug = models.SlugField('Слаг', unique=True, null=True)

    def get_absolute_url(self):
        try:
            url = reverse('articles-category-list',
                          kwargs={'slug': self.slug})
            return url
        except:
            url = "/"
            return url
    class Meta:
        verbose_name = 'Категорія для публікації'
        verbose_name_plural = 'Категорії для публікацій'
        def __str__(self):
            return self.category


class Article(models.Model):
    title = models.CharField('Заголовок', max_length=250,
                              help_text='Максимум 250 символів')

    description = models.TextField(blank=True, verbose_name='Опис')

    pub_date = models.DateTimeField('Дата публікації',default=timezone.now)

    slug = models.SlugField('Слаг', unique_for_date='pub_date')

    main_page = models.BooleanField('Головна',
                                    default=False,
                                    help_text='’Показувати на головній сторінці')

    category = models.ForeignKey(Category,
                                related_name='articles',
                                blank=True,
                                null=True,
                                verbose_name='Категорія',
                                on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        try:
            url = reverse('news-detail',
                          kwargs={
                              'year': self.pub_date.strftime("%Y"),
                              'month': self.pub_date.strftime("%m"),
                              'day': self.pub_date.strftime("%d"),
                              'slug': self.slug,
                          })
            return url
        except Exception as e:
            url = "/"
            return url
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Стаття'
        verbose_name_plural = 'Статті'
class ArticleImage(models.Model):
    article = models.ForeignKey(Article,
                                verbose_name='Стаття',
                                related_name='images',
                                on_delete=models.CASCADE)

    image = models.ImageField('Фото', upload_to='photos')

    title = models.CharField('Заголовок', max_length=250,
                            help_text='Максимум 250 символів',
                            blank=True)

    def __str__(self):
        return self.title

    @property
    def filename(self):
        return self.image.name.rsplit('/', 1)[-1]
    class Meta:
        verbose_name = 'Фото для статті'
        verbose_name_plural = 'Фото для статті'
