import json


def add_toast(response, message, level):
    response["HX-Trigger"] = json.dumps(
        {
            "htmx-toasts:notify": {
                "message": message,
                "level": level,
            },
        },
    )

    return response
