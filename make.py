# -*- coding: utf-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import json
import requests
import tes
import codecs


result = tes.rank("人気記事")

print("frag1")

code = {
  "type": "carousel",
  "contents": [
      {
      "type": "bubble",
      "header": {
          "type": "box",
          "layout": "horizontal",
          "contents": [
              {
                "type": "text",
                "text": "GIGAZINE ranking",
                "weight": "bold",
                "color": "#000000",
                "size": "xl"
              }
          ]
      },
      "hero": {
          "type": "image",
          "url": result[0][2],
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "uri": result[0][1]
          }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "spacing": "sm",
            "contents": [
                {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                    {
                    "type": "text",
                    "text": result[0][0],
                    "wrap": True,
                    "color": "#666666",
                    "weight": "bold",
                    "size": "sm",
                    "flex": 5
                    }
                  ]
                }
              ]
            }
          ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                "type": "button",
                "style": "secondary",
                "action": {
                    "type": "uri",
                    "label": "MORE",
                    "uri": result[0][1]
                }
              },
        {
        "type": "spacer",
        "size": "sm"
        }
      ],
      "flex": 0
    }
  },
  {
"type": "bubble",
"header": {
  "type": "box",
  "layout": "horizontal",
  "contents": [
    {
      "type": "text",
      "text": "GIGAZINE ranking",
      "weight": "bold",
      "color": "#000000",
      "size": "xl"
    }
  ]
},
 "hero": {
  "type": "image",
  "url": result[1][2],
  "size": "full",
  "aspectRatio": "20:13",
  "aspectMode": "cover",
  "action": {
    "type": "uri",
    "uri": result[1][1]
  }
},

"body": {
  "type": "box",
  "layout": "vertical",
  "contents": [
    {
      "type": "box",
      "layout": "vertical",
      "margin": "lg",
      "spacing": "sm",
      "contents": [
        {
          "type": "box",
          "layout": "baseline",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": result[1][0],
              "wrap": True,
              "color": "#666666",
              "weight": "bold",
              "size": "sm",
              "flex": 5
            }
          ]
        }
      ]
    }
  ]
},
"footer": {
  "type": "box",
  "layout": "vertical",
  "spacing": "sm",
  "contents": [
    {
              "type": "button",
              "style": "secondary",
              "action": {
                  "type": "uri",
                  "label": "MORE",
                  "uri": result[1][1]
              }
          },
    {
      "type": "spacer",
      "size": "sm"
    }
  ],
  "flex": 0
}
},
{
"type": "bubble",
"header": {
  "type": "box",
  "layout": "horizontal",
  "contents": [
    {
      "type": "text",
      "text": "GIGAZINE ranking",
      "weight": "bold",
      "color": "#000000",
      "size": "xl"
    }
  ]
},
 "hero": {
  "type": "image",
  "url": result[2][2],
  "size": "full",
  "aspectRatio": "20:13",
  "aspectMode": "cover",
  "action": {
    "type": "uri",
    "uri": result[2][1]
  }
},

"body": {
  "type": "box",
  "layout": "vertical",
  "contents": [
    {
      "type": "box",
      "layout": "vertical",
      "margin": "lg",
      "spacing": "sm",
      "contents": [
        {
          "type": "box",
          "layout": "baseline",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": result[2][0],
              "wrap": True,
              "color": "#666666",
              "weight": "bold",
              "size": "sm",
              "flex": 5
            }
          ]
        }
      ]
    }
  ]
},
"footer": {
  "type": "box",
  "layout": "vertical",
  "spacing": "sm",
  "contents": [
    {
              "type": "button",
              "style": "secondary",
              "action": {
                  "type": "uri",
                  "label": "MORE",
                  "uri": result[2][1]
              }
          },
    {
      "type": "spacer",
      "size": "sm"
    }
  ],
  "flex": 0
}
},
{
"type": "bubble",
"header": {
  "type": "box",
  "layout": "horizontal",
  "contents": [
    {
      "type": "text",
      "text": "GIGAZINE ranking",
      "weight": "bold",
      "color": "#000000",
      "size": "xl"
    }
  ]
},
 "hero": {
  "type": "image",
  "url": result[3][2],
  "size": "full",
  "aspectRatio": "20:13",
  "aspectMode": "cover",
  "action": {
    "type": "uri",
    "uri": result[3][1]
  }
},

"body": {
  "type": "box",
  "layout": "vertical",
  "contents": [
    {
      "type": "box",
      "layout": "vertical",
      "margin": "lg",
      "spacing": "sm",
      "contents": [
        {
          "type": "box",
          "layout": "baseline",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": result[3][0],
              "wrap": True,
              "color": "#666666",
              "weight": "bold",
              "size": "sm",
              "flex": 5
            }
          ]
        }
      ]
    }
  ]
},
"footer": {
  "type": "box",
  "layout": "vertical",
  "spacing": "sm",
  "contents": [
    {
              "type": "button",
              "style": "secondary",
              "action": {
                  "type": "uri",
                  "label": "MORE",
                  "uri": result[3][1]
              }
          },
    {
      "type": "spacer",
      "size": "sm"
    }
  ],
  "flex": 0
}
},
{
"type": "bubble",
"header": {
  "type": "box",
  "layout": "horizontal",
  "contents": [
    {
      "type": "text",
      "text": "GIGAZINE ranking",
      "weight": "bold",
      "color": "#000000",
      "size": "xl"
    }
  ]
},
 "hero": {
  "type": "image",
  "url": result[4][2],
  "size": "full",
  "aspectRatio": "20:13",
  "aspectMode": "cover",
  "action": {
    "type": "uri",
    "uri": result[4][1]
  }
},

"body": {
  "type": "box",
  "layout": "vertical",
  "contents": [
    {
      "type": "box",
      "layout": "vertical",
      "margin": "lg",
      "spacing": "sm",
      "contents": [
        {
          "type": "box",
          "layout": "baseline",
          "spacing": "sm",
          "contents": [
            {
              "type": "text",
              "text": result[4][0],
              "wrap": True,
              "color": "#666666",
              "weight": "bold",
              "size": "sm",
              "flex": 5
            }
          ]
        }
      ]
    }
  ]
},
"footer": {
  "type": "box",
  "layout": "vertical",
  "spacing": "sm",
  "contents": [
      {
      "type": "button",
      "style": "secondary",
      "action": {
        "type": "uri",
        "label": "MORE",
        "uri": result[4][1]
        }
      },
      {
      "type": "spacer",
      "size": "sm"
      }
    ],
    "flex": 0
    }
  },
  {
      "type": "bubble",
      "header": {
          "type": "box",
          "layout": "horizontal",
          "contents": [
              {
                "type": "text",
                "text": "GIGAZINE ranking",
                "weight": "bold",
                "color": "#000000",
                "size": "xl"
              }
          ]
      },
      "hero": {
          "type": "image",
          "url": result[5][2],
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "uri": result[5][1]
          }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "spacing": "sm",
            "contents": [
                {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                    {
                    "type": "text",
                    "text": result[5][0],
                    "wrap": True,
                    "color": "#666666",
                    "weight": "bold",
                    "size": "sm",
                    "flex": 5
                    }
                  ]
                }
              ]
            }
          ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                "type": "button",
                "style": "secondary",
                "action": {
                    "type": "uri",
                    "label": "MORE",
                    "uri": result[5][1]
                }
              },
        {
        "type": "spacer",
        "size": "sm"
        }
      ],
      "flex": 0
    }
  },
  {
      "type": "bubble",
      "header": {
          "type": "box",
          "layout": "horizontal",
          "contents": [
              {
                "type": "text",
                "text": "GIGAZINE ranking",
                "weight": "bold",
                "color": "#000000",
                "size": "xl"
              }
          ]
      },
      "hero": {
          "type": "image",
          "url": result[6][2],
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "uri": result[6][1]
          }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "spacing": "sm",
            "contents": [
                {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                    {
                    "type": "text",
                    "text": result[6][0],
                    "wrap": True,
                    "color": "#666666",
                    "weight": "bold",
                    "size": "sm",
                    "flex": 5
                    }
                  ]
                }
              ]
            }
          ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                "type": "button",
                "style": "secondary",
                "action": {
                    "type": "uri",
                    "label": "MORE",
                    "uri": result[6][1]
                }
              },
        {
        "type": "spacer",
        "size": "sm"
        }
      ],
      "flex": 0
    }
  },
  {
      "type": "bubble",
      "header": {
          "type": "box",
          "layout": "horizontal",
          "contents": [
              {
                "type": "text",
                "text": "GIGAZINE ranking",
                "weight": "bold",
                "color": "#000000",
                "size": "xl"
              }
          ]
      },
      "hero": {
          "type": "image",
          "url": result[7][2],
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "uri": result[7][1]
          }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "spacing": "sm",
            "contents": [
                {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                    {
                    "type": "text",
                    "text": result[7][0],
                    "wrap": True,
                    "color": "#666666",
                    "weight": "bold",
                    "size": "sm",
                    "flex": 5
                    }
                  ]
                }
              ]
            }
          ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                "type": "button",
                "style": "secondary",
                "action": {
                    "type": "uri",
                    "label": "MORE",
                    "uri": result[7][1]
                }
              },
        {
        "type": "spacer",
        "size": "sm"
        }
      ],
      "flex": 0
    }
  },
  {
      "type": "bubble",
      "header": {
          "type": "box",
          "layout": "horizontal",
          "contents": [
              {
                "type": "text",
                "text": "GIGAZINE ranking",
                "weight": "bold",
                "color": "#000000",
                "size": "xl"
              }
          ]
      },
      "hero": {
          "type": "image",
          "url": result[8][2],
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "uri": result[8][1]
          }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "spacing": "sm",
            "contents": [
                {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                    {
                    "type": "text",
                    "text": result[8][0],
                    "wrap": True,
                    "color": "#666666",
                    "weight": "bold",
                    "size": "sm",
                    "flex": 5
                    }
                  ]
                }
              ]
            }
          ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                "type": "button",
                "style": "secondary",
                "action": {
                    "type": "uri",
                    "label": "MORE",
                    "uri": result[8][1]
                }
              },
        {
        "type": "spacer",
        "size": "sm"
        }
      ],
      "flex": 0
    }
  },
  {
      "type": "bubble",
      "header": {
          "type": "box",
          "layout": "horizontal",
          "contents": [
              {
                "type": "text",
                "text": "GIGAZINE ranking",
                "weight": "bold",
                "color": "#000000",
                "size": "xl"
              }
          ]
      },
      "hero": {
          "type": "image",
          "url": result[9][2],
          "size": "full",
          "aspectRatio": "20:13",
          "aspectMode": "cover",
          "action": {
            "type": "uri",
            "uri": result[9][1]
          }
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
            "type": "box",
            "layout": "vertical",
            "margin": "lg",
            "spacing": "sm",
            "contents": [
                {
                "type": "box",
                "layout": "baseline",
                "spacing": "sm",
                "contents": [
                    {
                    "type": "text",
                    "text": result[9][0],
                    "wrap": True,
                    "color": "#666666",
                    "weight": "bold",
                    "size": "sm",
                    "flex": 5
                    }
                  ]
                }
              ]
            }
          ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                "type": "button",
                "style": "secondary",
                "action": {
                    "type": "uri",
                    "label": "MORE",
                    "uri": result[9][1]
                }
              },
        {
        "type": "spacer",
        "size": "sm"
        }
      ],
      "flex": 0
    }
  }

# contents
  ]
}

print("frag2")
# f = open("temp.json",'w')
# f = open("templates/temp.json",'w')
f = codecs.open('templates/temp.json', 'w','utf-8')

# json_data=json.load(f)
json.dump(code,f, ensure_ascii=False,indent=4)
# f.write(str(code))
f.close()