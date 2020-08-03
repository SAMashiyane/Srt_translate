
#!/usr/bin/python
# -*- coding: UTF-8 -*- 
# To Make This subtile translate , you need to install googletrans Python Module
# Link Download ===> https://pypi.org/project/googletrans/
# In this program dest--->LANGUAGES (example this scrip dest="de" means translate 'de': 'german')
# Unfortunately, this program does not support Persian and Arabic languages, but this problem will be solved in the next version

face = '''
                        :::Srt_Translate :::
                         
 
        +=======================================+
        |..........Srt_Translate................|
        +---------------------------------------+
        |          Coded by SAM355              |
        |                                       |
        |    Email:  salio.blue@gmail.com       |
        |    mohtarami.seyedali@gmail.com       |                 
        |  We take no responsibilities for the  |
        |  use of this program                  |
        +---------------------------------------+
 
                                                 
                   
   
        '''
from googletrans import Translator
import arabic_reshaper
try:
    # Fix UTF8 output issues on Windows console.
    # Does nothing if package is not installed
    from win_unicode_console import enable
    enable()
except ImportError:
    pass

translator = Translator()
with open('sub.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
sentences = content
translations = (translator.translate(sentences, dest="de"))
for translation in translations:
    tx=arabic_reshaper.reshape(translation.text)
    f = open("output.txt", "a")
    print(f"{tx}",file=f)
    f.close()
