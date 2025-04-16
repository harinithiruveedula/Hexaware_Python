class ArtWorkNotFoundException(Exception):
    def __init__(self, artwork_id):
        super().__init__(f"Artwork with ID {artwork_id} not found in the database.")


class UserNotFoundException(Exception):
    def __init__(self, user_id):
        super().__init__(f"User with ID {user_id} not found in the database.")

class AlreadyFavoriteException(Exception):
    def __init__(self, user_id, artwork_id):
        super().__init__(f"Artwork with ID {artwork_id} is already in favorites for User ID {user_id}.")
class FavoriteNotFoundException(Exception):
    def __init__(self, user_id, artwork_id):
        super().__init__(f"Favorite entry not found for User ID {user_id} and Artwork ID {artwork_id}.")

class ArtistNotFoundException(Exception):
    def __init__(self, message="Artist not found."):
        super().__init__(message)
