import urllib
def read_text():
    quotes = open("I:\Sonali Git Hub\Python Intro\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    check_profanity(contents_of_file)
    quotes.close()

def check_profanity(text_to_check):
        connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
        output = connection.read()
        print(output)
        connection.close()
        if "true" in output:
            print("profanity Aler!!")
        elif "false" in output:
            print("This document has no curse words!")
        else:
            print("could not scan the document properly")
        
    
read_text()
