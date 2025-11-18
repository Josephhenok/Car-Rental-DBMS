from django.shortcuts import render
from django.apps import apps

def _rows_for(model, limit=200):
    fields = [f for f in model._meta.fields]
    headers = [f.name for f in fields]
    rows = []
    for obj in model.objects.all()[:limit]:
        row = []
        for f in fields:
            v = getattr(obj, f.name)
            row.append(str(v) if f.is_relation and v is not None else v)
        rows.append(row)
    return headers, rows

def dashboard(request):
    app = apps.get_app_config("rental")
    models = sorted([m for m in app.get_models()], key=lambda m: m._meta.verbose_name_plural.lower())
    model_map = {m.__name__: m for m in models}
    selected_name = request.GET.get("table") or (models[0].__name__ if models else "")
    selected = model_map.get(selected_name) if selected_name else None
    headers, rows = ([], [])
    if selected:
        headers, rows = _rows_for(selected)
    tabs = [{"name": m.__name__, "label": m._meta.verbose_name_plural.title()} for m in models]
    ctx = {"tabs": tabs, "selected_name": selected_name, "headers": headers, "rows": rows}
    return render(request, "dashboard.html", ctx)
