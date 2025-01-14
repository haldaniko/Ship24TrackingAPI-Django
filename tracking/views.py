from django.http import JsonResponse
from .helpers import create_tracker, track_package


def track_package_view(request, tracking_id):
    try:
        result = track_package(tracking_id)

        if result["success"]:
            return JsonResponse(result["data"], safe=False)

        elif (
            result["status_code"] == 404
            and any(error.get("code") == "tracker_not_found" for error in result["error"].get("errors", []))
        ):
            create_tracker(tracking_id)
            result = track_package(tracking_id)

        return JsonResponse(result["data"], safe=False)

    except ValueError as e:
        return JsonResponse({"error": f"Value Error: {str(e)}"}, status=400)

    except KeyError as e:
        return JsonResponse({"error": f"Key Error: {str(e)}"}, status=400)

    except Exception as e:
        return JsonResponse({"error": f"Unexpected Error: {str(e)}"}, status=500)
