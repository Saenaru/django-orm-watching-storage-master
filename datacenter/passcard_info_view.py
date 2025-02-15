from django.shortcuts import get_object_or_404, render
from datacenter.models import Passcard, Visit
from datacenter.time_helpers import is_visit_long, get_duration, format_duration


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits = []
    for visit in visits:
        duration_seconds = get_duration(visit)
        formatted_duration = format_duration(duration_seconds)
        is_strange = is_visit_long(visit)
        this_passcard_visits.append({
            'entered_at': visit.entered_at,
            'duration': formatted_duration,
            'is_strange': is_strange
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
