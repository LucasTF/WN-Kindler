from abc import ABC, abstractmethod
from typing import List

import os
import click

class Source(ABC):

    def __init__(self, filename: str) -> None:
        if os.name == 'posix' and os.path.isfile(f'{os.path.expanduser('~')}/.cache/wnk/{filename}.json'):
            # TODO: Load cached json with novel list
            click.echo(click.style('Exists', fg='green'))

    @abstractmethod
    def list_novels(page: int = 1, limit: int = 50) -> List[str]:
        pass

    @abstractmethod
    def cache_novels(novel_list: List[str] = None) -> None:
        pass

