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

    @abstractmethod
    def add_artist(self) -> bool:
        pass
    @abstractmethod
    def get_artist_by_id(self) -> bool:
        pass
    @abstractmethod
    def remove_artist_by_id(self) -> bool:
        pass

    @abstractmethod
    def create_virtual_gallery(self) -> bool:
        pass
    @abstractmethod
    def add_artwork_to_gallery(self) ->bool:
        pass
    @abstractmethod
    def delete_artwork_from_gallery(self) -> bool:
        pass
    @abstractmethod
    def delete_virtual_gallery(self) -> bool:
        pass
    @abstractmethod
    def view_virtual_galleries(self) -> bool:
        pass
    @abstractmethod
    def add_user(self) -> bool:
        pass

    @abstractmethod
    def get_user_by_id(self) -> bool:
        pass
    @abstractmethod
    def remove_user_by_id(self) -> bool:
        pass

