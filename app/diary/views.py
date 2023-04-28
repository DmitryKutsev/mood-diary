from core.models import Diary
from core.models import DiaryEntry
from django.shortcuts import render
from django.views.generic.base import View


# Create your views here.


class DiariesListView(View):
    """Diaries view"""

    def get(self, request):
        diaries = Diary.objects.all()  # .filter(patient=self.request.user)
        return render(request, "diary/diaries_list.html", {"diary_list": diaries})


class DiaryDetailsView(View):
    """Diary's detailed view"""

    def get(self, request, pk):
        diary = Diary.objects.get(id=pk)
        entries_list = diary.entries.all()
        return render(
            request,
            "diary/diary_details.html",
            {"diary": diary, "entries": entries_list},
        )
