# -*- coding: utf-8 -*-

import re
import codecs
import requests
import inspect
import bklv2


def mkreadme():
    f = codecs.open( "head.txt", "r", "utf-8" )
    text = f.read()
    f.close()

    text += make_functionlist()

    fout = codecs.open( "README.md", "w", "utf-8" )
    fout.write( text )
    fout.close()


def make_functionlist():
    mbrs = inspect.getmembers( bklv2.api, inspect.isfunction )
    text = "\r\n## API methods\r\n| method | description |\r\n|:------:|:------------|\r\n"
    for m in mbrs:
        if m[0][0]!="_":
            print( m[0] )
            comment = inspect.getdoc( m[1] )
            url = re.search( "http[s]*://[/.\-\w]+", comment ).group()
            response = requests.get( url )
            hit = re.search( "<div class=\"entry__content\">\s*<p>([ /.\-\w\"\']+)</p>", response.text )
            text += "| [" + m[0] + "](" + url + ") | " + hit.group(1) + "|\r\n"
    return text

if __name__ == "__main__":
    mkreadme()
