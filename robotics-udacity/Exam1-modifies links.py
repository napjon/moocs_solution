# Question 4: Remove Tags

# When we add our words to the index, we don't really want to include
# html tags such as <body>, <head>, <table>, <a href="..."> and so on.

# Write a procedure, remove_tags, that takes as input a string and returns
# a list of words, in order, with the tags removed. Tags are defined to be
# strings surrounded by < >. Words are separated by whitespace or tags.
# You may assume the input does not include any unclosed tags, that is,
# there will be no '<' without a following '>'.

def remove_tags1(s):
    end_bracket = s.find('>')
    if end_bracket == -1:
        return s.split()
    else:
        start_bracket = s.find('<',end_bracket)
        l = s[end_bracket+1:start_bracket].split()
        return  l + remove_tags(s[end_bracket+1:])

def remove_tags(string):
    start = string.find('<')
    while start != -1:
        end = string.find('>', start)
        string = string[:start] + " " +string[end+1:]
        start = string.find('<')
    return string.split()




print remove_tags('''<h1>Title</h1><p>This is a
                    <a href="http://www.udacity.com">link</a>.<p>''')
#>>> ['Title','This','is','a','link','.']

#print remove_tags('''<table cellpadding='3'>
 #                 <tr><td>Hello</td><td>World!</td></tr>
  #                 </table>''')
#>>> ['Hello','World!']

#print remove_tags("<hello><goodbye>")
#>>> []

#print remove_tags("This is plain text.")
#>>> ['This', 'is', 'plain', 'text.']

print remove_tags('This is in <i>italics</i>')