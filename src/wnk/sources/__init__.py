from enum import Enum

from wnk.sources.helscans import Helscans
from wnk.sources.source import Source

class Wnsource(Enum):
    FAQWIKI = 1
    HELSCANS = 2
    INOVELTRANSLATIONS = 3
    ROYAL_ROAD = 4

def get_source_name(source: Wnsource) -> str:
    match source:
        case Wnsource.FAQWIKI:
            return 'FaqWiki'
        case Wnsource.HELSCANS:
            return 'Helscans'
        case Wnsource.INOVELTRANSLATIONS:
            return 'iNovelTranslations'
        case Wnsource.ROYAL_ROAD:
            return 'Royal Road'
    
def create_source(source_num: int) -> Source:

    source = Wnsource(source_num)

    match source:
        case Wnsource.HELSCANS:
            return Helscans()
        case _:
            return None