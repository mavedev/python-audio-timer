#!/usr/bin/python
# -*- coding: utf-8 -*-

from playsound import playsound

from app.schedule_actor import ScheduleActor
from app.invariants import Constants


def main() -> None:
    try:
        ScheduleActor(duration=10).run_task(
            playsound,
            Constants.DEFAULT_FILE_PATH
        )
    except KeyboardInterrupt:
        print('Program finished by user.')


if __name__ == '__main__':
    main()
