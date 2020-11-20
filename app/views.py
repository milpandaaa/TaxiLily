from datetime import timedelta
import datetime

from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.generic import FormView
from .models import *
from .forms import *


# @csrf_protect
class MyRegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/accounts/login/"
    template_name = "sign.html"

    def form_valid(self, form):
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)


def tariff(request):
    context = {"tariff": Tariff.objects.all()}
    return render(request, "tariff.html", context)


def account(request, accountId):
    try:
        context = {"taxis": Taxis.objects.get(id=accountId), "orders": Order.objects.filter(taxis=accountId)}
        return render(request, "account.html", context)
    except Taxis.DoesNotExist:
        form = TaxisForm(request.POST or None)
        if form.is_valid():
            form.save()
            context = {"taxis": Taxis.objects.get(id=accountId), "orders": Order.objects.filter(taxis=accountId)}
            return render(request, "account.html", context)
        context = {'form': form}
        return render(request, "accountCreate.html", context)


def freeCar(request):
    if request.method == "POST":
        date = request.POST.get("date")
        time = request.POST.get("time")
        temp = Order.objects.filter(date=date, startTime__lte=time, endTime__gte=time).values('taxis')
        temp = Taxis.objects.exclude(user_id__in=temp).values('user_id')
        print(temp)
        context = {"tax": Taxis.objects.filter(user_id__in=temp)}
        return render(request, "taxi.html", context)
    else:
        return render(request, "search.html")


def orderCreate(request, taxis_id):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        temp = Order.objects.get(date=form.cleaned_data['date'],
                                 startTime=form.cleaned_data['startTime'],
                                 passenger=form.cleaned_data['passenger'],
                                 taxis=form.cleaned_data['taxis'])
        temp.endTime = time_plus(form.cleaned_data['startTime'], timedelta(hours=1))
        temp.save()
        order = Order.objects.get(id=temp.id)
        taxis = Taxis.objects.get(id=order.taxis)
        return render(request, "order.html", {"order": order, "taxis": taxis})
    context = {'form': form, "taxis_id": taxis_id}
    return render(request, "orderCreate.html", context, )


def order(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        taxis = Taxis.objects.get(id=order.taxis)
        return render(request, "order.html", {"order": order, "taxis": taxis})
    except Order.DoesNotExist:
        return HttpResponseNotFound("<h2>Order not found</h2>")


def orderFinish(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        if request.method == "POST":
            order.date = request.POST.get("date")
            order.startTime = request.POST.get("startTime")
            order.endTime = request.POST.get("endTime")
            order.distance = request.POST.get("distance")
            order.tariff = request.POST.get("tariff")
            order.passenger = request.POST.get("passenger")
            order.taxis = request.POST.get("taxis")
            order.cost = request.POST.get("passenger")
            order.save()
            return render(request, 'account.html', {"taxis": Taxis.objects.get(id=request.POST.get("taxis")),
                                                    "orders": Order.objects.filter(taxis=request.POST.get("taxis"))})
        else:
            return render(request, "orderFinish.html", {"order": order})
    except Order.DoesNotExist:
        return HttpResponseNotFound("<h2>Order not found</h2>")


def time_plus(time, timedelta):
    start = datetime.datetime(
        2000, 1, 1,
        hour=time.hour, minute=time.minute, second=time.second)
    end = start + timedelta
    return end.time()
