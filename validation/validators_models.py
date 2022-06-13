from django.core.exceptions import ValidationError
from datetime import datetime, timedelta

def validate_date_time(value: datetime) -> None:
    TODAY = datetime.now()
    limit = TODAY + timedelta(weeks=12)

    if value.timestamp() < TODAY.timestamp():
        raise ValidationError(message='date_time cannot be in the past')
    if value.timestamp() > limit.timestamp():
        raise ValidationError(
            message='date must not be < now + 3months')
    pass


def validate_duration(value: timedelta) -> None:
    if value <= timedelta(minutes=15):
        raise ValidationError(message='duration must not be > 15min')
    if value > timedelta(minutes=120):
        raise ValidationError(message='duration must not be < 2h')


def validate_burned_calories(value: str):
    if value < 0 :
        raise ValidationError(message="burned calories must be a positive number")