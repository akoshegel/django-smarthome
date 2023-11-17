from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def get_devices(request):
    return Response(
        {"test": True},
        status=200,
    )
