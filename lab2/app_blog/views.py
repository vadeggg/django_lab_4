from django.shortcuts import render
from django.views.generic import TemplateView
# Створіть свої представлення тут.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'app_blog/index.html', context=None)