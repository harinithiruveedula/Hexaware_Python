from util.DBConnection import DBConnection
from entity.artwork import Artwork
from dao.IVirtualArtGallery import IVirtualArtGallery

from exception.app_exceptions import *


class VirtualArtGalleryImpl(IVirtualArtGallery):


    def add_artwork(self, artwork: Artwork = None) -> bool:
        try:
            if artwork is None:
                print("------ Hey! Enter your Artwork details -----")

                title = input("Enter Title: ")
                description = input("Enter Description: ")
                creation_date = input("Enter Creation Date (YYYY-MM-DD): ")
                medium = input("Enter Medium: ")
                image_url = input("Enter Image URL: ")
                artist_id = int(input("Enter Artist ID: "))

                artwork = Artwork(0, title, description, creation_date, medium, image_url, artist_id)

            # Connect to DB and insert
            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            insert_query = """
                INSERT INTO Gallery.Artwork 
                (Title, Description, CreationDate, Medium, ImageURL, ArtistID)
                VALUES (?, ?, ?, ?, ?, ?)
            """

            cursor.execute(insert_query, (
                artwork.get_title(),
                artwork.get_description(),
                artwork.get_creation_date(),
                artwork.get_medium(),
                artwork.get_image_url(),
                artwork.get_artist_id()
            ))

            conn.commit()

            print("Artwork details inserted successfully.")
            print("\n🎨 All Artworks in the Database:")
            select_query = """
                        SELECT ArtworkID, Title, Description, CreationDate, Medium, ImageURL, ArtistID 
                        FROM Gallery.Artwork
                    """
            cursor.execute(select_query)
            artworks = cursor.fetchall()
            for row in artworks:
                print(f"\nArtwork ID: {row[0]}")
                print(f"Title: {row[1]}")
                print(f"Description: {row[2]}")
                print(f"Creation Date: {row[3]}")
                print(f"Medium: {row[4]}")
                print(f"Image URL: {row[5]}")
                print(f"Artist ID: {row[6]}")


            return True


        except Exception as e:
            print(" Error while inserting artwork:", e)
            return False

    def update_artwork(self) -> bool:
        try:
            artwork_id = int(input("Enter the ArtworkID to update: "))

            # First check if it exists
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Gallery.Artwork WHERE ArtworkID = ?", (artwork_id,))
            if cursor.fetchone() is None:
                raise ArtWorkNotFoundException(artwork_id)

            print("\nWhich field do you want to update?")
            print("1. Title\n2. Description\n3. CreationDate\n4. Medium\n5. ImageURL\n6. ArtistID")
            choice = input("Enter your choice (1-6): ")

            # Debugging line to check the input
            print(f"Debug: User selected choice: {choice}")

            field_map = {
                '1': 'Title',
                '2': 'Description',
                '3': 'CreationDate',
                '4': 'Medium',
                '5': 'ImageURL',
                '6': 'ArtistID'
            }

            if choice not in field_map:
                print("Invalid choice.")
                return False

            new_value = input(f"Enter new value for {field_map[choice]}: ")

            update_query = f"UPDATE Gallery.Artwork SET {field_map[choice]} = ? WHERE ArtworkID = ?"
            cursor.execute(update_query, (new_value, artwork_id))
            conn.commit()

            print("✅ Artwork updated successfully.")

            # Select and display all artworks
            cursor.execute("SELECT * FROM Gallery.Artwork")
            artworks = cursor.fetchall()
            print("\nAll Artworks after update:")
            for artwork in artworks:
                print(f"ArtworkID: {artwork[0]}, Title: {artwork[1]}, ArtistID: {artwork[6]}, Medium: {artwork[4]}")

            return True

        except ArtWorkNotFoundException as ae:
            print(ae)
            raise

        except Exception as e:
            print("❌ Error updating artwork:", e)
            return False

    def remove_artwork(self) -> bool:
        try:
            artwork_id = int(input("Enter the ArtworkID to remove: "))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Gallery.Artwork WHERE ArtworkID = ?", (artwork_id,))
            if cursor.fetchone() is None:
                raise ArtWorkNotFoundException(artwork_id)

            delete_query = "DELETE FROM Gallery.Artwork WHERE ArtworkID = ?"
            cursor.execute(delete_query, (artwork_id,))
            conn.commit()

            print("✅ Artwork removed successfully.")

            # Select and display all artworks
            cursor.execute("SELECT * FROM Gallery.Artwork")
            artworks = cursor.fetchall()
            print("\nAll Artworks after removal:")
            for artwork in artworks:
                print(f"ArtworkID: {artwork[0]}, Title: {artwork[1]}, ArtistID: {artwork[6]}, Medium: {artwork[4]}")


            return True

        except ArtWorkNotFoundException as ae:
            print(ae)
            raise

        except Exception as e:
            print("❌ Error removing artwork:", e)
            return False

    def get_artwork_by_id(self, artwork_id=None):
        try:
            if artwork_id is None:
                artwork_id = int(input("Enter Artwork ID to fetch: "))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM gallery.Artwork WHERE ArtworkID = ?", (artwork_id,))
            result = cursor.fetchone()

            if result:
                print("\n🎨 Artwork Details:")
                print(f"ArtworkID: {result[0]}")
                print(f"Title: {result[1]}")
                print(f"Description: {result[2]}")
                print(f"CreationDate: {result[3]}")
                print(f"Medium: {result[4]}")
                print(f"ImageURL: {result[5]}")
                print(f"ArtistID: {result[6]}")
                return result
            else:
                raise ArtWorkNotFoundException(artwork_id)

        except ArtWorkNotFoundException as ae:
            print(f"❌ {ae}")
            raise
        except ValueError:
            print("⚠ Please enter a valid numeric Artwork ID.")
        except Exception as e:
            print("⚠ Unexpected error:", e)

    def get_user_by_id(self, user_id):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM gallery.Users WHERE UserID = ?", (user_id,))
            result = cursor.fetchone()

            if result:
                print(f"UserID: {result[0]}, Name: {result[1]}, Email: {result[2]}")
                return result
            else:
                raise UserNotFoundException(user_id)

        except UserNotFoundException as ue:
            print(ue)
            raise
        except Exception as e:
            print("⚠ Unexpected error:", e)

    def search_artworks(self) -> list[Artwork]:
        # Ask the user for the search keyword
        keyword = input("Enter a keyword to search: ")

        artworks = []
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            query = """
                SELECT ArtworkID, Title, Description, CreationDate, Medium, ImageURL, ArtistID
                FROM Gallery.Artwork
                WHERE Title LIKE ? OR Description LIKE ? OR Medium LIKE ?
            """

            wildcard_keyword = f"%{keyword}%"
            cursor.execute(query, (wildcard_keyword, wildcard_keyword, wildcard_keyword))
            rows = cursor.fetchall()

            if rows:
                print("\nSearch Results:")
                for row in rows:
                    print(f"ArtworkID: {row[0]}, Title: {row[1]}, ArtistID: {row[6]}, Medium: {row[4]}")

                for row in rows:
                    artwork = Artwork(
                        artwork_id=row[0],
                        title=row[1],
                        description=row[2],
                        creation_date=row[3],
                        medium=row[4],
                        image_url=row[5],
                        artist_id=row[6]
                    )
                    artworks.append(artwork)
            else:
                print("No artworks found matching your search.")


        except Exception as e:
            print("❌ Error while searching artworks:", e)

        return artworks


    def add_artwork_to_favorite(self) -> bool:
        conn = None
        try:
            user_id = int(input("Enter User ID: "))
            artwork_id = int(input("Enter Artwork ID: "))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            # Check if user exists
            cursor.execute("SELECT 1 FROM Gallery.Users WHERE UserID = ?", (user_id,))
            if not cursor.fetchone():
                raise UserNotFoundException(user_id)

            # Check if artwork exists
            cursor.execute("SELECT 1 FROM Gallery.Artwork WHERE ArtworkID = ?", (artwork_id,))
            if not cursor.fetchone():
                raise ArtWorkNotFoundException(artwork_id)

            # Check if already in favorites
            cursor.execute("SELECT 1 FROM Gallery.User_Favorite_Artwork WHERE UserID = ? AND ArtworkID = ?",
                           (user_id, artwork_id))
            if cursor.fetchone():
                raise AlreadyFavoriteException(user_id, artwork_id)

            # Add to favorites
            cursor.execute("""
                INSERT INTO Gallery.User_Favorite_Artwork (UserID, ArtworkID)
                VALUES (?, ?)
            """, (user_id, artwork_id))
            conn.commit()
            print("✅ Artwork successfully added to favorites!")
            return True

        except (UserNotFoundException, ArtWorkNotFoundException, AlreadyFavoriteException) as e:
            print("❌", e)
            raise


        except Exception as e:
            print("❌ Unexpected error occurred:", e)
            return False

    def remove_artwork_from_favorite(self) -> bool:
        conn = None
        try:
            user_id = int(input("Enter User ID: "))
            artwork_id = int(input("Enter Artwork ID: "))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            # Check if user exists
            cursor.execute("SELECT 1 FROM Gallery.Users WHERE UserID = ?", (user_id,))
            if not cursor.fetchone():
                raise UserNotFoundException(user_id)

            # Check if artwork exists
            cursor.execute("SELECT 1 FROM Gallery.Artwork WHERE ArtworkID = ?", (artwork_id,))
            if not cursor.fetchone():
                raise ArtWorkNotFoundException(artwork_id)

            # Check if favorite exists
            cursor.execute("""
                SELECT 1 FROM Gallery.User_Favorite_Artwork 
                WHERE UserID = ? AND ArtworkID = ?
            """, (user_id, artwork_id))
            if not cursor.fetchone():
                raise FavoriteNotFoundException(user_id, artwork_id)

            # Delete favorite
            cursor.execute("""
                DELETE FROM Gallery.User_Favorite_Artwork
                WHERE UserID = ? AND ArtworkID = ?
            """, (user_id, artwork_id))
            conn.commit()
            print("✅ Artwork successfully removed from favorites!")
            return True

        except (UserNotFoundException, ArtWorkNotFoundException, FavoriteNotFoundException) as e:
            print("❌", e)
            raise



        except Exception as e:
            print("❌ Unexpected error occurred:", e)
            return False

    def get_user_favorite_artworks(self) -> bool:
        conn = None
        try:
            user_id = int(input("Enter User ID to view favorite artworks: "))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            # Check if user exists
            cursor.execute("SELECT 1 FROM Gallery.Users WHERE UserID = ?", (user_id,))
            if not cursor.fetchone():
                raise UserNotFoundException(user_id)

            # Fetch favorite artworks
            query = """
                   SELECT A.ArtworkID, A.Title, A.Medium, A.CreationDate, A.ArtistID
                   FROM Gallery.Artwork A
                   INNER JOIN Gallery.User_Favorite_Artwork UFA ON A.ArtworkID = UFA.ArtworkID
                   WHERE UFA.UserID = ?
               """
            cursor.execute(query, (user_id,))
            rows = cursor.fetchall()

            if rows:
                print(f"\n🎨 Favorite Artworks for User ID {user_id}:")
                for row in rows:
                    print(
                        f"ArtworkID: {row[0]}, Title: {row[1]}, Medium: {row[2]}, Created On: {row[3]}, Artist ID: {row[4]}")
                return True
            else:
                print(f"ℹ️ No favorite artworks found for User ID {user_id}.")
                return False

        except UserNotFoundException as e:
            print("❌", e)
            raise

