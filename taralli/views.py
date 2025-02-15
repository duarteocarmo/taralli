from datetime import datetime
import logging
import random
from typing import Union

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from pydantic import BaseModel

logger = logging.getLogger(__name__)

meals = []
weights = []


class Weight(BaseModel):
    weight: float
    date: datetime = datetime.now()


class Meal(BaseModel):
    description: str
    date: datetime = datetime.now()
    calories: int | None = None


class LogEntry(BaseModel):
    logs: list[Union[Weight, Meal]]


def compile_log_entries():
    weight_entries = [(w, "weight") for w in weights]
    meal_entries = [(m, "meal") for m in meals]
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
    return JsonResponse({"weights": weights, "meals": meals})


@require_http_methods(["POST"])
def log_weight(request):
    weight = float(request.POST.get("weight"))
    date = request.POST.get("date") or datetime.now()
    w = Weight(weight=weight, date=date)
    weights.append(w)
    logger.info(f"Logged weight: {w.weight} on {w.date}")
    return render(request, "index.html", {"log_entries": compile_log_entries()})


@require_http_methods(["POST"])
def log_meal(request):
    description = request.POST.get("description")
    date = request.POST.get("date") or datetime.now()
    m = Meal(description=description, date=date, calories=random.randint(100, 1000))
    meals.append(m)
    logger.info(f"Logged meal: {m.description} on {m.date}")
    return render(request, "index.html", {"log_entries": compile_log_entries()})
