import urllib

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from core.models import Diary, User


class HomePageView(TemplateView):
    template_name = 'home.html'

from django.views import generic

class DiaryListView(ListView):
    template_name = "diary/diaries.html"

    def get_queryset(self):
        try:
            return Diary.objects.filter(author=self.request.user)
        except User.DoesNotExist:
            return
class DiaryDetailView(DetailView):
    model = Diary
    template_name = 'diary/diary_details.html'
