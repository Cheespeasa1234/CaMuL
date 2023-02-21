from __future__ import annotations

"""
This framework is meant for DOM creation, not for frontend work.
If you need to create a very complex and multi-faceted DOM, then
you should definitely use CaMuL! 

It compiles to HTML and CSS.
"""

class Style:
  def __init__(self, selector=':root', rules={}):
    self.selector = selector
    self.rules = rules

class HTMLElement:
  def __init__(self, tag="html", innerHTML=[], id="", classlist=[]):
    self.innerHTML = innerHTML
    self.classlist = classlist
    self.tag = tag
    self.id = id

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
    childrenstr = ""
    for child in filter(lambda e:e is not self,self.innerHTML):
      if isinstance(child, HTMLElement):
        childrenstr += child.to_string(level + 1)
      else:
        childrenstr += str(child)
    return f"{indent}<{self.tag} class={self.classlist}>\n{childrenstr}\n{indent}</{self.tag}>\n"

class p(HTMLElement):
  def __init__(self, inner):
    super().__init__(tag="p", innerHTML=[inner], classlist=['&p'], id="")

def render(document: HTMLElement) -> None:
  output = document.to_string

if __name__ == "__main__":
  print("This is the compiler, silly! Run app.py to run your code!")
else:
  print("CaMuL Initialized.")