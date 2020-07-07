def color_code(x,siz):
  g = int(1280*x/siz)
  if 0 <= g and g < 256:
    lef = "ff"
    md = hex(g)[2:4]
    rig = "00"
  elif 256 <= g and g < 512:
    g -= 256
    lef = hex(int("ff",16) - g)[2:4]
    md = "ff"
    rig = "00"
  elif 512 <= g and g < 768:
    g -= 512
    lef = "00"
    md = "ff"
    rig = hex(g)[2:4]    
  elif 768 <= g and g < 1024:
    g -= 768
    lef = "00"
    md = hex(int("ff",16) - g)[2:4]
    rig = "ff"    
  elif 1024 <= g and g < 1280:
    g -= 1024
    lef = hex(g)[2:4]
    md = "00"
    rig = "ff"
  if len(lef) == 1:lef = "0"+lef
  if len(md) == 1:md = "0"+md
  if len(rig) == 1:rig = "0"+rig
  
  return "#"+lef+md+rig

if __name__ == "__main__":
    x = 10
    for i in range(x):
        print(color_code(i,x))