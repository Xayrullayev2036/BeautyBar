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


# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzAyMjg1NDE4LCJpYXQiOjE3MDIyNzgyMTgsImp0aSI6ImQyN2JmNDAxZWJjNDQ5ZjY5NWI2YTczOWEzYjc4ZWMzIiwidXNlcl9pZCI6MX0.yxxGCaP76IbSnfQbjzWcoJe5HmPPoq7DUEe7n1w28FQ


#
# from datetime import datetime, timedelta
#
#
# def generate_minutes(start_time, end_time, interval_minutes):
#     current_time = start_time
#     while current_time < end_time:
#         yield current_time.strftime("%H:%M")
#         current_time += timedelta(minutes=interval_minutes)
#
#
# def generate_booking_slots(booking_time, service_duration, start_time, end_time):
#     booking_end = booking_time + service_duration
#     generate_start = max(start_time, booking_end)
#     generate_interval_minutes = 60
#     return generate_minutes(generate_start, end_time, generate_interval_minutes)
#
#
# start_time = datetime.strptime("10:00", "%H:%M")
# end_time = datetime.strptime("19:00", "%H:%M")
# booking_time = datetime.strptime("13:00", "%H:%M")
# service_duration = timedelta(hours=1, minutes=30)
#
# available_slots = list(generate_booking_slots(booking_time, service_duration, start_time, end_time))
#
# print(available_slots)


#
# import json
# from datetime import datetime, timedelta
#
#
# def generate_time_slots(start_time, end_time, interval_minutes):
#     current_time = start_time
#     time_slots = []
#
#     while current_time <= end_time:
#         time_slots.append(current_time.strftime("%H:%M"))
#         current_time += timedelta(minutes=interval_minutes)
#
#     return time_slots
#
#
# def generate_schedule(start_date, end_date, start_time, end_time, interval_minutes):
#     current_date = start_date
#     schedule = {}
#
#     while current_date <= end_date:
#         date_str = current_date.strftime("%Y-%m-%d")
#         time_slots = generate_time_slots(start_time, end_time, interval_minutes)
#         schedule[date_str] = time_slots
#         current_date += timedelta(days=1)
#
#     return schedule
#
#
# def place_order(schedule, date, time_slot):
#     if date in schedule and time_slot in schedule[date]:
#         schedule[date].remove(time_slot)
#         print(f"Order placed for {date} at {time_slot}")
#     else:
#         print("Invalid date or time slot")
#
#
# if __name__ == "__main__":
#     start_date = datetime(2023, 12, 1)  # Change to the desired start date
#     end_date = datetime(2023, 12, 31)  # Change to the desired end date
#     start_time = datetime.strptime("09:00", "%H:%M")
#     end_time = datetime.strptime("20:00", "%H:%M")
#     interval_minutes = 60
#
#     schedule = generate_schedule(start_date, end_date, start_time, end_time, interval_minutes)
#
#     # Assume placing an order on December 15, 2023, at 10:30
#     order_date = datetime(2023, 12, 1)
#     order_time_slot = "11:00"
#
#     place_order(schedule, order_date.strftime("%Y-%m-%d"), order_time_slot)
#
#     with open("schedule.json", "w") as json_file:
#         json.dump(schedule, json_file, indent=2)
#
#     print("Schedule updated and saved to 'schedule.json'")


import json
from datetime import datetime, timedelta


def generate_schedule(start_date, end_date, start_time, end_time, interval_minutes):
    schedule = {}

    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        schedule[date_str] = [current_date.strftime("%H:%M") for current_date in
                              generate_time_slots(start_time, end_time, interval_minutes)]
        current_date += timedelta(days=1)

    return schedule


def generate_time_slots(start_time, end_time, interval_minutes):
    current_time = start_time
    while current_time <= end_time:
        yield current_time
        current_time += timedelta(minutes=interval_minutes)


def place_order(schedule, date, time_slot, service_duration):
    if date in schedule and time_slot in schedule[date]:
        order_datetime = datetime.strptime(f"{date} {time_slot}", "%Y-%m-%d %H:%M")
        end_order_time = order_datetime + timedelta(minutes=service_duration)
        print(schedule[date])
        schedule[date].remove(time_slot)
        current_time = order_datetime
        while current_time < end_order_time:
            current_time_str = current_time.strftime("%H:%M")
            if current_time_str in schedule[date]:
                schedule[date].remove(current_time_str)
            current_time += timedelta(minutes=interval_minutes)
    else:
        print("Invalid date or time slot")


if __name__ == "__main__":
    start_date = datetime(2023, 12, 1)
    end_date = datetime(2023, 12, 31)
    start_time = datetime.strptime("09:00", "%H:%M")
    end_time = datetime.strptime("20:00", "%H:%M")
    interval_minutes = 30

    schedule = generate_schedule(start_date, end_date, start_time, end_time, interval_minutes)

    order_date = datetime(2023, 12, 6)
    order_time_slot = "13:00"
    service_duration = 90

    place_order(
        schedule,
        order_date.strftime("%Y-%m-%d"),
        order_time_slot,
        service_duration,
    )
    # print(schedule)
    # print(order_date)
    # print(order_time_slot)
    # print(service_duration)

    with open("schedule.json", "w") as json_file:
        json.dump(schedule, json_file, indent=2)

    print("Schedule updated and saved to 'schedule.json'")

# user_id = 1
# user_instance = User.objects.get(id=user_id)
# master_inst = Master.objects.get(user_id=user_instance.id)
# print(master_inst)
