from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    description = models.TextField(verbose_name="Описание категории", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


from django.db import models


class Project(models.Model):
    category = models.ForeignKey(Category, related_name='projects', on_delete=models.SET_NULL, null=True,
                                 verbose_name="Категория")
    title = models.CharField(max_length=200, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание проекта")
    goal = models.TextField(verbose_name="Цель")
    result = models.TextField(verbose_name="Результат")
    xp_download_link = models.URLField(verbose_name="Ссылка для загрузки XP", blank=True)
    contact_email = models.EmailField(verbose_name="Контактный email")
    video = models.FileField(upload_to='videos/', null=True, blank=True, verbose_name="Видео проекта")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"


class ProjectPhoto(models.Model):
    project = models.ForeignKey(Project, related_name='photos', on_delete=models.CASCADE, verbose_name="Проект")
    photo = models.ImageField(upload_to='photos/', verbose_name="Фото проекта")

    class Meta:
        verbose_name = "Фотография проекта"
        verbose_name_plural = "Фотографии проекта"


class CategoryNews(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категории_Новости"
        verbose_name_plural = "Категории_Новости"

class News(models.Model):
    category = models.ForeignKey(CategoryNews, related_name='projects', on_delete=models.SET_NULL, null=True,
                                 verbose_name="Новости")
    title = models.CharField(max_length=200, verbose_name="Название новости")
    description = models.TextField(verbose_name="Описание новости")
    photo = models.ImageField(upload_to='photo/', null=True, blank=True, verbose_name="Фото проекта")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новости"
        verbose_name_plural = "Новости"



from django.db import models

from django.db import models

class CaseCard(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название работы")
    category_tags = models.ManyToManyField('CategoryTag', related_name='case_cards', verbose_name="Категории")
    client_business_task = models.TextField(verbose_name="Бизнес задача клиента")
    photo = models.ImageField(upload_to='case_photos/', null=True, blank=True, verbose_name="Фото")


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кейс"
        verbose_name_plural = "Кейсы"

class CategoryTag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Имя тега")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория-Кейс"
        verbose_name_plural = "Категория-Кейсы"


