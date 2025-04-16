from abc import ABC, abstractmethod
from entity.artwork import Artwork

class IVirtualArtGallery(ABC):
    @abstractmethod
    def add_artwork(self, artwork: Artwork) -> bool:
        pass

    @abstractmethod
    def update_artwork(self, artwork: Artwork) -> bool:
        pass

    @abstractmethod
    def remove_artwork(self, artwork: Artwork) -> bool:
        pass

    @abstractmethod
    def search_artworks(self, keyword: str) -> list[Artwork]:
        pass

    @abstractmethod
    def add_artwork_to_favorite(self, user_id: int, artwork_id: int) -> bool:
        pass

    @abstractmethod
    def remove_artwork_from_favorite(self) -> bool:
        pass

    @abstractmethod
    def get_user_favorite_artworks(self) -> bool:
        pass

