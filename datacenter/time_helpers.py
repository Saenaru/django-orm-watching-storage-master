from django.utils import timezone


SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600


def get_duration(visit):
    end_time = visit.leaved_at or timezone.now()
    duration = end_time - visit.entered_at
    return duration.total_seconds()


def format_duration(duration):
    hours, remainder = divmod(duration, SECONDS_IN_HOUR)
    minutes, seconds = divmod(remainder, SECONDS_IN_MINUTE)
    return '{:02}ч {:02}мин {:02}сек'.format(int(hours), int(minutes), int(seconds))


def is_visit_long(visit, minutes=60):
    duration_seconds = get_duration(visit)
    threshold_seconds = minutes * SECONDS_IN_MINUTE
    return duration_seconds > threshold_seconds
