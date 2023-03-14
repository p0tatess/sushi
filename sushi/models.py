from django.db import models


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, unique=True, verbose_name='Название')
    order = models.SmallIntegerField(default=0,db_index=True,verbose_name='Порядок')
    super_rubric = models.ForeignKey('SuperRubric',on_delete=models.PROTECT,null=True,blank=True,verbose_name='Надрубрика')

class SuperRubricManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_rubric__isnull=True)

class SuperRubric(Rubric):
    objects = SuperRubricManager()

    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        ordering = ('order','name')
        verbose_name = 'Надрубрика'
        verbose_name_plural = 'Надрубрики'


class SubRubricManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(super_rubric__isnull=False)

class SubRubric(Rubric):
    object = SubRubricManager()

    def __str__(self):
        return '%s - %s' % ( self.super_rubric.name ,self.name )

    class Meta:
        proxy = True
        ordering = ('super_rubric__order','super_rubric__name','order','name')
        verbose_name = 'Подрубрика'
        verbose_name_plural = 'Подрубрики'



class Sortirovka(models.Model):
    ingredient_name = models.CharField(max_length=255)

    class Meta:
        ordering = ['ingredient_name']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self):
        return self.ingredient_name


class Menu(models.Model):
    name = models.CharField(max_length=100,verbose_name='Название')
    slug = models.SlugField(db_index=True)
    rubric = models.ForeignKey(SubRubric, on_delete=models.PROTECT, verbose_name='Рубрика')
    image = models.ImageField(blank=True, verbose_name='Изображение')
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='Цена')
    quant = models.PositiveSmallIntegerField(blank=True,null=True,verbose_name='Количество')
    weight = models.PositiveSmallIntegerField(verbose_name='Вес')
    centimeters = models.PositiveSmallIntegerField(blank=True,null=True,verbose_name='см')
    available = models.BooleanField(default=True,verbose_name='Наличие')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True,verbose_name='Последнее обновление')
    ingredient = models.ManyToManyField(Sortirovka,blank=True,verbose_name='Ингредиенты')

    class Meta:
        ordering = ['name']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.name
