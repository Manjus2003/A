def HtmlTags(html):
    stack = []
    i = 0
    while i < len(html):
        if html[i] == '<':
            j = i + 1
            while j < len(html) and html[j] != '>':# to find the closing tag
                j += 1
            tag = html[i+1:j]                      # to get the tag name
            if not tag.startswith('/'):            # if it's an opening tag
                stack.append(tag)                  # push to stack    
            else: 
                if not stack or stack[-1] != tag[1:]:# if stack is empty or top of stack doesn't match closing tag
                    return False
                stack.pop()                        # pop from stack
            i = j
        i += 1
    return len(stack)==0                           # if stack is empty return true else false

html1="<html><body><h1>Title</h1></body></html>"
html2="<html><body><h1>Title</body></html>" 
print(HtmlTags(html1)) 
print(HtmlTags(html2))
                    