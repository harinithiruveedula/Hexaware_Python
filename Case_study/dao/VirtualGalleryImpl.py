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
            print("Please enter a valid numeric Artwork ID.")
        except Exception as e:
            print("Unexpected error:", e)


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

    def add_artwork_to_favorite(self):
        try:
            user_id = int(input("Enter User ID: "))
            artwork_id = int(input("Enter Artwork ID: "))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            # Check if artwork exists
            cursor.execute("SELECT * FROM Gallery.Artwork WHERE ArtworkID = ?", (artwork_id,))
            if not cursor.fetchone():
                raise ArtWorkNotFoundException(artwork_id)

            # Check if user exists
            cursor.execute("SELECT * FROM Gallery.Users WHERE UserID = ?", (user_id,))
            if not cursor.fetchone():
                raise UserNotFoundException(user_id)

            # Check if already favorite
            cursor.execute("""
                SELECT * FROM Gallery.User_Favorite_Artwork 
                WHERE UserID = ? AND ArtworkID = ?
            """, (user_id, artwork_id))

            if cursor.fetchone():
                print(f"Artwork ID {artwork_id} is already in favorites for User ID {user_id}.")
            else:
                cursor.execute("""
                    INSERT INTO Gallery.User_Favorite_Artwork (UserID, ArtworkID) 
                    VALUES (?, ?)
                """, (user_id, artwork_id))
                conn.commit()
                print(f"✅ Artwork ID {artwork_id} added to favorites for User ID {user_id}.")

            conn.close()

        except (UserNotFoundException, ArtWorkNotFoundException) as e:
            print(e)
        except Exception as e:
            print("❌ Error while adding artwork to favorites:", e)

    def remove_artwork_from_favorite(self) -> bool:
        conn = None
        try:
            user_id = int(input("Enter User ID: "))

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            # Check if user exists
            cursor.execute("SELECT 1 FROM Gallery.Users WHERE UserID = ?", (user_id,))
            if not cursor.fetchone():
                raise UserNotFoundException(user_id)

            # Fetch and display user's favorite artworks
            cursor.execute("""
                SELECT a.ArtworkID, a.Title, a.Medium
                FROM Gallery.User_Favorite_Artwork ufa
                JOIN Gallery.Artwork a ON ufa.ArtworkID = a.ArtworkID
                WHERE ufa.UserID = ?
            """, (user_id,))
            favorites = cursor.fetchall()

            if not favorites:
                print(f"User ID {user_id} has no favorite artworks.")
                return False

            print("\n🎨 Favorite Artworks:")
            for art in favorites:
                print(f"Artwork ID: {art[0]}, Title: {art[1]}, Medium: {art[2]}")

            # Ask which artwork to remove
            artwork_id = int(input("Enter the Artwork ID to remove from favorites: "))

            # Check if it's really in favorites
            cursor.execute("""
                SELECT a.Title FROM Gallery.User_Favorite_Artwork ufa
                JOIN Gallery.Artwork a ON ufa.ArtworkID = a.ArtworkID
                WHERE ufa.UserID = ? AND ufa.ArtworkID = ?
            """, (user_id, artwork_id))
            row = cursor.fetchone()

            if not row:
                raise FavoriteNotFoundException(user_id, artwork_id)

            # Confirm before deleting
            confirm = input(f"Are you sure you want to remove '{row[0]}' from favorites? (yes/no): ").strip().lower()
            if confirm != 'yes':
                print("❎ Deletion canceled.")
                return False

            # Perform delete
            cursor.execute("""
                DELETE FROM Gallery.User_Favorite_Artwork
                WHERE UserID = ? AND ArtworkID = ?
            """, (user_id, artwork_id))
            conn.commit()
            print("✅ Artwork successfully removed from favorites!")
            return True

        except (UserNotFoundException, ArtWorkNotFoundException, FavoriteNotFoundException) as e:
            print("❌", e)
            return False

        except Exception as e:
            print("❌ Unexpected error occurred:", e)
            return False

    def get_user_favorite_artworks(self):
        try:
            user_id = input("Enter User ID to view favorite artworks: ")

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            # Check if user exists
            cursor.execute("SELECT * FROM Gallery.Users WHERE UserID = ?", (user_id,))
            user = cursor.fetchone()

            if not user:
                raise UserNotFoundException(user_id)

            # Fetch favorite artworks
            cursor.execute("""
                SELECT A.ArtworkID, A.Name, A.Description
                FROM Gallery.Artwork A
                JOIN Gallery.User_Favorite_Artwork UFA ON A.ArtworkID = UFA.ArtworkID
                WHERE UFA.UserID = ?
            """, (user_id,))
            artworks = cursor.fetchall()

            if artworks:
                print("🎨 Favorite Artworks:")
                for art in artworks:
                    print(f"ID: {art[0]}, Name: {art[1]}, Description: {art[2]}")
            else:
                print("No favorite artworks found for this user.")

        except Exception as e:
            print("❌ Error retrieving favorite artworks:", e)

    def add_artist(self):
        try:
            name = input("Enter Artist Name: ")
            biography = input("Enter Biography: ")
            birthdate = input("Enter Birthdate (YYYY-MM-DD): ")
            nationality = input("Enter Nationality: ")
            website = input("Enter Website: ")
            contact_info = input("Enter Contact Info: ")

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            insert_query = """
                INSERT INTO Gallery.Artists (Name, Biography, BirthDate, Nationality, Website, ContactInfo)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_query, (name, biography, birthdate, nationality, website, contact_info))
            conn.commit()
            print("✅ Artist added successfully.")

        except Exception as e:
            print("❌ Error adding artist:", e)

    def get_artist_by_id(self):
        try:
            artist_id = int(input("Enter Artist ID: "))
            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Gallery.Artists WHERE ArtistID = ?", (artist_id,))
            artist = cursor.fetchone()
            if artist:
                print("\n--- Artist Details ---")
                print(f"ID: {artist[0]}")
                print(f"Name: {artist[1]}")
                print(f"Biography: {artist[2]}")
                print(f"BirthDate: {artist[3]}")
                print(f"Nationality: {artist[4]}")
                print(f"Website: {artist[5]}")
                print(f"Contact: {artist[6]}")
            else:
                print("❌ Artist not found.")

        except Exception as e:
            print("❌ Error viewing artist:", e)

    def remove_artist_by_id(self):
        try:
            artist_id = int(input("Enter Artist ID to remove: "))
            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            cursor.execute("DELETE FROM Gallery.Artists WHERE ArtistID = ?", (artist_id,))
            conn.commit()

            if cursor.rowcount > 0:
                print("✅ Artist removed successfully.")
            else:
                print("❌ Artist not found.")
        except Exception as e:
            print("❌ Error removing artist:", e)

    def create_virtual_gallery(self):
        try:
            name = input("Enter Gallery Name: ")
            description = input("Enter Description: ")
            location = input("Enter Location: ")
            curator_id = input("Enter Curator (Artist) ID (or leave blank): ")
            opening_hours = input("Enter Opening Hours: ")
            user_id = input("Enter User ID (or leave blank): ")
            gtype = input("Enter Type (Physical/Virtual): ")

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            insert_query = """
                INSERT INTO Gallery.Gallery (Name, Description, Location, CuratorID, OpeningHours, UserID, Type)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_query, (
            name, description, location or None, curator_id or None, opening_hours, user_id or None, gtype))
            conn.commit()
            print("✅ Gallery added successfully.")
        except Exception as e:
            print("❌ Error adding gallery:", e)

    def add_artwork_to_gallery(self):
        try:
            artwork_name = input("Enter Artwork Name: ")
            artist_id = input("Enter Artist ID: ")
            gallery_id = input("Enter Gallery ID: ")
            description = input("Enter Artwork Description: ")
            creation_date = input("Enter Creation Date (YYYY-MM-DD): ")
            price = input("Enter Price: ")
            medium = input("Enter Medium (e.g., oil, sculpture): ")
            dimensions = input("Enter Dimensions (e.g., 30x40 cm): ")

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            insert_query = """
                INSERT INTO Gallery.Artwork (Name, ArtistID, GalleryID, Description, CreationDate, Price, Medium, Dimensions)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_query,
                           (artwork_name, artist_id, gallery_id, description, creation_date, price, medium, dimensions))
            conn.commit()
            print("✅ Artwork added to gallery successfully.")
        except Exception as e:
            print("❌ Error adding artwork to gallery:", e)

    def delete_artwork_from_gallery(self):
        try:
            artwork_id = input("Enter Artwork ID to delete: ")

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            delete_query = """
                DELETE FROM Gallery.Artwork
                WHERE ArtworkID = ?
            """
            cursor.execute(delete_query, (artwork_id,))
            conn.commit()

            if cursor.rowcount > 0:
                print("✅ Artwork deleted successfully.")
            else:
                print("❌ Artwork not found.")
        except Exception as e:
            print("❌ Error deleting artwork:", e)

    def delete_virtual_gallery(self):
        try:
            gallery_id = int(input("Enter Gallery ID to delete: "))
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Gallery.Gallery WHERE GalleryID = ?", (gallery_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print("✅ Gallery deleted successfully.")
            else:
                print("❌ Gallery not found.")
        except Exception as e:
            print("❌ Error deleting gallery:", e)

    def view_virtual_galleries(self):
        try:
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Gallery.Gallery")
            rows = cursor.fetchall()

            if not rows:
                print("No galleries found.")
            else:
                print("\n--- Galleries ---")
                for g in rows:
                    print(f"\nID: {g[0]}, Name: {g[1]}, Description: {g[2]}, Type: {g[7]}, CreatedAt: {g[8]}")

        except Exception as e:
            print("❌ Error retrieving galleries:", e)

    def add_user(self):
        try:
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            email = input("Enter Email: ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            dob = input("Enter Date of Birth (YYYY-MM-DD): ")

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            insert_query = """
                INSERT INTO Gallery.Users (Username, Password, Email, FirstName, LastName, DateOfBirth)
                VALUES (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_query, (username, password, email, first_name, last_name, dob))
            conn.commit()
            print("✅ User added successfully.")

        except Exception as e:
            print("❌ Error adding user:", e)

    def get_user_by_id(self):
        try:
            user_id = input("Enter User ID: ").strip()

            # Check if input is a valid integer
            if not user_id.isdigit():
                print("❌ Invalid User ID. Please enter a numeric value.")
                return

            user_id = int(user_id)

            conn = DBConnection.get_connection()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM gallery.Users WHERE UserID = ?", (user_id,))
            result = cursor.fetchone()

            if result:
                print(f"✅ UserID: {result[0]}, Name: {result[1]}, Email: {result[2]}")
                return result
            else:
                raise UserNotFoundException(user_id)

        except UserNotFoundException as ue:
            print(f"❌ {ue}")
        except Exception as e:
            print("❌ Unexpected error:", e)


    def remove_user_by_id(self):
        try:
            user_id = int(input("Enter User ID to remove: "))
            conn = DBConnection.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Gallery.Users WHERE UserID = ?", (user_id,))
            conn.commit()
            if cursor.rowcount > 0:
                print("✅ User removed successfully.")
            else:
                print("❌ User not found.")
        except Exception as e:
            print("❌ Error removing user:", e)
