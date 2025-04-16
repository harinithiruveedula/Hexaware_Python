from service.VirtualArt_gallery_service import VirtualArtGalleryImpl

def main():
    gallery_service = VirtualArtGalleryImpl()

    while True:
        print("\n------- Virtual Art Gallery Menu -------")
        print("1. Add Artwork")
        print("2. Update Artwork")
        print("3. Remove Artwork")
        print("4. View Artwork by ID")
        print("5. Search Artworks")
        print("6. Add Artwork to Favorite")
        print("7. Remove Artwork from Favorite")
        print("8. View User's Favorite Artworks")
        print("9. Exit")

        choice = input("\nEnter your choice (1-9): ")

        if choice == '1':
            gallery_service.add_artwork()
        elif choice == '2':
            gallery_service.update_artwork()
        elif choice == '3':
            gallery_service.remove_artwork()
        elif choice == '4':
            gallery_service.get_artwork_by_id()
        elif choice == '5':
            gallery_service.search_artworks()
        elif choice == '6':
            gallery_service.add_artwork_to_favorite()
        elif choice == '7':
            gallery_service.remove_artwork_from_favorite()
        elif choice == '8':
            gallery_service.get_user_favorite_artworks()
        elif choice == '9':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
