# coding: utf-8
# Author: Max Mildh

from os import listdir,chdir,pardir,remove
from bottle import route, run, template, request, error,redirect


 
@route("/")
def list_articles():
    """
    This is the home page, which shows a list of links to all articles
    in the wiki.
    """
    wiki = listdir("wiki")
    return template("index", wiki = wiki)
    
@route('/wiki/<pagename>/')
def show_article(pagename):
    """Displays a single article (loaded from a text file)."""
    filename = pagename + ".txt"
    fo = open("wiki/" + filename)
    article = fo.read()
    fo.close
    return template("wiki", head = pagename,  content = article)
    
@route('/edit/')
def edit_form():
    """
    Shows a form which allows the user to input a title and content
    for an article. This form should be sent via POST to /update/.
    """
    return template ("edit")
 
@route('/update/', method="POST")
def do_upload():
    chdir("wiki")
    subject = request.forms.subject
    data = request.forms.data
    fo = open(subject + ".txt", "wb")
    fo.write(data);
    fo.close()
    chdir(pardir)
    redirect("/wiki/" + subject + "/")

    

@error(404)
def error404(error):
    return 'Nothing here, sorry'
    
    
@route("/delete/", method="POST")
def delete():
    try:
        deletes = request.forms.dele
        remove("wiki/" + deletes + ".txt")
        return template("del_right", title = deletes)
    except:
        return template("del_wrong", title = deletes)
        
@route("/edit_ex/<pagename>")
def change(pagename):
    filename = pagename + ".txt"
    fo = open("wiki/" + filename)
    article = fo.read()
    fo.close
    return template ("edit_ex", content = article, head = pagename)
    
    
 
 
run(host='localhost', port=8080, debug=True, reloader=True)