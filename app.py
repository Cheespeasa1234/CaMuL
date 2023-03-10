from CaMuL import *

# Example Script
button = HTMLElement(
    tag="button", 
    classlist=['colorful'], 
    onclick="alert(1);",
    innerHTML='Hello, World!'
) # Make a button

list = HTMLElement(
    tag="ul", classlist=['colorful'],
    innerHTML=[
        HTMLElement(tag="li", innerHTML="Hello!"),
        HTMLElement(tag="li", innerHTML="World!"),
        HTMLElement(tag="li", innerHTML="Alive!")
    ]
)

document.appendChild(button) # Add the button to the DOM
document.appendChild(list) # Add the button to the DOM

colorful = Class(selector=".colorful", rules={ # Make a style
    'color': 'red',
    'font-weight': 'bold'
})
colorful_before = Class(selector=".colorful::before", rules={ # Make a pseudo-style
    'content': '">> "'
})

export(*compile())