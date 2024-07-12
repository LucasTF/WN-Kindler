from typing import List

from wnk.sources.source import Source

class Helscans(Source):

    def __init__(self) -> None:
        super().__init__('helscans')

    def list_novels(page: int = 1, limit: int = 50) -> List[str]:
        pass

    def cache_novels(novel_list: List[str] = None) -> None:
        pass