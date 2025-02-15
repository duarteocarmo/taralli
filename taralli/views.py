import logging
import random

from django.shortcuts import render
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from .models import Weight, Meal

logger = logging.getLogger(__name__)


def compile_log_entries():
    weight_entries = [(w, "weight") for w in Weight.objects.all()]
    meal_entries = [(m, "meal") for m in Meal.objects.all()]
    entries = weight_entries + meal_entries
    entries.sort(key=lambda x: x[0].date)
    return entries


def index(request):
    return render(
        request,
        "index.html",
        {
            "log_entries": compile_log_entries(),
        },
    )


def get_logs(request):
    return JsonResponse(
        {"weights": list(Weight.objects.values()), "meals": list(Meal.objects.values())}
    )


@require_http_methods(["POST"])
def log_weight(request):
    weight = float(request.POST.get("weight"))
    date = (
        timezone.make_aware(datetime.fromisoformat(request.POST.get("date")))
        if request.POST.get("date")
        else timezone.now()
    )
    w = Weight.objects.create(weight=weight, date=date)
    logger.info(f"Logged weight: {w.weight} on {w.date}")
    return render(request, "index.html", {"log_entries": compile_log_entries()})


@require_http_methods(["POST"])
def log_meal(request):
    description = request.POST.get("description")
    date = (
        timezone.make_aware(datetime.fromisoformat(request.POST.get("date")))
        if request.POST.get("date")
        else timezone.now()
    )
    m = Meal.objects.create(
        description=description, date=date, calories=random.randint(100, 1000)
    )
    logger.info(f"Logged meal: {m.description} on {m.date}")
    return render(request, "index.html", {"log_entries": compile_log_entries()})
