from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SalesSearchForm
# Create your views here.

def home_view(request):
    form = SalesSearchForm(request.POST or None)
    context = {
    'form': form
    }
    return render(request, 'sales/home.html', context)

class SalesView(ListView):
    model = Sale
    template_name = 'sales/main.html'

# def sale_list_view(request):
#     qs = Sale.objects.all()
#     context = {
#         'object_list': qs
#     }
#     return render(request, 'sales/main.html', context)

class SalesDetailView(DetailView):
    model = Sale
    template_name = 'sales/detail.html'

# def sale_detail_view(request, **kwargs):
#     pk = kwargs.get('pk')
#     # obj = Sale.objects.get(id=pk)
#     obj = get_object_or_404(Sale, id=pk)
#     context = {
#         'obj': obj
#     }
#     return render(request, 'sales/detail.html', context)

