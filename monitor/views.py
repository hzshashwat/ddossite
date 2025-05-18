import json, psutil, time
from django.http import JsonResponse
from .models import BlockedIP
from prometheus_client import Gauge

cpu_gauge      = Gauge('django_cpu_percent', 'CPU percent via psutil')
blocked_gauge  = Gauge('blocked_ip_total', 'Total blocked IPs')

def status(request):
    cpu = psutil.cpu_percent(interval=None)
    cpu_gauge.set(cpu)

    blocked = list(BlockedIP.objects
                   .values('ip', 'reason', 'created_at')
                   .order_by('-created_at')[:50])
    blocked_gauge.set(len(blocked))
    return JsonResponse({
        "alive": True,
        "timestamp": time.time(),
        "cpu": cpu,
        "blocked": blocked,
    })

from django.shortcuts import render
def dashboard(request): return render(request, "dashboard.html")
