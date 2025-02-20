import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
# ________________________________________________SUCESS CASES______________________________________________#
##                                                                                                         ##
    def test_eq(self):
        node = TextNode("This is some text", TextType.BOLD)
        node2 = TextNode("This is some text", TextType.BOLD)
        return self.assertEqual(node, node2)
    
    def test_eq_url(self):
        node = TextNode("Some Text", TextType.CODE, "https://www.boot.dev")
        node2 = TextNode("Some Text", TextType.CODE, "https://www.boot.dev")
        return self.assertEqual(node, node2)
    
    def test_eq_repr(self):
        node = TextNode("Some Text", TextType.BOLD, "https://www.boot.dev")
        self.assertEqual("TextNode(Some Text, bold, https://www.boot.dev)", repr(node))
##                                                                                                         ##
# ________________________________________________FAIL CASES________________________________________________#
##                                                                                                         ##
    def test_eq_false_1(self):
        node = TextNode("Some Txet", TextType.CODE, "https://www.boot.dev")
        node2 = TextNode("Some Text", TextType.CODE, "https://www.boot.dev")
        return self.assertNotEqual(node, node2)
    
    def test_eq_false_2(self):
        node = TextNode("Some Text", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("Some Text", TextType.CODE, "https://www.boot.dev")
        return self.assertNotEqual(node, node2)
    
    def test_eq_false_3(self):
        node = TextNode("Some Text", TextType.CODE, "https://www.google.com")
        node2 = TextNode("Some Text", TextType.CODE, "https://www.boot.dev")
        return self.assertNotEqual(node, node2)
##                                                                                                        ##
#__________________________________________________________________________________________________________#


if __name__ == "__main__":
    unittest.main()