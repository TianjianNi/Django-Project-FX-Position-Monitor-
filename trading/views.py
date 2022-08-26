from django.shortcuts import render
from .models import Trade
from .forms import TradeForm

# Create your views here.
def index(request):
    return render(request, 'trading/index.html')

def detail(request, trade_id):
    try:
        trade = Trade.objects.get(pk=trade_id)
    except Trade.DoesNotExist:
        return render(request, 'trading/error.html')
    return render(request, 'trading/detail.html', {'trade': trade})

def results(request):
    latest_trade_list = Trade.objects.order_by('id')
    context = {'latest_trade_list': latest_trade_list}
    return render(request, 'trading/results.html', context)

def add(request):
    form = TradeForm()
    if request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'trading/index.html')
    return render(request,'trading/add.html',{'form':form})