import os
from tkinter import N

import django

import datetime

import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

from datacenter.models import Visit

from django.utils import timezone

from django.utils.timezone import localtime



if __name__ == '__main__':
    # Программируем здесь
    Passcard_list = Passcard.objects.all()
    name_card = Passcard_list[0].owner_name
    passcode_card = Passcard_list[0].passcode
    created_at_card = Passcard_list[0].created_at
    is_active_card = Passcard_list[0].is_active
    active_passcards = Passcard.objects.filter(is_active=True)
    Visit_list = Visit.objects.filter(leaved_at=None)
    # print(Visit_list)
    entered_at = Visit_list[0].entered_at
    leaved_at = Visit_list[0].leaved_at
    msc_entered_at = django.utils.timezone.localtime(entered_at)
    print(entered_at, msc_entered_at)
    
    for visiter in Visit_list:
        passcard = visiter.passcard
        visiter_name = passcard.owner_name
        entered_at = visiter.entered_at
        now = datetime.datetime.now(timezone.utc)
        delta = now - msc_entered_at
        total_seconds = delta.total_seconds()
        time_spent = time.strftime ("%H:%M:%S", time.gmtime (total_seconds))
        print(f'{visiter_name} Зашел в хранилище по Москве:\n{msc_entered_at}\nНаходится в хранилище:\n{time_spent}')

 
    
    # print("Активных пропусков:", len(active_passcards))
    # print(f"owner_name: {name_card}\npasscode: {passcode_card}\ncreated_at: {created_at_card}\nis_active: {is_active_card}")
    # print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
