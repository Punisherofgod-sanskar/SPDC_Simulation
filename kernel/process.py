"""Process class
To-Do - 1. raise a proper error message for typeerrors and attribute errors
"""

from typing import Any

class Process:
    """
    Attributes:
    owner : the object instance whose method will be invoked
    number : useful for tracking of process in timeline
    call method : name of the method called on the owner
    call args :positional arguements
    call kwargs : dictionary of arguements
    """

    def __init__(self, owner: Any, call_method: str, call_args: list[Any], call_kwargs: dict[Any, Any] = {}):
        self.owner = owner
        self.number = None
        self.call = call_method
        self.call_args = call_args
        self.call_kwargs = call_kwargs
    
    def run(self) -> None:

        return getattr(self.owner, self.call)(*self.call_args, **self.call_kwargs)