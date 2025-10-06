from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import CreateUser,BookingForm,FeadBackForm
from .models import Service,TimeSlot,Booking
from datetime import datetime as dt ,timedelta,time
import datetime

def home(request):
    services = Service.objects.in_bulk([1,2,3,4,5,6])
    context = {
        'service1':services[1],
        'service2':services[2],
        'service3':services[3],
        'service4':services[4],
        'service5':services[5],
        'service6':services[6],
    }
    return render(request,'home.html',context)

def aboutus(request):
    return render(request,'about.html',{})

def callus(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = FeadBackForm(request.POST)
            if form.is_valid():
                feadback = form.save(commit=False)
                feadback.user = request.user
                feadback.save()
                return redirect('call')
            else:
                messages.error(request,'فرم مشکل دارد')
        else:
            form = FeadBackForm()
    else:            
        form = FeadBackForm()
        messages.error(request,'اول لاگین بشید')
    return render(request,'call.html',{'form':form})

def serviceus(request):
    services = Service.objects.in_bulk([1,2,3,4,5,6])
    context = {
        'service1':services[1],
        'service2':services[2],
        'service3':services[3],
        'service4':services[4],
        'service5':services[5],
        'service6':services[6],
    }
    return render(request,'service.html',context)


def generate_times():
    start = datetime.time(7, 30)
    end = datetime.time(22, 0)
    slot_length = datetime.timedelta(minutes=90)
    times = []
    cur = datetime.datetime.combine(datetime.date.today(), start)
    while cur.time() <= end:
        times.append(cur.time())
        cur += slot_length
    return times

def schedule_view(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    today = datetime.date.today()
    days = [today + datetime.timedelta(days=i) for i in range(7)]
    times = generate_times()

    slots_qs = TimeSlot.objects.filter(service=service, date__in=days)
    slot_map = { f"{s.date.isoformat()}_{s.start_time.strftime('%H:%M')}": s for s in slots_qs }

    rows = []
    for t in times:
        cells = []
        for d in days:
            key = f"{d.isoformat()}_{t.strftime('%H:%M')}"
            slot = slot_map.get(key)   
            cells.append({'date': d, 'time': t, 'slot': slot})
        rows.append({'time': t, 'cells': cells})

    return render(request, 'schedule.html', {"service": service, "days": days, "rows": rows})


@login_required(login_url=reverse_lazy('login'))
def reserve(request,service_id,date,time):
    date_obj = datetime.datetime.strptime(date,"%Y-%m-%d").date()
    time_obj = datetime.datetime.strptime(time,"%H:%M").time()
    #slot = get_object_or_404(TimeSlot, service=service_id, date=date_obj, start_time=time_obj, is_reserved=False)
    service = get_object_or_404(Service,id=service_id)
    slot , created = TimeSlot.objects.get_or_create(service=service, 
                                          date=date_obj, 
                                          start_time=time_obj,)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.timeslot = slot
            booking.save()
            slot.is_reserved = True
            slot.save()
            return redirect('schedule',service_id=service_id)
    else:
        form = BookingForm()
    return render(request,'confirmation.html',{'form':form,'slot':slot,'service':service})



def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'کاربر مورد نظر یافت نشد')
    return render(request,'login.html',{})

def log_out(request):
    logout(request)
    return redirect('home')

def sign_in(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            messages.error(request,'لطفاً خطا را برطرف کنید.')
    else:
        form = CreateUser()
    return render(request,'signin.html',{})