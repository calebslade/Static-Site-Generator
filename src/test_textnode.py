import unittest

from textnode import (TextNode,   
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_text)
        self.assertEqual(node, node2)
    
    def test_neq(self):
        node = TextNode("This is a text node", text_type_text)
        node2 = TextNode("This is a text node", text_type_bold)
        self.assertNotEqual(node,node2)

    def test_eqnone(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold", None)
        self.assertEqual(node,node2)

    def text_eq_url(self):
        node = TextNode('This is a text node', text_type_text, "google.com")
        node2 = TextNode('This is a text node', text_type_text, "google.com")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_text, "google.com")
        self.assertEqual("TextNode(This is a text node, text, google.com)", repr(node))
        
if __name__ == "__main__":
    unittest.main()