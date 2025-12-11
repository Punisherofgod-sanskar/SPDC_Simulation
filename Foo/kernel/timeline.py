"""Quiet a bit of modules we have to add like Quantum manager for timeline"""

from .event import Event
from heapq import heapify, heappush, heappop

class Timeline:
    def __init__(self, name="default_timeline") -> None:
        self._name = name
        self._event_list: list[Event] = []

    def __len__(self):
        return len(self._event_list)

    def __iter__(self):
        yield from self._event_list

    def schedule(self, event: Event|list[Event]) -> None:
        if(isinstance(event, list)):
            self._event_list.extend(event)
            return heapify(self._event_list)
        
        heappush(self._event_list, event)

    def pop(self) -> Event:
        return heappop(self._event_list)

    def top(self) -> Event:
        return self._event_list[0]

    def isempty(self) -> bool:
        return len(self._event_list) == 0

    def remove(self, event: Event) -> None:
        """Method to remove events from heap.

        The event is set as the invalid state to save the time of removing event from heap.
        """

        event.set_invalid()

    def update_event_time(self, event: Event, time: int):
        """Method to update the timestamp of event and maintain the min-heap structure.
        """
        if time == event.time:
            return

        # TODO: to use an event id
        for i, e in enumerate(self._event_list):
            if id(e) == id(event):
                e.time = time
                break
        heapify(self._event_list)

    def debug(self):
        for event in self._event_list:
            print(event)

    def run(self):
        while(self._event_list):
            event = heappop(self._event_list)
            
            print(event)
            event.process.run()