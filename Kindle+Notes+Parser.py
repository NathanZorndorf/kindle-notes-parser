
# coding: utf-8

# In[2]:

import os.path


# In[ ]:

import 


# In[19]:

clipping = open('Kindle Clippings 11:16.txt', 'r')


# In[11]:

new_notes = open('Kindle Paperwhite Notes.txt', 'w')


# In[20]:

for line in clipping:
    print(line)


# In[23]:

clipping.close()


# In[7]:

import re
import os.path
import tkinter as tk
from tkinter import filedialog

#root = tk.Tk()
#root.withdraw()
#clippings_file_path = filedialog.askopenfilename()

#titleFormat = input('Enter the general name you would like to save your files as.\n' 
#                    'Use "Title" and "Author" to place the title and author within your document name.\n'
#                    'For example, "Notes on Title by Author" would result in "Notes on Moby Dick by Herman Melville".\n')

prevTextType = 'Highlight' # initialize history variable
textType = 'Highlight'

with open('My Clippings.txt') as clipping:
    
    lineNum = 0
    
    for line in clipping:
        if(lineNum == 0):  # this line contains the title and author
            line = line.replace(':', ',') # use commas instead of ':' in boot titles
            line = line.replace(';', ' ') # don't include semi colons in titles 
            bookTitle = line.split('(')[0]
            bookTitle = bookTitle[:-1] # delete the space at the end of the book title
            bookAuthor = line.split('(')[1]
            bookAuthor = bookAuthor[:-2] # Don't need the closing parantheses, or the new line character

            #hardcoded title
            fileName = 'Notes on {title} by {author}.txt'.format(title=bookTitle, author=bookAuthor)
            
            #fileName = titleFormat.replace('Title', bookTitle)
            #fileName = fileName.replace('Author', bookAuthor) 
            #fileName = fileName + '.txt'
            
            # using reg expressions 
            #l = {'NORTH':'N','SOUTH':'S','EAST':'E','WEST':'W'}
            #pattern = '|'.join(sorted(re.escape(k) for k in l))
            #address = "123 north anywhere street"
            #re.sub(pattern, lambda m: l.get(m.group(0).upper()), address, flags=re.IGNORECASE)

            
            if(os.path.isfile(fileName) == True): # file already exists
                curFile = open(fileName, 'a') # open file in append mode 
            else: # file does not exist already
                curFile = open(fileName, 'w') # create a new file in 'write' mode 
                curFile.write(fileName[:-4]) # write title in first line
                curFile.write('\n\n')
            
            
        if(lineNum == 1): # this line contains the information on whether this is a note or a highlight
            prevTextType = textType
            if 'Highlight' in line:
                textType = 'Highlight'
                location = line.split(' ')
                location = location[5]
                location = 'Location ' + str(location)
            elif('Note' in line):
                textType = 'Note'
                location = line.split(' ')
                location = location[5]
                location = 'Location ' + str(location)
                
                
        if(lineNum == 3): # this line contains the highlighted text, or the note
            text = line[:-1] # don't need the newline at the end   
            if(textType == 'Note'):
                note = text 
            elif(textType == 'Highlight'):
                quote = text
        
        lineNum += 1 # increment our lineNum variable                 
        
        if '==========' in line: # if we reach the end of a highlight/note
            lineNum = 0 # reset lineNum
                
            if(textType == 'Highlight'): # if it's a higlight, wrap with quotation marks, append two newline characters
                s = '\n\n\n' + 'Quote at ' + location + ': ' + '\"' + quote + '\"'
                curFile.write(s)
                    
            if(prevTextType == 'Note'): # if the previous text was a note, then add the note AFTER the quote
                s =  '\n' + 'Note at ' + location + ': ' + note  
                curFile.write(s)
                
                
            curFile.close() # close the current file, because the next item in 'My Clippings.txt' could be for a different book
            
            


# In[ ]:

testFile = open('Text Formatting Test.rtf', 'w')

quote = "To thine own self be true, and it must follow, as the night the day, thou canst not then be false to any man."
text = "That's what I'm sayin dawg!!"


