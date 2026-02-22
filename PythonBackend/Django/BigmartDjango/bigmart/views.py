# bigmart/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum, Count, Q
from django.utils import timezone
from datetime import timedelta
from .models import *
from .forms import *

@login_required
def dashboard(request):
    today = timezone.now().date()
    week_ago = today - timedelta(days=7)
    
    context = {
        'total_products': Product.objects.count(),
        'low_stock_products': Product.objects.filter(stock_quantity__lte=models.F('reorder_level')).count(),
        'total_customers': Customer.objects.count(),
        'today_sales': Sale.objects.filter(sale_date__date=today).aggregate(total=Sum('total_amount'))['total'] or 0,
        'week_sales': Sale.objects.filter(sale_date__date__gte=week_ago).aggregate(total=Sum('total_amount'))['total'] or 0,
        'recent_sales': Sale.objects.all().order_by('-sale_date')[:10],
        'low_stock_items': Product.objects.filter(stock_quantity__lte=models.F('reorder_level'))[:10],
    }
    return render(request, 'bigmart/dashboard.html', context)


# Product Views
@login_required
def product_list(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    
    products = Product.objects.all()
    
    if query:
        products = products.filter(Q(name__icontains=query) | Q(sku__icontains=query))
    
    if category_id:
        products = products.filter(category_id=category_id)
    
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'query': query,
    }
    return render(request, 'bigmart/product_list.html', context)


@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product created successfully!')
            return redirect('product_list')
    else:
        form = ProductForm()
    
    return render(request, 'bigmart/product_form.html', {'form': form, 'title': 'Add Product'})


@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully!')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    
    return render(request, 'bigmart/product_form.html', {'form': form, 'title': 'Edit Product'})


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect('product_list')
    return render(request, 'bigmart/product_confirm_delete.html', {'product': product})


# Customer Views
@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'bigmart/customer_list.html', {'customers': customers})


@login_required
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer created successfully!')
            return redirect('customer_list')
    else:
        form = CustomerForm()
    
    return render(request, 'bigmart/customer_form.html', {'form': form, 'title': 'Add Customer'})


# Sale/POS Views
@login_required
def pos_view(request):
    if request.method == 'POST':
        # Handle sale creation
        cart_items = request.session.get('cart', [])
        if not cart_items:
            messages.error(request, 'Cart is empty!')
            return redirect('pos_view')
        
        # Create sale
        invoice_number = f"INV-{timezone.now().strftime('%Y%m%d%H%M%S')}"
        customer_id = request.POST.get('customer_id')
        payment_method = request.POST.get('payment_method')
        
        total = sum(item['subtotal'] for item in cart_items)
        
        sale = Sale.objects.create(
            invoice_number=invoice_number,
            customer_id=customer_id if customer_id else None,
            cashier=request.user.employee,
            total_amount=total,
            payment_method=payment_method
        )
        
        # Create sale items and update stock
        for item in cart_items:
            product = Product.objects.get(id=item['product_id'])
            SaleItem.objects.create(
                sale=sale,
                product=product,
                quantity=item['quantity'],
                unit_price=item['price'],
                subtotal=item['subtotal']
            )
            product.stock_quantity -= item['quantity']
            product.save()
        
        # Clear cart
        request.session['cart'] = []
        messages.success(request, f'Sale completed! Invoice: {invoice_number}')
        return redirect('sale_detail', pk=sale.id)
    
    products = Product.objects.filter(stock_quantity__gt=0)
    customers = Customer.objects.all()
    cart = request.session.get('cart', [])
    
    context = {
        'products': products,
        'customers': customers,
        'cart': cart,
        'cart_total': sum(item['subtotal'] for item in cart)
    }
    return render(request, 'bigmart/pos.html', context)


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    
    cart = request.session.get('cart', [])
    
    # Check if product already in cart
    for item in cart:
        if item['product_id'] == product_id:
            item['quantity'] += quantity
            item['subtotal'] = item['quantity'] * item['price']
            break
    else:
        cart.append({
            'product_id': product.id,
            'name': product.name,
            'price': float(product.selling_price),
            'quantity': quantity,
            'subtotal': float(product.selling_price) * quantity
        })
    
    request.session['cart'] = cart
    messages.success(request, f'{product.name} added to cart!')
    return redirect('pos_view')


@login_required
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    cart = [item for item in cart if item['product_id'] != product_id]
    request.session['cart'] = cart
    messages.success(request, 'Item removed from cart!')
    return redirect('pos_view')


@login_required
def sale_list(request):
    sales = Sale.objects.all().order_by('-sale_date')
    return render(request, 'bigmart/sale_list.html', {'sales': sales})


@login_required
def sale_detail(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    return render(request, 'bigmart/sale_detail.html', {'sale': sale})


# Supplier Views
@login_required
def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'bigmart/supplier_list.html', {'suppliers': suppliers})


@login_required
def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Supplier created successfully!')
            return redirect('supplier_list')
    else:
        form = SupplierForm()
    
    return render(request, 'bigmart/supplier_form.html', {'form': form, 'title': 'Add Supplier'})


# Reports
@login_required
def reports_view(request):
    today = timezone.now().date()
    
    # Date filters
    start_date = request.GET.get('start_date', today - timedelta(days=30))
    end_date = request.GET.get('end_date', today)
    
    sales_data = Sale.objects.filter(
        sale_date__date__gte=start_date,
        sale_date__date__lte=end_date
    ).aggregate(
        total_sales=Sum('total_amount'),
        total_transactions=Count('id')
    )
    
    top_products = SaleItem.objects.filter(
        sale__sale_date__date__gte=start_date,
        sale__sale_date__date__lte=end_date
    ).values('product__name').annotate(
        total_quantity=Sum('quantity'),
        total_revenue=Sum('subtotal')
    ).order_by('-total_revenue')[:10]
    
    context = {
        'sales_data': sales_data,
        'top_products': top_products,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'bigmart/reports.html', context)