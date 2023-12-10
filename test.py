# from datetime import datetime, timedelta
# from sqlalchemy import and_
#
# from models import Appointment
#
# class AvailableService:
#     def run(self, provider_id, date):
#         appointments = Appointment.query.filter(
#             and_(
#                 Appointment.provider_id == provider_id,
#                 Appointment.canceled_at.is_(None),
#                 Appointment.date.between(
#                     date.replace(hour=0, minute=0, second=0),
#                     date.replace(hour=23, minute=59, second=59),
#                 ),
#             )
#         ).all()
#
#         schedule = [
#             '08:00',
#             '09:00',
#             '10:00',
#             '11:00',
#             '12:00',
#             '13:00',
#             '14:00',
#             '15:00',
#             '16:00',
#             '17:00',
#             '18:00',
#             '19:00',
#             '20:00',
#         ]
#
#         available = [
#             {
#                 "time": time,
#                 "value": (date.replace(hour=int(time.split(':')[0]), minute=int(time.split(':')[1]), second=0)).isoformat(),
#                 "available": (
#                     datetime.now() < date.replace(hour=int(time.split(':')[0]), minute=int(time.split(':')[1]), second=0)
#                     and not any(a.date.strftime('%H:%M') == time for a in appointments)
#                 ),
#             }
#             for time in schedule
#         ]
#
#         return available
