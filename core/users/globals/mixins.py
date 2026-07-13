from django.http import HttpResponse


class HTMXFormMixin:
    """
    Mixin to automatically convert standard form_valid redirects to HTMX redirects
    using the 'HX-Redirect' header.
    """

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get("HX-Request") == "true":
            response = HttpResponse("")
            response["HX-Redirect"] = self.get_success_url()
        return response
