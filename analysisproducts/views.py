from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category
   
class ProductList(ListView):
    model= Product
    #ordering = '-pk'
    paginate_by = 12
    
    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_product_count'] = Product.objects.filter(
            category=None).count()
        return context

class ProductDetail(DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_product_count'] = Product.objects.filter(
            category=None).count()
        return context 

def category_page(request, slug):
    if slug == 'no_category':
        category ='기타'
        product_list = Product.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        product_list =  Product.objects.filter(category=category)
    
    return render(
        request,
        'analysisproducts/product_list.html',
        {
            'product_list': product_list,
            'categories': Category.objects.all(),
            'no_category_product_count': Product.objects.filter(category=None).count(),
            'category': category,
        }

    )  
