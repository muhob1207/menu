
from django.db import models
from django.urls import reverse

class MenuItem(models.Model):
    #В данном случае name должен быть равен названию меню, которе будет использоваться в template_tag {% draw_menu 'name' %}
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, null=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        if self.pk:
            return reverse('admin:menu_app_menuitem_change', args=[str(self.pk)])
        else:
            return reverse('admin:menu_app_menuitem_add')