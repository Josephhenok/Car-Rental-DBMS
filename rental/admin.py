from django.contrib import admin
from django.apps import apps
class GenericAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [f.name for f in self.model._meta.fields]
    def get_search_fields(self, request):
        return [f.name for f in self.model._meta.fields if f.get_internal_type() in {"CharField","TextField","EmailField"}]
    def get_list_filter(self, request):
        return [f.name for f in self.model._meta.fields if f.is_relation or f.get_internal_type() in {"BooleanField"}]
app = apps.get_app_config("rental")
for model in app.get_models():
    try:
        admin.site.register(model, GenericAdmin)
    except admin.sites.AlreadyRegistered:
        pass
