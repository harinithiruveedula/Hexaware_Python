class Artsit:
    def __init__(self, artist_id=None, name=None, birthdate=None, nationality=None,website=None, contact_info=None):
        self._artist_id = artist_id    #private variables
        self._name = name
        self._birthdate = birthdate
        self._nationality = nationality
        self._website = website
        self._contact_info = contact_info

    # getters
    def get_artist_id(self):
        return self._artist_id
    def get_name(self):
        return self._name
    def get_birthdate(self):
        return self._birthdate
    def get_nationality(self):
        return self._nationality
    def get_website(self):
        return self._website
    def get_contact_info(self):
        return self._contact_info

    #setters
    def set_artist_id(self, artist_id):
        self._artist_id = artist_id

    def set_name(self, name):
        self._name = name

    def set_birthdate(self, birthdate):
        self._birthdate = birthdate

    def set_nationality(self, nationality):
        self._nationality = nationality

    def set_website(self, website):
        self._website = website

    def set_contact_info(self, contact_info):
        self._contact_info = contact_info
