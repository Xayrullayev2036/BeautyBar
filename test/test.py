
# yourappname/services.py
from datetime import datetime, timedelta
from .models import Appointment


class AvailableService:
    def run(self, provider_id, date):
        # O'zgartirilgan JavaScript kodining Python versiyasi
        appointments = Appointment.objects.filter(
            provider_id=provider_id,
            canceled_at__isnull=True,
            date__range=[
                datetime.strptime(date, '%Y-%m-%d').replace(hour=0, minute=0, second=0),
                datetime.strptime(date, '%Y-%m-%d').replace(hour=23, minute=59, second=59),
            ],
        )

        schedule = [
            '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00',
            '20:00',
        ]

        available = [
            {
                "time": time,
                "value": (datetime.strptime(f'{date} {time}', '%Y-%m-%d %H:%M')).isoformat(),
                "available": (
                        datetime.now() < datetime.strptime(f'{date} {time}', '%Y-%m-%d %H:%M')
                        and not any(a.date.strftime('%H:%M') == time for a in appointments)
                ),
            }
            for time in schedule
        ]

        return available
