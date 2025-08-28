import re

def get_tag_name(tag):
    # Get tag name, ignoring attributes
    tag = tag.strip('<>/')
    parts = tag.split()
    return parts

def validate_html_tags_with_attr(html):
    stack = []
    regex = re.compile(r'<[^>]+>')
    tags = regex.findall(html)
    for tag in tags:
        if tag[2] != '/': 
            if tag[-2:] != '/>':  
                stack.append(get_tag_name(tag))
        else:  # Closing tag
            if not stack or stack[-1] != get_tag_name(tag):
                return False
            stack.pop()
    return len(stack) == 0

    
html1 = '<div class="container"><p id="paragraph">Hello</p></div>'
html2 = '<div><p>Hello</div></p>'
print(validate_html_tags_with_attr(html1)) 
print(validate_html_tags_with_attr(html2))  