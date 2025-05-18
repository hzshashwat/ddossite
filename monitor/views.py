import psutil, json, datetime
from django.http import JsonResponse
from django.shortcuts import render
from .models import BlockedIP

def dashboard(request):
    return render(request, "monitor/dashboard.html")

def stats_api(request):
    cpu   = psutil.cpu_percent(interval=None)
    mem   = psutil.virtual_memory().percent
    count = BlockedIP.objects.count()
    return JsonResponse({"cpu": cpu, "mem": mem, "blocked": count,
                         "ts": datetime.datetime.now().isoformat()})
