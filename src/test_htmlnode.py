import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
# ________________________________________________SUCESS CASES______________________________________________#
##                                                                                                         ##
    def test_eq(self):
        node = HTMLNode("p", "value text", "something", "something else")
        node2 = HTMLNode("p", "value text", "something", "something else")
        return self.assertEqual(node, node2)
    
    def test_eq_repr(self):
        node = HTMLNode("p", "value text", "something", "something else")
        self.assertEqual("HTMLNode(p, value text, something, something else)", repr(node))
##                                                                                                         ##
# ________________________________________________FAIL CASES________________________________________________#
##                                                                                                         ##
    def test_eq_false_1(self):
        node = HTMLNode("a", "value text", "something", "something else")
        node2 = HTMLNode("p", "value text", "something", "something else")
        return self.assertNotEqual(node, node2)
    
    def test_eq_false_2(self):
        node = HTMLNode("p", "val text", "something", "something else")
        node2 = HTMLNode("p", "value text", "something", "something else")
        return self.assertNotEqual(node, node2)
    
    def test_eq_false_3(self):
        node = HTMLNode("p", "value text", "somthing", "something else")
        node2 = HTMLNode("p", "value text", "something", "something else")
        return self.assertNotEqual(node, node2)
    
    def test_eq_false_3(self):
        node = HTMLNode("p", "value text", "something", "somethin else")
        node2 = HTMLNode("p", "value text", "something", "something else")
        return self.assertNotEqual(node, node2)
##                                                                                                        ##
#__________________________________________________________________________________________________________#


if __name__ == "__main__":
    unittest.main()