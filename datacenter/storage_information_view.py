from datacenter.models import Visit
from datacenter.models import is_visit_long, get_duration, format_duration
from django.shortcuts import render


def storage_information_view(request):
    active_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in active_visits:
        duration_seconds = get_duration(visit)
        formatted_duration = format_duration(duration_seconds)
        is_strange = is_visit_long(visit)
        non_closed_visit = {
            'who_entered': visit.passcard,
            'entered_at': visit.entered_at,
            'duration': formatted_duration,
            'is_strange': is_strange
        }
        non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
