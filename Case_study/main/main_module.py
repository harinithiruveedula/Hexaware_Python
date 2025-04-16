from service.VirtualArt_gallery_service import VirtualArtGalleryImpl

def main():
    gallery_service = VirtualArtGalleryImpl()

    while True:
        print("\n======= VIRTUAL ART GALLERY SYSTEM =======")
        print("1. Artist Operations")
        print("2. Artwork Operations")
        print("3. Favorite Operations")
        print("4. Gallery Operations")
        print("5. User Operations")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            while True:
                print("\n--- ARTIST OPERATIONS ---")
                print("1. Add Artist")
                print("2. View Artist by ID")
                print("3. Remove Artist by ID")
                print("4. Back to Main Menu")

                artist_choice = input("Enter your choice: ")
                if artist_choice == '1':
                    gallery_service.add_artist()
                elif artist_choice == '2':
                    gallery_service.get_artist_by_id()
                elif artist_choice == '3':
                    gallery_service.remove_artist_by_id()
                elif artist_choice == '4':
                    break
                else:
                    print("Invalid input. Try again.")

        elif choice == '2':
            while True:
                print("\n--- ARTWORK OPERATIONS ---")
                print("1. Add Artwork")
                print("2. Update Artwork")
                print("3. Remove Artwork")
                print("4. View Artwork by ID")
                print("5. Search Artworks")
                print("6. Back to Main Menu")

                artwork_choice = input("Enter your choice: ")
                if artwork_choice == '1':
                    gallery_service.add_artwork()
                elif artwork_choice == '2':
                    gallery_service.update_artwork()
                elif artwork_choice == '3':
                    gallery_service.remove_artwork()
                elif artwork_choice == '4':
                    gallery_service.get_artwork_by_id()
                elif artwork_choice == '5':
                    gallery_service.search_artworks()
                elif artwork_choice == '6':
                    break
                else:
                    print("Invalid input. Try again.")

        elif choice == '3':
            while True:
                print("\n--- FAVORITE OPERATIONS ---")
                print("1. Add Artwork to Favorite")
                print("2. Remove Artwork from Favorite")
                print("3. View User's Favorite Artworks")
                print("4. Back to Main Menu")

                fav_choice = input("Enter your choice: ")
                if fav_choice == '1':
                    gallery_service.add_artwork_to_favorite()
                elif fav_choice == '2':
                    gallery_service.remove_artwork_from_favorite()
                elif fav_choice == '3':
                    gallery_service.get_user_favorite_artworks()
                elif fav_choice == '4':
                    break
                else:
                    print("Invalid input. Try again.")

        elif choice == '4':
            while True:
                print("\n--- GALLERY OPERATIONS ---")
                print("1. Create Virtual Gallery")
                print("2. Add Artwork to Gallery")
                print("3. Remove Artwork from Gallery")
                print("4. Delete Virtual Gallery")
                print("5. View All Virtual Galleries")

                print("6. Back to Main Menu")

                gallery_choice = input("Enter your choice: ")
                if gallery_choice == '1':
                    gallery_service.create_virtual_gallery()
                elif gallery_choice == '2':
                    gallery_service.add_artwork_to_gallery()
                elif gallery_choice == '3':
                    gallery_service.delete_artwork_from_gallery()
                elif gallery_choice == '4':
                    gallery_service.delete_virtual_gallery()
                elif gallery_choice == '5':
                    gallery_service.view_virtual_galleries()

                elif gallery_choice == '6':
                    break
                else:
                    print("Invalid input. Try again.")

        elif choice == '5':
            while True:
                print("\n--- USER OPERATIONS ---")
                print("1. Add User")
                print("2. View User by ID")
                print("3. Delete User")
                print("4. Back to Main Menu")

                user_choice = input("Enter your choice: ")
                if user_choice == '1':
                    gallery_service.add_user()
                elif user_choice == '2':
                    gallery_service.get_user_by_id()
                elif user_choice == '3':
                    gallery_service.remove_user_by_id()
                elif user_choice == '4':
                    break
                else:
                    print("Invalid input. Try again.")

        elif choice == '6':
            print("👋 Exiting the system. Goodbye!")
            break
        else:
            print("❌ Invalid main menu choice. Try again.")

if __name__ == "__main__":
    main()
