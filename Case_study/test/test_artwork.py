import unittest
from dao.VirtualGalleryImpl import VirtualArtGalleryImpl
from exception.app_exceptions import ArtWorkNotFoundException

class TestArtworkService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.service = VirtualArtGalleryImpl()

    def test_get_artwork_by_valid_id(self):
        result = self.service.get_artwork_by_id(artwork_id=13)
        self.assertIsNotNone(result)

    """def test_get_artwork_by_invalid_id(self):
        with self.assertRaises(ArtWorkNotFoundException):
            self.service.get_artwork_by_id(artwork_id=13)"""

    def test_add_artwork(self):
        result = self.service.add_artwork()
        self.assertIsNotNone(result)
    def test_remove_artwork(self):
        result = self.service.remove_artwork()
        self.assertIsNotNone(result)



if __name__ == '__main__':
    unittest.main()
