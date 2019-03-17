from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Category, Product
# Create your views here.
class ProductListview(ListView):

    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    paginate_by = 1

product_list = ProductListview.as_view()

class CategoryListView(ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'products'
    paginate_by = 1

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

category = CategoryListView.as_view()

def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product':product
    }
    return render(request, 'catalog/product.html', context)
