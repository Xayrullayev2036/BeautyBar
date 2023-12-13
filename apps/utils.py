from datetime import timedelta, datetime

from apps.appointment.models import Schedule


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
    # schedule_instance.available_times = schedule_data
    schedule_instance.save()
