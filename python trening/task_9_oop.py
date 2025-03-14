from re import search


class Button:


    def __init__(self, text, link):
        self.text = text
        self.link = link


home = Button("домой", "/home")
catalog_msk = Button('каталог', '/msk/catalog')



print(home.text)
print('кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('/in')

print(catalog_msk)
print(' кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)



class ButtonTwo:


    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc


    def click(self):
        return "клик по локатору - {}". format(self.loc)


home_two = ButtonTwo('домой','/home','button#home')


print(home_two.click())



class Input:
    def __init__(self, loc):
        self.loc = loc
search = Input("input#search")


print(search.loc)
