from dao.VirtualGalleryImpl import VirtualArtGalleryImpl
from entity.artwork import Artwork
from exception.app_exceptions import *
from util.DBConnection import DBConnection


class VirtualArtGalleryService:

    def __init__(self):
        self.gallery_impl = VirtualArtGalleryImpl()
        self.db_connection = DBConnection.get_connection()

    def add_artwork(self, artwork: Artwork = None) -> bool:
        try:
            return self.gallery_impl.add_artwork(artwork)
        except Exception as e:
            print(f"Error in service layer: {e}")
            return False

    def update_artwork(self) -> bool:
        try:
            return self.gallery_impl.update_artwork()
        except Exception as e:
            print(f"Error in service layer: {e}")
            return False

    def remove_artwork(self) -> bool:
        try:
            return self.gallery_impl.remove_artwork()
        except Exception as e:
            print(f"Error in service layer: {e}")
            return False

    def get_artwork_by_id(self):
        try:
            return self.gallery_impl.get_artwork_by_id()
        except Exception as e:
            print(f"Error in service layer: {e}")
            return None


    def search_artworks(self) -> list:
        try:
            return self.gallery_impl.search_artworks()
        except Exception as e:
            print(f"Error in service layer: {e}")
            return []

    def add_artwork_to_favorite(self, user_id: int, artwork_id: int) -> bool:
        try:
            return self.gallery_impl.add_artwork_to_favorite(user_id, artwork_id)
        except Exception as e:
            print(f"Error in service layer: {e}")
            return False

    def remove_artwork_from_favorite(self) -> bool:
        try:
            return self.gallery_impl.remove_artwork_from_favorite()
        except Exception as e:
            print(f"Error in service layer: {e}")
            return False

    def get_user_favorite_artworks(self) -> bool:
        try:
            return self.gallery_impl.get_user_favorite_artworks()
        except Exception as e:
            print(f"Error in service layer: {e}")
    def add_artist(self):
        try:
            return self.gallery_impl.add_artist()
        except Exception as e:
            print(f"Error in service layer: {e}")
            return False
    def get_artist_by_id(self):
        try:
            return self.gallery_impl.get_artist_by_id()
        except Exception as e:
            print(f"Error in service layer: {e}")
            return None
    def remove_artist_by_id(self):
        try:
            return self.gallery_impl.remove_artist_by_id()
        except Exception as e:
            print(f"Error in service layer: {e}")
            return False

    def create_virtual_gallery(self):
        try:
            return self.create_virtual_gallery()
        except Exception as e:
            print(f"Error in service layer: {e}")
            return False
    def add_artwork_to_gallery(self):
        try:
            return self.add_artwork_to_gallery()
        except Exception as e:
            print(f"Error in service layer: {e}")
            return False

    def delete_artwork_from_gallery(self):
        try:
            return self.delete_artwork_from_gallery()
        except Exception as e:
            print(f"Error in service layer: {e}")
            return False
    def delete_virtual_gallery(self):
        try:
            return self.delete_virtual_gallery()
        except Exception as e:
            print(f"Error in service layer: {e}")
            return False
    def view_virtual_galleries(self):
        try:
            return self.view_virtual_galleries()
        except Exception as e:
            print(f"Error in service layer: {e}")
            return False
    def add_user(self):
        try:
            return self.add_user()
        except Exception as e:
            print(f"Error in service layer: {e}")
            return False
    def get_user_by_id(self):
        try:
            return self.gallery_impl.get_user_by_id()
        except Exception as e:
            print(f"Error in service layer: {e}")
            return None
    def remove_user_by_id(self):
        try:
            return self.gallery_impl.remove_user_by_id()
        except Exception as e:
            print(f"Error in service layer: {e}")
            return False



