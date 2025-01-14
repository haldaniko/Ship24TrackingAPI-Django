from django.core.cache import cache
from django.http import JsonResponse
from .helpers import create_tracker, track_package


def track_package_view(request, tracking_id):
    cache_key = f"tracking_{tracking_id}"
    cached_data = cache.get(cache_key)

    if cached_data:
        return JsonResponse(cached_data, safe=False)

    try:
        result = track_package(tracking_id)

        if result["success"]:
            cache.set(cache_key, result["data"])
            return JsonResponse(result["data"], safe=False)

        elif (
            result["status_code"] == 404
            and any(error.get("code") == "tracker_not_found" for error in result["error"].get("errors", []))
        ):
            create_tracker(tracking_id)
            result = track_package(tracking_id)

            cache.set(cache_key, result["data"])
            return JsonResponse(result["data"], safe=False)

    except Exception as e:
        return JsonResponse({"error": f"Unexpected Error: {str(e)}"}, status=500)
