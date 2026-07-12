import json

from django.http import HttpResponse


class HTMXMixin:
    """
    A mixin to configure Class-Based Views for seamless HTMX interaction.
    Provides utility properties, automatic template swapping for partials,
    and helpers for setting HTMX response headers.
    """

    htmx_template_name = None

    @property
    def is_htmx(self) -> bool:
        """Check if the request was made via HTMX."""
        return bool(self.request.headers.get("HX-Request"))

    def get_template_names(self):
        """
        If it's an HTMX request and htmx_template_name is set, return it.
        Otherwise, fall back to standard template names.
        """
        if self.is_htmx and self.htmx_template_name:
            return [self.htmx_template_name]
        return super().get_template_names()

    def get_htmx_response(self, content="", status=200, headers=None, **kwargs):
        """
        Helper method to return a standard HttpResponse with HTMX headers.
        """
        response = HttpResponse(content, status=status, **kwargs)
        if headers:
            for key, value in headers.items():
                response[key] = value
        return response

    def hx_redirect(self, url: str) -> HttpResponse:
        """Trigger a client-side redirect via HTMX using the HX-Redirect header."""
        return self.get_htmx_response(headers={"HX-Redirect": url})

    def hx_refresh(self) -> HttpResponse:
        """Trigger a full client-side page refresh via HTMX."""
        return self.get_htmx_response(headers={"HX-Refresh": "true"})

    def hx_trigger(
        self,
        response: HttpResponse,
        event_name: str,
        event_data=None,
    ) -> HttpResponse:
        """
        Add a client-side event trigger to the response using the HX-Trigger header.
        Supports appending to existing triggers gracefully.
        """
        trigger_header = response.get("HX-Trigger")

        if trigger_header:
            try:
                triggers = json.loads(trigger_header)
                if not isinstance(triggers, dict):
                    triggers = {trigger_header: ""}
            except json.JSONDecodeError:
                triggers = {trigger_header: ""}
        else:
            triggers = {}

        # Add/update the event
        triggers[event_name] = event_data if event_data is not None else ""
        response["HX-Trigger"] = json.dumps(triggers)
        return response
