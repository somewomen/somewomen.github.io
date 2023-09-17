"""Route declaration."""
from flask import current_app as app
from flask import render_template
import yaml
import os

current_directory = os.path.abspath(os.path.dirname(__file__))

# nav = [
#     {"name": "Home", 'page' : 'home'},
#     {"name": "Short CV", 'page':'cv'},
#     {"name": "Publications", 'page':'pubs'},
#     {"name": "Recipes", 'page':'recipes'},
#     ]
nav = {
    'index': {"name":"About",
             'desc':""},
    # 'laurel': {"name": "Laurels",
    #          'desc':'Laurels'},
    'team': {"name":"Team",
             'desc':""},
    'press': {"name": "Press",
             'desc':''},
    'blurb': {"name": "What People are Saying",
              'desc':''},
    'impact': {"name": "Resources & Impact",
             'desc':''},
    # 'presskit': {"name": "Press Kit",
    #          'desc':''},
    'contact': {"name": "Contact",
                'desc':''},
     'watch': {"name": "Watch",
             'desc':''}
}



# press = [
# ("At The Movies: Some Women is a moving, painfully honest look at a trans woman's life in S'pore",
#  "https://str.sg/wnme",
#   "John Lui",
#      "Straits Times",
#      "2022-03-23",
#  "", ""),
    
#     ("Some Women film hopes to show that being transgender is not 'sexual deviancy'",
#      "https://str.sg/wnmP",
#      "John Lui",
#      "Straits Times",
#      "2022-03-23",
#      """SINGAPORE - In the documentary Some Women, film-maker Quen Wong shows herself being physically close to husband Francis Bond. They hold hands, cuddle and kiss - just like any ordinary couple.

# In a film filled with conversation and visuals that deal with the turbulent journey Wong and others have taken as transgender women in Singapore, the quiet moments of intimacy are akin to hitting the pause button.""",
#      ""),
#     ("《一些女人》一刀不剪公映 跨性别者从他变她",
#      "https://www.zaobao.com.sg/entertainment/story20220322-1254754",
#      "李亦筠",
#      "Zaobao",
#      "2022-03-23",
#      "", ""),
#     ("This Singaporean Filmmaker’s Debut Feature Is a Love Letter to the Trans Community",
#      "https://www.tatlerasia.com/culture/arts/sgiff-2021-singaporean-filmmaker-quen-wong-some-women-trans-community",
#      "HASHIRIN NURIN HASHIMI",
#      "Tatler",
#      "2021-12-03",
#      "", ""),
# ]




@app.route("/<page>.html")
def show(page):
    """Show a page"""
    if page == 'press':
        yaml_file= os.path.join(current_directory, 'press.yaml')
        with open(yaml_file, "r") as stream:
            details = yaml.safe_load(stream)
    elif page == 'blurb':
        yaml_file= os.path.join(current_directory, 'blurb.yaml')
        with open(yaml_file, "r") as stream:
            details = yaml.safe_load(stream)  
    else:
         details = []
         
    return render_template(
        f"{page}.html",
        page=page,
        nav=nav,
        title=nav[page]['name'],
        description=nav[page]['desc'],
        details=details
    )

@app.route("/")
def home():
    """show the home page"""
    return show('index')

