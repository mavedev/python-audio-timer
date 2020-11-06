#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from playsound import playsound

from app.schedule_actor import ScheduleActor
from app.invariants import Constants


def main() -> None:
    if len(sys.argv) != 2:
        print('Invalid argument amount, must be 1')
        return

    try:
        seconds_provided = int(sys.argv[1])
        ScheduleActor(duration=seconds_provided).run_task(
            playsound,
            Constants.DEFAULT_FILE_PATH
        )
    except KeyboardInterrupt:
        print('Program finished by user.')
    except ValueError:
        print('Invalid argument. Duration must be number of seconds.')


if __name__ == '__main__':
    main()
