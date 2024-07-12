from enum import Enum

class Wnsource(Enum):
    FAQWIKI = 1
    HELSCANS = 2
    INOVELTRANSLATIONS = 3
    ROYAL_ROAD = 4

def get_source_name(source: Wnsource) -> str:
    if source == Wnsource.FAQWIKI:
        return 'FaqWiki'
    elif source == Wnsource.HELSCANS:
        return 'Helscans'
    elif source == Wnsource.INOVELTRANSLATIONS:
        return 'iNovelTranslations'
    elif source == Wnsource.ROYAL_ROAD:
        return 'Royal Road'