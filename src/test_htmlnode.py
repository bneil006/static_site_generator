import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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
    
    def test_eq_false_4(self):
        node = HTMLNode("p", "value text", "something", "somethin else")
        node2 = HTMLNode("p", "value text", "something", "something else")
        return self.assertNotEqual(node, node2)
##                                                                                                        ##
#__________________________________________________________________________________________________________#
    
##### LEAF NODES & PARENT NODES #####                                  ##### LEAF NODES & PARENT NODES #####
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
##                                                                                                        ##
#__________________________________________________________________________________________________________#


if __name__ == "__main__":
    unittest.main()