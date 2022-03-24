###
### ('title', 'author', 'publisher', 'url', 'blurb', 'image')
###
###

from yaml import load, dump
import toml


press = [
("At The Movies: Some Women is a moving, painfully honest look at a trans woman's life in S'pore",
 "https://str.sg/wnme",
  "John Lui",
     "Straits Times",
     "2022-03-23",
 "", ""),
    
    ("Some Women film hopes to show that being transgender is not 'sexual deviancy'",
     "https://str.sg/wnmP",
     "John Lui",
     "Straits Times",
     "2022-03-23",
     """SINGAPORE - In the documentary Some Women, film-maker Quen Wong shows herself being physically close to husband Francis Bond. They hold hands, cuddle and kiss - just like any ordinary couple.

In a film filled with conversation and visuals that deal with the turbulent journey Wong and others have taken as transgender women in Singapore, the quiet moments of intimacy are akin to hitting the pause button.""",
     ""),
    ("《一些女人》一刀不剪公映 跨性别者从他变她",
     "https://www.zaobao.com.sg/entertainment/story20220322-1254754",
     "李亦筠",
     "Zaobao",
     "2022-03-23",
     "", ""),
    ("This Singaporean Filmmaker’s Debut Feature Is a Love Letter to the Trans Community",
     "https://www.tatlerasia.com/culture/arts/sgiff-2021-singaporean-filmmaker-quen-wong-some-women-trans-community",
     "HASHIRIN NURIN HASHIMI",
     "Tatler",
     "2021-12-03",
     "", ""),
]

press = [
    {'title':"At The Movies: Some Women is a moving, painfully honest look at a trans woman's life in S'pore",
 'url':"https://str.sg/wnme",
  'author':"John Lui",
  'source':"Straits Times",
  'date':"2022-03-23",
     'blurb':"",
     'img': "",
     'status': 1,
}
    ]


press_toml=toml.dumps(press)

print(press_toml)
    
