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
            elif('Note' in line):
                textType = 'Note'
                
        if(lineNum == 3): # this line contains the highlighted text, or the note
            text = line[:-1] # don't need the newline at the end            
        
        lineNum += 1 # increment our lineNum variable                 
        
        if '==========' in line: # if we reach the end of a highlight/note
            lineNum = 0 # reset lineNum
                
            if(textType == 'Highlight'): # if it's a higlight, warp with quotation marks, append two newline characters
                s = 'Quote: ' + '\"' + text + '\"' + '\n'
                if(prevTextType == 'Highlight'): # add another 2 newlines if the previous entry was a quote/highlight
                    s = '\n\n' + s                
            else: # if it's a note, append three newlines
                s = 'Note: ' + text + '\n\n\n'
                
            curFile.write(s) # then insert the text into the appropriate file     
            curFile.close()
            
            