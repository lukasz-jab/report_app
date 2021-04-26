from django.shortcuts import render
from profiles.models import Profile
from django.http import JsonResponse
from .utils import get_report_image
from .models import Report
from django.views.generic import ListView, DetailView
from .forms import ReportForm
# Create your views here.

class ReportListView(ListView):
    model = Report
    template_name = 'reports/main.html'

class ReportDetailView(DetailView):
    model = Report
    template_name = 'reports/detail.html'


def create_report_view(request):
    if request.is_ajax():
        name = request.POST.get('name')
        remarks = request.POST.get('remarks')
        image = request.POST.get('image')
        img = get_report_image(image)
        author = Profile.objects.get(user=request.user)
        Report.objects.create(name=name, remarks=remarks, image=img, author=author)
    return JsonResponse({})

# def create_report_view(request):
#     form = ReportForm(request.POST or None)
#     if request.is_ajax():
#         image = request.POST.get('image')
#         img = get_report_image(image)
#         author = Profile.objects.get(user=request.user)
#
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.image = img
#             instance.author = author
#             instance.save()
#
#     return JsonResponse({})

