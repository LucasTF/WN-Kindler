from enum import Enum

from wnk.sources.helscans import Helscans
from wnk.sources.source import Source

class Wnsource(Enum):
    FAQWIKI = 1
    HELSCANS = 2
    INOVELTRANSLATIONS = 3
    ROYAL_ROAD = 4
        
class SourceFactory:

    def __init__(self, source: int) -> None:
        try:
            self.source = Wnsource(source)
            self.source_name = self.get_source_title(Wnsource(source))
        except ValueError:
            self.source = None
            self.source_name = None

    @staticmethod
    def get_source_title(source: Wnsource) -> str:
        match source:
            case Wnsource.FAQWIKI:
                return 'FaqWiki'
            case Wnsource.HELSCANS:
                return 'Helscans'
            case Wnsource.INOVELTRANSLATIONS:
                return 'iNovelTranslations'
            case Wnsource.ROYAL_ROAD:
                return 'Royal Road'
            case _:
                return None
    
    def create_source(self) -> Source:
        match self.source:
            case Wnsource.HELSCANS:
                return Helscans()
            case _:
                return None
            