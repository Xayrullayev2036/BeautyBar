from datetime import timedelta, datetime

from apps.appointment.models import Schedule
from apps.master.models import Master
from apps.services.models import Services
from apps.users.models import User


def generate_time_slots(start_time, end_time, interval_minutes):
    current_time = datetime.combine(datetime.today(), start_time)  # Convert to datetime object
    end_datetime = datetime.combine(datetime.today(), end_time)  # Convert end_time to datetime object

    while current_time <= end_datetime:
        yield current_time.time()
        current_time += timedelta(minutes=interval_minutes)


def generate_schedule(start_date, end_date, start_time, end_time, interval_minutes):
    schedule_data = {}

    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        schedule_data[date_str] = [current_date.strftime("%H:%M") for current_date in
                                   generate_time_slots(start_time, end_time, interval_minutes)]
        current_date += timedelta(days=1)

    return schedule_data


def save_schedule_to_database(master_instance, start_date, end_date, start_time, end_time, interval_minutes):
    schedule_data = generate_schedule(start_date, end_date, start_time, end_time, interval_minutes)

    schedule_instance = Schedule(
        master=master_instance,
        available_times=schedule_data
    )
    schedule_instance.save()


def place_order(schedule, date, time_slot, service_duration):
    if date in schedule and time_slot in schedule[date]:
        order_datetime = datetime.strptime(f"{date} {time_slot}", "%Y-%m-%d %H:%M")
        end_order_time = order_datetime + timedelta(minutes=service_duration)
        schedule[date].remove(time_slot)
        current_time = order_datetime
        while current_time < end_order_time:
            current_time_str = current_time.strftime("%H:%M")
            if current_time_str in schedule[date]:
                schedule[date].remove(current_time_str)
            current_time += timedelta(minutes=30)
    else:
        print("Invalid date or time slot")


def get_schedule(service):
    master_instance = Services.objects.filter(id=service).first()
    user = User.objects.filter(id=master_instance.owner_id).first()
    master = Master.objects.filter(user_id=user.id).first()
    schedule_master = Schedule.objects.filter(master_id=master.id).first()
    schedule = schedule_master.available_times
    return schedule


def get_duration(service):
    duration = Services.objects.filter(id=service).first()
    return duration.time_to_took


def get_service_duration(time: str):
    a = time.split(":", 2)
    return int(a[0]) * 60 + int(a[1])
