from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from inside.models import SanPham
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
	
	cart = Cart(request)  # create a new cart object passing it the request object 
	product = get_object_or_404(SanPham, id=product_id) 
	
	if 'Th_don_gia' not in request.POST:
		price=0
	else:
		price=request.POST['Th_don_gia']
	form = CartAddProductForm(request.POST)
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(product=product, price=product.don_gia_ban, quantity=int(cd['quantity']), update_quantity=cd['update'])
	return redirect('cart:cart_detail')


def cart_remove(request, product_id):
	cart = Cart(request)
	product = get_object_or_404(SanPham, id=product_id)
	cart.remove(product)
	return redirect('cart:cart_detail')


def cart_detail(request):
	print('------------------------------------')
	cart = Cart(request)
	for item in cart:
		item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
		print(item['update_quantity_form'])
	return render(request, 'cart/detail.html', {'cart': cart})
