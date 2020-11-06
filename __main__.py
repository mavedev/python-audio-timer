#!/usr/bin/python
# -*- coding: utf-8 -*-

from app.schedule_actor import ScheduleActor


def main() -> None:
    try:
        ScheduleActor(duration=10).run_task(print, 'Hello')
    except KeyboardInterrupt:
        print('Program finished by user.')


if __name__ == '__main__':
    main()
