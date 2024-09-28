from django.shortcuts import render
from datacenter.tools import format_duration, get_duration

from datacenter.models import Visit


def storage_information_view(request):
    non_leaved_visits = Visit.objects.filter(leaved_at=None)

    for visit in non_leaved_visits:
        duration = get_duration(visit)
        formatted_duration = format_duration(duration)

        time_then = visit.entered_at
        author = visit.passcard

    non_closed_visits = [
        {
            'who_entered': author.owner_name,
            'entered_at': time_then,
            'duration': formatted_duration,
        }
    ]
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
