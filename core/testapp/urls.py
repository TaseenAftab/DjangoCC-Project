from django.urls import path

from core.testapp.views import ifta_create_view
from core.testapp.views import ifta_delete_view
from core.testapp.views import ifta_detail_view
from core.testapp.views import ifta_list_view
from core.testapp.views import ifta_update_view
from core.testapp.views import testview

app_name = "testapp"

urlpatterns = [
    path("", view=testview, name="dashboard"),
    path("ifta/", view=ifta_list_view, name="ifta_list"),
    path("ifta/create/", view=ifta_create_view, name="ifta_create"),
    path("ifta/<str:name>/", view=ifta_detail_view, name="ifta_detail"),
    path("ifta/<str:name>/update/", view=ifta_update_view, name="ifta_update"),
    path("ifta/<str:name>/delete/", view=ifta_delete_view, name="ifta_delete"),
]
