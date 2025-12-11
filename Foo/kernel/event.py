"""Event class
Events are executed by the timeline, and they have to be scheduled in the timeline to be run.
To-do: 1. raise a proper error message for typeerrors and attribute errors
"""

from dataclasses import dataclass, field
from .process import Process

@dataclass(order= True)
class Event:
    """
    Attributes:
    time: simulation time after which the event is executed
    process: process being executed
    priority: the priority of the event, lower value denotes a higher priority (default inf)
    is removed: the flag to denotes if it's a valid event
    """
    time: int
    process: Process = field(compare= False)
    priority: float
    _is_removed: bool = field(default= False, compare= False)

    def __init__(self, time: int, process: Process, priority=float('inf')):
        self.time = time
        self.priority = priority
        self.process = process
    
    # TODO: correct this
    def __repr__(self) -> str:
        return f"Event(time={self.time},process={self.process},priority={self.priority})"

    def set_invalid(self):
        self._is_removed = True

    def is_invalid(self):
        return self._is_removed