from django.contrib import admin
from .models import Sortirovka,Menu,SuperRubric,SubRubric


@admin.register(Sortirovka)
class SortirovkaAdmin(admin.ModelAdmin):
    field = ('ingredient_name')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name','rubric','weight','image','price','available',)
    list_editable = ('image','rubric','weight','price','available',)
    filter_horizontal = ['ingredient']
    prepopulated_fields = {'slug':('name',)}


class SuperRubricInline(admin.TabularInline):
    model = SubRubric


class SuperRubricAdmin(admin.ModelAdmin):

    exclude = ['super_rubric']
    inlines = [SuperRubricInline]

admin.site.register(SuperRubric,SuperRubricAdmin)




