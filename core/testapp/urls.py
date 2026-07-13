from django.urls import path

from core.testapp.views import (
    ifta_create_view,
    ifta_delete_view,
    ifta_detail_view,
    ifta_list_view,
    ifta_update_view,
)

app_name = "testapp"

urlpatterns = [
    path("", view=ifta_list_view, name="ifta_list"),
    path("create/", view=ifta_create_view, name="ifta_create"),
    path("<str:name>/", view=ifta_detail_view, name="ifta_detail"),
    path("<str:name>/update/", view=ifta_update_view, name="ifta_update"),
    path("<str:name>/delete/", view=ifta_delete_view, name="ifta_delete"),
]
