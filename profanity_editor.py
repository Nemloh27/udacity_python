import urllib

def read_text():
    quotes = open("C:\Nemloh27\Udacity-Python\movie_quotes.txt")
    contents = quotes.read()
    quotes.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Profanity Alert!!!")
    else:
        print("No profanities found")

read_text()
