from django.shortcuts import render, redirect
from .forms import OrderForm

# Create your views here.
def order_form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin/')  # 注文が成功した場合のリダイレクト先
    else:
        form = OrderForm()

    return render(request, 'blog/order_form.html', {'form': form})