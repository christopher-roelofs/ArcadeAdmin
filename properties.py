global db_name
global secret_key
global gamelist_xml
global samlple_gamelist


with open('properties.txt') as property_file:
    for property in property_file:
        name = property.split('=')[0].strip()
        value = property.split('=')[1].strip()

        if name == 'db_name':
            db_name = value
        if name == 'secret_key':
            secret_key = value
        if name == 'gamelist_xml':
            gamelist_xml = value
        if name == 'samlple_gamelist':
            samlple_gamelist = value
    print db_name
    print secret_key
    print gamelist_xml
    print samlple_gamelist