from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from .models import Service, Customer, Channel
from .forms import ServiceForm, CustomerForm, ChannelForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Service, Customer, Channel
from .forms import ServiceForm, CustomerForm, ChannelForm
from django.db.models import Count
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy


@login_required
def home(request):
    total = Service.objects.count()
    active = Service.objects.filter(status="ACTIVE").count()
    test = Service.objects.filter(status="TEST").count()
    removed = Service.objects.filter(status="REMOVED").count()

    expired_tests = sum(1 for s in Service.objects.all() if s.test_expired)

    return render(request, "core/home.html", {
        "total": total,
        "active": active,
        "test": test,
        "removed": removed,
        "expired_tests": expired_tests,
    })


@login_required
def service_list(request):
    query = request.GET.get("q", "").strip()
    status_filter = request.GET.get("status")
    order = request.GET.get("order", "newest")

    services = Service.objects.select_related("customer", "channel")

    if status_filter:
        services = services.filter(status=status_filter)

    if query:
        services = services.filter(
            models.Q(customer__name__icontains=query) |
            models.Q(channel__name__icontains=query) |
            models.Q(public_ip__icontains=query)
        )

    if order == "oldest":
        services = services.order_by("created_at")
    else:
        services = services.order_by("-created_at")

    return render(request, "core/service_list.html", {
        "services": services,
        "query": query,
        "status_filter": status_filter,
        "order": order,
    })

@login_required
def service_create(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.created_by = request.user
            service.save()
            return redirect("service_list")
    else:
        form = ServiceForm()

    return render(request, "core/service_form.html", {"form": form})


@login_required
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)

    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect("service_list")
    else:
        form = ServiceForm(instance=service)

    return render(request, "core/service_form.html", {"form": form})


@login_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)

    if request.method == "POST":
        service.status = "REMOVED"
        service.save()
        return redirect("service_list")

    return render(request, "core/service_confirm_delete.html", {"service": service})
@login_required
def customer_create_popup(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return JsonResponse({
                "success": True,
                "id": customer.id,
                "name": customer.name,
            })
        return JsonResponse({
            "success": False,
            "errors": form.errors,
        }, status=400)

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)
@login_required
def channel_create_popup(request):
    if request.method == "POST":
        form = ChannelForm(request.POST)
        if form.is_valid():
            channel = form.save()
            return JsonResponse({
                "success": True,
                "id": channel.id,
                "name": channel.name,
            })
        return JsonResponse({
            "success": False,
            "errors": form.errors,
        }, status=400)

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)
class UserLoginView(LoginView):
    template_name = "core/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("home")


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("login")