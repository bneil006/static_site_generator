
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag # An HTMLNode without a tag will just render as raw text
        self.value = value # An HTMLNode without a value will be assumed to have children
        self.children = children # An HTMLNode without children will be assumed to have a value
        self.props = props # An HTMLNode without props simply won't have any attributes

    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None: return "" # want to return as "" so that in our to_html in our LeafNode() we can capture a href properly and <p> properly without adding None to the text
        formatted = ""
        for i in self.props:
            formatted += f' {i}="{self.props[i]}"'
        return formatted

# A LeafNode is a type of HTMLNode that represents a single HTML tag with no children. For example, a simple <p> tag with some text inside of it
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None): # removed children parameter, tag along with value required for this one, though tag may be None
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None: raise ValueError("invalid HTML: no value")
        if self.tag is None: return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"



def something():
    html_node = HTMLNode("p", "this is the text", "probably replace later with a class object", None)
    a = LeafNode("p", "This is a paragraph of text.")
    b = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(a.to_html())
    print(b.to_html())

something()