class UserFavoriteArtwork:
    def __init__(self, user_id=None, artwork_id=None):
        self.__user_id = user_id
        self.__artwork_id = artwork_id


    #getters
    def get_user_id(self):
        return self.__user_id
    def get_artwork_id(self):
        return self.__artwork_id

    #setters
    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_artwork_id(self, artwork_id):
        self.__artwork_id = artwork_id


