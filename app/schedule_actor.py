from collections.abc import Callable

import sched
import time

from singletons import Singleton

from .invariants import Constants


class ScheduleActor(metaclass=Singleton):
    """Main class that runs timer."""

    def __init__(self, *, duration: int) -> None:
        self._duration = duration
        self._scheduler = sched.scheduler(time.time, time.sleep)

    def run_task(self, task: Callable, *args: tuple, **kwargs: dict) -> None:
        """Run provided scheduled operation."""
        task(*args, **kwargs)
        self._scheduler.enter(
            self._duration,
            Constants.DEFAULT_TASK_PRIORITY,
            self.run_task,
            (lambda: task(*args, **kwargs), )
        )
        self._scheduler.run()
