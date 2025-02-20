from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    node = TextNode("Sometext", TextType.BOLD, "https://www.boot.dev")
    node2 = HTMLNode("p", "this is the text", "probably replace later with a class object", "proppa")
    print(node) # can print the Class like this since we have the __repr__ set up for this class
    print(node2)

if __name__ == "__main__":
    main()