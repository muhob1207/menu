# menu/templatetags/menu_tags.py
from django import template
from menu_app.models import MenuItem
from django.utils.html import format_html
from django.urls import resolve
from django.urls import reverse

register = template.Library()

@register.simple_tag
def draw_menu(menu_name, request):
    #Получаем меню по названию из БД (только 1 запрос в БД)
    menu_items = MenuItem.objects.filter(name=menu_name)
    #Получаем ссылку текущей страницы
    current_url = request.path
    #Получаем строку, отрадающую полный путь к пункту меню, соответствующему текущей странице
    link_ancestry = get_link_ancestry(menu_items, current_url, 0, '')['link_ancestry']
    #Показываем меню и все подчиненные пункты
    return render_menu(menu_items, current_url, 0, '', link_ancestry)


def get_link_ancestry(menu_items, current_url, level, ancestry):
    link_ancestry = None
    run = True
    #Проходим по каждому пункту, имеющему один и тот же родительский пункт
    for n, item in enumerate(menu_items):
        #Получаем строку - путь к данному пункту
        item_ancestry = ancestry + '__' + str(level) + '_' + str(n)

        #Смотрим, не определен ли уже путь к пункту, соответствующему текущей странице
        if run:
            #Смотрим, равна ли ссылка на этот пункт ссылке текущей странтицы
            if '/' + item.url == current_url:
                #Если равна, то путь найден
                link_ancestry = item_ancestry
                #Ставим run = False чтобы прервать все родительские функции
                run = False
                #Прерываем цикл
                break
                
            #Смотрим, есть ли у пункта дочерние пункты
            if item.children.exists():
                #Если есть, то запускаем по ним текущую функцию
                res = get_link_ancestry(item.children.all(), current_url, level+1, item_ancestry)

                link_ancestry = res['link_ancestry']
                run = res['run']
        
    return {'link_ancestry':link_ancestry, 'run':run}
    

    


def render_menu(menu_items, current_url, level, ancestry, link_ancestry):
    result = '<ul>'

    #Проходим по каждому пункту из меню
    for n, item in enumerate(menu_items):
        #Получаем путь к данному пункту и ссылку на данный пункт
        item_ancestry = ancestry + '__' + str(level) + '_' + str(n)
        url = reverse(item.url[:-1])  


        if link_ancestry.startswith(item_ancestry):
            #Если путь к данному пункту совпадает с началом пути пункта соответствующего текущей странице, то дочерние пункты данного пункта разворачиваем
            if link_ancestry != item_ancestry:
                result += f'<li><details open><summary><a href="{url}">{item.name}</a></summary>'
            #Если путь к данному пункту равен пути пункта соотвествующего текущей странице, то раскрываем все его подпункты и помечаем желтым цветом
            else:
                result += f'<li><details open><summary><a style="background-color: yellow;" href="{url}">{item.name}</a></summary>'
        #Если путь к данному пункту не совпадает с началом пути пункта текущей страницы, то его подпункты не раскрываем
        else:
            result += f'<li><details><summary><a href="{url}">{item.name}</a></summary>'

        #Запускаем эту же функцию для подпунктов данного пункта если они есть
        if item.children.exists():
            result += render_menu(item.children.all(),current_url, level + 1, item_ancestry, link_ancestry)
        result += '</details></li>'

    result += '</ul>'

    return format_html(result)