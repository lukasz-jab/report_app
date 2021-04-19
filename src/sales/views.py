from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Sale
from .forms import SalesSearchForm
import pandas as pd
# Create your views here.

def home_view(request):
    sales_df = None
    positions_df = None
    form = SalesSearchForm(request.POST or None)
    if request.method == 'POST':
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        chart_type = request.POST.get('chart_type')
        qs = Sale.objects.filter(created__date__lte=date_to, created__date__gte=date_from)
        if len(qs) > 0:
            sales_df = pd.DataFrame(qs.values())
            positions = []
            for sale in qs:
                for position in sale.get_positions():
                    obj = {
                        'position_id': position.id,
                        'product': position.product.name,
                        'quantity': position.quantity,
                        'price': position.price,
                    }
                    positions.append(obj)
            positions_df = pd.DataFrame(positions)
            sales_df = sales_df.to_html()
            positions_df = positions_df.to_html()
    context = {
    'form': form,
    'sales_df': sales_df,
    'positions_df': positions_df

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

