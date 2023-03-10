from __future__ import annotations

"""
This framework is meant for DOM creation, not for frontend work.
If you need to create a very complex and multi-faceted DOM, then
you should definitely use CaMuL! 

It compiles to HTML and CSS.
"""


class Class:
    def __init__(self, selector='', rules={}):
        self.selector = selector
        self.rules = rules
        self.psuedoclasses = []

        register_as_class(self)

    def to_string(self):
        out = self.selector + " {"
        for rule in self.rules.keys():
            out += f"\n  {rule}: {self.rules[rule]};"
        return out + "\n}"

class HTMLElement:
    def __init__(self, tag='div', **kwargs):
        self.__dict__.update(kwargs)
        if not hasattr(self, 'innerHTML'):
            self.innerHTML = []
        elif isinstance(self.innerHTML, str):
            self.innerHTML = [self.innerHTML]
        self.tag = tag
        self.self_closing = ["link", "meta"].count(tag) > 0

    def appendChild(self, element) -> HTMLElement:
        if element is not self:
            self.innerHTML.append(element)
        return element

    def removeChild(self, element) -> HTMLElement:
        """
        Removes an element object from the innerHTML of an element.
        Used for dynamic DOM creation.
        """
        self.innerHTML.remove(element)
        return element

    def getElementById(self, id) -> HTMLElement:
        for child in self.innerHTML:
            if child.id == id:
                return child
        return None

    def to_string(self, level=0) -> str:
        
        indent = '  ' * level
        child_indent = '  ' * (level + 1)
        childrenstr = ""
        if hasattr(self, 'innerHTML'):
            
            for child in self.innerHTML:
                if child is self:
                    continue
                if isinstance(child, HTMLElement):
                    childrenstr += child.to_string(level + 1)
                else:
                    childrenstr += str(child)
            
        styles = "class="
        if hasattr(self, 'class'):
            for styleclass in self.classlist:
                if type(styleclass) == type(Class()) and styleclass.selector.startswith("."):
                    styles += styleclass.selector[1:len(styleclass.selector)] + " "
        classtag = styles if styles != "class=" else ""

        attrs = ""
        for attr in vars(self).keys():
            if ["innerHTML", "classlist", "tag", "self_closing"].count(attr) < 1:
                attrs += f"{attr}='{vars(self)[attr]}' "


        opening_tag = f"{indent}<{self.tag} {attrs}{classtag}"
        closing_tag = f"</{self.tag}>"
        if self.self_closing:
            opening_tag += "/>"
            closing_tag = ""
        else:
            opening_tag += ">"
        return f"{opening_tag.strip()}\n{child_indent}{childrenstr}\n{indent}{closing_tag}\n{indent}"

# generate header
document = HTMLElement(tag="html", lang="en", innerHTML="")
header = HTMLElement(tag="head")
header.appendChild(HTMLElement(tag="link", rel="stylesheet", href="style.css"))
title = HTMLElement(tag="title")
title.appendChild("Document")
header.appendChild(title)
document.appendChild(header)
classes = []
def register_as_class(style: Class):
    classes.append(style)

def compile():
    classes_str = ""
    for cls in classes:
        classes_str += cls.to_string() + "\n\n"
    return f'<!DOCTYPE html>\n\n{document.to_string()}', classes_str

def export(dom_output, css_output):
    html_file = open("src/index.html", "wt")
    css_file = open("src/style.css", "wt")

    n1=html_file.write(dom_output)
    n2=css_file.write(css_output)

    html_file.close()
    css_file.close()

    print(f'Exported: {n1}, {n2}')

if __name__ == "__main__":
    print("This is the compiler, silly! Run app.py to run your code!")
else:
    print("CaMuL Initialized.")