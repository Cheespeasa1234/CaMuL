class HTMLElement:
  def __init__(self, tag="html", innerHTML=[], id="", classlist=[]):
    self.innerHTML = innerHTML
    self.classlist = classlist
    self.tag = tag
    self.id = id

  def appendChild(self, element):
    if element is not self:
      self.innerHTML.append(element)

  def removeChild(self, element):
    self.innerHTML.remove(element)

  def getElementById(self, id):
    for child in self.innerHTML:
      if child.id == id:
        return child;
    return None;

  def to_string(self, level=0):
    indent = '  ' * level
    childrenstr = ""
    for child in filter(lambda e:e is not self,self.innerHTML):
      if isinstance(child, HTMLElement):
        childrenstr += child.to_string(level + 1)
      else:
        childrenstr += str(child)
    return f"{indent}<{self.tag} level={level} class={self.classlist}>\n{childrenstr}\n{indent}</{self.tag}>\n"

class p(HTMLElement):
  def __init__(self, inner):
    super().__init__(tag="p", innerHTML=[inner], classlist=['&p'], id="")

print("CaMuL Initialized.")
print("I am ", __name__)