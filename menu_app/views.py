# views.py
from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from menu_app import models


class HomePage(TemplateView):
    template_name = 'index.html'





class Menu1(TemplateView):
    template_name = 'menu1.html'

class Menu2(TemplateView):
    template_name = 'menu2.html'

class Menu3(TemplateView):
    template_name = 'menu3.html'






class Menu1Submenu1(TemplateView):
    template_name = 'menu1_submenu1.html'

class Menu1Submenu2(TemplateView):
    template_name = 'menu1_submenu2.html'


class Menu2Submenu1(TemplateView):
    template_name = 'menu2_submenu1.html'

class Menu2Submenu2(TemplateView):
    template_name = 'menu2_submenu2.html'

class Menu3Submenu1(TemplateView):
    template_name = 'menu3_submenu1.html'

class Menu3Submenu2(TemplateView):
    template_name = 'menu3_submenu2.html'




class Menu1Submenu1Submenu1(TemplateView):
    template_name = 'menu1_submenu1_submenu1.html'

class Menu1Submenu1Submenu2(TemplateView):
    template_name = 'menu1_submenu1_submenu2.html'

class Menu1Submenu1Submenu3(TemplateView):
    template_name = 'menu1_submenu1_submenu3.html'


class Menu1Submenu2Submenu1(TemplateView):
    template_name = 'menu1_submenu2_submenu1.html'

class Menu1Submenu2Submenu2(TemplateView):
    template_name = 'menu1_submenu2_submenu2.html'

class Menu1Submenu2Submenu3(TemplateView):
    template_name = 'menu1_submenu2_submenu3.html'



class Menu2Submenu1Submenu1(TemplateView):
    template_name = 'menu2_submenu1_submenu1.html'

class Menu2Submenu1Submenu2(TemplateView):
    template_name = 'menu2_submenu1_submenu2.html'

class Menu2Submenu1Submenu3(TemplateView):
    template_name = 'menu2_submenu1_submenu3.html'


class Menu2Submenu2Submenu1(TemplateView):
    template_name = 'menu2_submenu2_submenu1.html'

class Menu2Submenu2Submenu2(TemplateView):
    template_name = 'menu2_submenu2_submenu2.html'

class Menu2Submenu2Submenu3(TemplateView):
    template_name = 'menu2_submenu2_submenu3.html'




class Menu3Submenu1Submenu1(TemplateView):
    template_name = 'menu3_submenu1_submenu1.html'

class Menu3Submenu1Submenu2(TemplateView):
    template_name = 'menu3_submenu1_submenu2.html'

class Menu3Submenu1Submenu3(TemplateView):
    template_name = 'menu3_submenu1_submenu3.html'


class Menu3Submenu2Submenu1(TemplateView):
    template_name = 'menu3_submenu2_submenu1.html'

class Menu3Submenu2Submenu2(TemplateView):
    template_name = 'menu3_submenu2_submenu2.html'

class Menu3Submenu2Submenu3(TemplateView):
    template_name = 'menu3_submenu2_submenu3.html'






class Menu1Submenu1Submenu1Submenu1(TemplateView):
    template_name = 'menu1_submenu1_submenu1_submenu1.html'