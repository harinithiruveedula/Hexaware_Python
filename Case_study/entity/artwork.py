class Artwork:
    def __init__(self, artwork_id=None, title=None, description=None,
                 creation_date=None, medium=None, image_url=None, artist_id=None):
        self.__artwork_id = artwork_id
        self.__title = title
        self.__description = description
        self.__creation_date = creation_date
        self.__medium = medium
        self.__image_url = image_url
        self.__artist_id = artist_id



    #getters
    def get_artwork_id(self):
        return self.__artwork_id
    def get_title(self):
        return self.__title
    def get_description(self):
        return self.__description
    def get_creation_date(self):
        return self.__creation_date
    def get_medium(self):
        return self.__medium
    def get_image_url(self):
        return self.__image_url
    def get_artist_id(self):
        return self.__artist_id

    #setters
    def set_artwork_id(self, artwork_id):
        self.__artwork_id = artwork_id

    def set_title(self, title):
        self.__title = title

    def set_description(self, description):
        self.__description = description

    def set_creation_date(self, creation_date):
        self.__creation_date = creation_date

    def set_medium(self, medium):
        self.__medium = medium

    def set_image_url(self, image_url):
        self.__image_url = image_url

    def set_artist_id(self, artist_id):
        self.__artist_id = artist_id

