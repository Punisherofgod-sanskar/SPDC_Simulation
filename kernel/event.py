"""Event class
Events are executed by the timeline, and they have to be scheduled in the timeline to be run.
To-do: 1. raise a proper error message for typeerrors and attribute errors
"""

from math import inf
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .process import Process
#to avoid circular imports between event.py and process.py


class Event:
    """
    Attributes:
    time: simulation time after which the event is executed
    process: process being executed
    priority: the priority of the event, lower value denotes a higher priority (default inf)
    is removed: the flag to denotes if it's a valid event
    """


    def __init__(self, time: int, process: "Process", priority=inf):
        self.time = time
        self.priority = priority
        self.process = process
        self._is_removed = False
    
    def __eq__(self, another):
        return (self.time == another.time) and (self.priority == another.priority)
    
    def __ne__(self, another):
        return (self.time != another.time) or (self.priority != another.priority)

    def __gt__(self, another):
        return (self.time > another.time) or (self.time == another.time and self.priority > another.priority)

    def __lt__(self, another):
        return (self.time < another.time) or (self.time == another.time and self.priority < another.priority)

    def set_invalid(self):
        self._is_removed = True

    def is_invalid(self):
        return self._is_removed