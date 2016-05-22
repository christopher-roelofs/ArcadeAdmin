import xml.etree.ElementTree as ET

class game_object(object):
    def __init__(self):
        self.id = ""
        self.source = ""
        self.path = ""
        self.name = ""
        self.desc = ""
        self.image = "./notreallythere.jpg"
        self.rating = "0"
        self.releasedate = "0000"
        self.developer = ""
        self.publisher = ""
        self.genre = ""
        self.players = 1
        self.playcount = ""
        self.lastplayed = ""
        self.favorite = False

def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def read(xmlFile):
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    game_list = []
    for child in root:

        game = game_object()
        game.id = child.get('id')
        game.source = child.get('source')
        for elem in child:
            if elem.tag == "path":
                game.path = elem.text
            if elem.tag == "name":
                game.name = elem.text.strip()
            if elem.tag == "desc":
                game.desc = elem.text
            if elem.tag == "image":
                game.image = elem.text
            if elem.tag == "rating":
                game.rating = elem.text
            if elem.tag == "releasedate":
                game.releasedate = elem.text
            if elem.tag == "developer":
                game.developer = elem.text
            if elem.tag == "publisher":
                game.publisher = elem.text
            if elem.tag == "genre":
                game.genre = elem.text
            if elem.tag == "players":
                game.players = elem.text
            if elem.tag == "playcount":
                game.playcount = elem.text
            if elem.tag == "lastplayed":
                game.lastplayed = elem.text
        game_list.append(game)
    return game_list

def write(list,xmlfile):
    root = ET.Element('gameList')
    for game in list:
        child = ET.SubElement(root,'game')
        child.set('id',game.id)
        child.set('source',game.source)
        path = ET.SubElement(child,'path')
        path.text = "./{}.zip".format(game.id)
        path = ET.SubElement(child,'name')
        path.text = game.name.strip()
        path = ET.SubElement(child,'desc')
        path.text = game.desc
        path = ET.SubElement(child,'image')
        path.text = './images/{}.jpg'.format(game.id)
        path = ET.SubElement(child,'rating')
        path.text = game.rating
        path = ET.SubElement(child,'releasedate')
        path.text = game.releasedate
        path = ET.SubElement(child,'developer')
        path.text = game.developer
        path = ET.SubElement(child,'publisher')
        path.text = game.publisher
        path = ET.SubElement(child,'genre')
        path.text = game.genre
        path = ET.SubElement(child,'players')
        path.text = game.players
        path = ET.SubElement(child,'playcount')
        path.text = game.playcount
        path = ET.SubElement(child,'lastplayed')
        path.text = game.lastplayed
    ET.tostring(ET.fromstring('<mytag/>'), method='html')
    indent(root)
    tree = ET.ElementTree(root)
    tree.write(xmlfile,encoding="UTF-8")

