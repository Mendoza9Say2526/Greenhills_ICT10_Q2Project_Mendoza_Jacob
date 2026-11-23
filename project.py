# Nickname Atlas Python
from pyscript import display, document

# function for revealing the nickname
def reveal_nickname(e):
    nickname = document.getElementById("country").value
    document.getElementById("div1").innerHTML = ""

    display(nickname, target="div1") #displaying the country's nickname

def skills_test(e):
    document.location.href = "skillstest2q.html"

def pa_2(e):
    document.location.href = "pa2.html"

def drill_2(e):
    document.location.href = "drill2.html"

def creator_page(e):
    document.location.href = "creator.html"

def home_page(e):
    document.location.href = "index.html"