from CaMuL import *;

document = HTMLElement(tag="body", classlist=[], id="body", innerHTML=[
    p("Hello, World!"),
    p("Goodbye, World!")
  ]
)

print(document.to_string())