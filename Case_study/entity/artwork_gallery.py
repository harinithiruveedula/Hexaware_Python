class ArtworkGallery:
    def __init__(self, artwork_id=None, gallery_id=None):
        self.__artwork_id = artwork_id
        self.__gallery_id = gallery_id

    #getters
    def get_artwork_id(self):
        return self.__artwork_id

    def get_gallery_id(self):
        return self.__gallery_id

    #setters
    def set_artwork_id(self, artwork_id):
        self.__artwork_id = artwork_id

    def set_gallery_id(self, gallery_id):
        self.__gallery_id = gallery_id

