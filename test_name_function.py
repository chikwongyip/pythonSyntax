import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """测试name function.py"""
    def test_first_last_name(self):
        """能够正确处理吗？"""
        formatted_name = get_formatted_name("janis","joplin")
        self.assertEqual(formatted_name,"Jains Joplin")

unittest.main()