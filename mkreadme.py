# -*- coding: utf-8 -*-
import os
import re
import codecs
import urllib.parse
import requests, bs4
import inspect
import bklv2


def mkreadme():
    host = "https://developer.nulab-inc.com"
    path = "/docs/backlog/"

    f = codecs.open( "head.txt", "r", "utf-8" )
    text = f.read()
    f.close()

    text += make_functionlist( host, path )

    fout = codecs.open( "README.md", "w", "utf-8" )
    fout.write( text )
    fout.close()

def mkreadme_j():
    host = "https://developer.nulab-inc.com"
    path = "/ja/docs/backlog/"

    f = codecs.open( "head.txt", "r", "utf-8" )
    text = f.read()
    f.close()

    text += make_functionlist( host, path )

    fout = codecs.open( "README.ja.md", "w", "utf-8" )
    fout.write( text )
    fout.close()


def replace_upper( match ):
    return match.group(1).upper()

def make_function_name_from_url( url ):
    parsed = urllib.parse.urlsplit( url )
    s = parsed.path.split( "/" )
    res = re.sub( "-([a-z])", replace_upper, s[-1] )
    return res

def make_functionlist( host, path ):
    res = requests.get( urllib.parse.urljoin( host, path ) )
    res.encoding = res.apparent_encoding
    soup = bs4.BeautifulSoup( res.text, "html.parser" )
    el = soup.find("optgroup", label="Backlog API")
    fncurllist = []
    if el is not None:
        ops = el.find_all("option")
        if ops is not None:
            for op in ops:
                fncurllist.append( urllib.parse.urljoin( host, op["value"] ))

    mbrs = inspect.getmembers( bklv2.api, inspect.isfunction )
    text = "\r\n## API methods\r\n| method | description |\r\n|:------:|:------------|\r\n"
    ok = 0
    ng = 0
    not_implementation= 0
    for url in fncurllist:
        fn = make_function_name_from_url( url )
        hit = False
        for m in mbrs:
            if m[0] == fn:
                hit = True
                break
        if hit==False:
            print("not implementation:{}".format(fn))
            text += "| [{}]({}) | **{}** |\r\n".format( fn, url, "not implementation." )
            not_implementation +=1
        else:
            res = requests.get( url )
            res.encoding = res.apparent_encoding
            if res.status_code == 200:
                soup = bs4.BeautifulSoup( res.text, "html.parser" )
                els = soup.find("main").find_all("p")
                context = ""
                for el in els:
                    context += el.text.replace( "\n", "" )
                print( "{}: {}".format(fn,context) )
                text += "| [{}]({}) | {} |\r\n".format( fn, url, context )
                ok += 1
            else:
                print( m[0] )
                print( "{} : {}".format(res.status_code, url) )
                text += "| [{}]({}) | **{}** |\r\n".format( fn, url, res.status_code )
                ng += 1

    print( "implementation={}({}), not_implementation={}".format( ok+ng, ng, not_implementation ) )
    return text


if __name__ == "__main__":
    os.chdir( os.path.dirname(__file__) )
    mkreadme()
    mkreadme_j()
