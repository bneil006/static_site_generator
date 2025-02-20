import unittest
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
#_________________________________________________SUCESS CASES______________________________________________#
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
#_________________________________________________FAIL CASES________________________________________________#
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
##                                                                                                         ##
#___________________________________________________________________________________________________________#


class TestTextNodeToHTMLNode(unittest.TestCase):
#_________________________________________________SUCESS CASES______________________________________________#
##                                                                                                         ##
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
##                                                                                                         ##
#___________________________________________________________________________________________________________#


if __name__ == "__main__":
    unittest.main()