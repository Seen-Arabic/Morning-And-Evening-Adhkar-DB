import unittest
import json
import os

class TestDataIntegrity(unittest.TestCase):
    def setUp(self):
        # Assuming tests are run from the project root
        self.ar_path = 'ar.json'
        self.en_path = 'en.json'

        with open(self.ar_path, 'r', encoding='utf-8') as f:
            self.ar_data = json.load(f)

        with open(self.en_path, 'r', encoding='utf-8') as f:
            self.en_data = json.load(f)

    def test_ar_fields_exist(self):
        required_fields = {
            "order", "content", "count", "count_description",
            "fadl", "source", "type", "audio",
            "hadith_text", "explanation_of_hadith_vocabulary"
        }
        for item in self.ar_data:
            self.assertTrue(required_fields.issubset(item.keys()),
                            f"Missing fields in ar.json item: {item.get('order', 'unknown')}")

    def test_en_fields_exist(self):
        required_fields = {
            "order", "content", "translation", "transliteration",
            "count", "count_description", "fadl", "source",
            "type", "audio", "hadith_text", "explanation_of_hadith_vocabulary"
        }
        for item in self.en_data:
            self.assertTrue(required_fields.issubset(item.keys()),
                            f"Missing fields in en.json item: {item.get('order', 'unknown')}")

    def test_count_description_values(self):
        # Mapping for specific counts to check.
        # Note: Text matching might be sensitive to diacritics.
        # We will check for containment of key phrases or exact matches where appropriate.

        for item in self.ar_data:
            count = item.get('count')
            desc = item.get('count_description', '')

            if count == 1:
                self.assertIn("مَرَّةٌ وَاحِدَةٌ", desc, f"Invalid description for count 1 in item {item['order']}")
            elif count == 2:
                # User specifically asked for this check: "مرتين"
                self.assertIn("مرتين", desc, f"Description for count 2 should contain 'مرتين' in item {item['order']}")
            elif count == 3:
                self.assertIn("ثَلَاثُ مَرَّاتٍ", desc, f"Invalid description for count 3 in item {item['order']}")
            elif count == 4:
                self.assertIn("أَربَعُ مَرَّاتٍ", desc, f"Invalid description for count 4 in item {item['order']}")
            elif count == 7:
                 self.assertIn("سَبعُ مَرَّاتٍ", desc, f"Invalid description for count 7 in item {item['order']}")
            elif count == 10:
                # "عَشرُ" or "عَشرَ" depending on grammar, checking broadly
                self.assertIn("عَشر", desc, f"Invalid description for count 10 in item {item['order']}")
            elif count == 100:
                self.assertIn("مِائَةُ مَرَّةٍ", desc, f"Invalid description for count 100 in item {item['order']}")
            else:
                self.fail(f"Unexpected count value: {count} in item {item['order']}")

    def test_en_count_description_values(self):
        for item in self.en_data:
            count = item.get('count')
            desc = item.get('count_description', '')

            if count == 1:
                self.assertEqual("Once", desc.strip(), f"Invalid description for count 1 in item {item['order']}")
            elif count == 2:
                self.fail(f"Count 2 not expected in current en.json data (item {item['order']}) - delete this if 2 is valid now")
            elif count == 3:
                self.assertIn("Three times", desc, f"Invalid description for count 3 in item {item['order']}")
            elif count == 4:
                self.assertIn("Four times", desc, f"Invalid description for count 4 in item {item['order']}")
            elif count == 7:
                 self.assertIn("Seven times", desc, f"Invalid description for count 7 in item {item['order']}")
            elif count == 10:
                self.assertIn("Ten times", desc, f"Invalid description for count 10 in item {item['order']}")
            elif count == 100:
                self.assertIn("One hundred times", desc, f"Invalid description for count 100 in item {item['order']}")
            else:
                 self.fail(f"Unexpected count value: {count} in item {item['order']}")

    def test_order_uniqueness(self):
        ar_orders = [item['order'] for item in self.ar_data]
        en_orders = [item['order'] for item in self.en_data]

        self.assertEqual(len(ar_orders), len(set(ar_orders)), "Duplicate order IDs found in ar.json")
        self.assertEqual(len(en_orders), len(set(en_orders)), "Duplicate order IDs found in en.json")

    def test_cross_file_consistency(self):
        self.assertEqual(len(self.ar_data), len(self.en_data), "ar.json and en.json have different number of items")

        ar_orders = set(item['order'] for item in self.ar_data)
        en_orders = set(item['order'] for item in self.en_data)

        self.assertEqual(ar_orders, en_orders, "Mismatch in order IDs between ar.json and en.json")

        # Check that counts match for the same order
        ar_dict = {item['order']: item for item in self.ar_data}
        en_dict = {item['order']: item for item in self.en_data}

        for order in ar_orders:
            ar_item = ar_dict[order]
            en_item = en_dict[order]

            self.assertEqual(ar_item.get('count'), en_item.get('count'),
                             f"Count mismatch for item order {order}: ar={ar_item.get('count')}, en={en_item.get('count')}")

if __name__ == '__main__':
    unittest.main()
