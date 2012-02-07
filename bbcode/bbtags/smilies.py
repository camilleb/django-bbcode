import urllib2
import re
from bbcode import *
from bbcode import settings


class Smilies(SelfClosingTagNode):
    open_pattern = re.compile(':(?P<name>[a-zA-Z-]+):')

    def parse(self):
        name = self.match.groupdict()['name']
        url = '%s%s.gif' % (settings.SMILEY_MEDIA_URL, name)
        if smilie_exists(url):
            return '<img src="%s" alt="%s" />' % (url, name)
        return ':%s:' % name


def smilie_exists(url):
    try:
        urllib2.urlopen(urllib2.Request(url))
        return True
    except:
        return False


class AlternativeSmilie(SelfClosingTagNode):
    def __init__(self, *args, **kwargs):
        if not hasattr(self, 'alias'):
            self.alias = self.__class__.__name__.lower()
        SelfClosingTagNode.__init__(self, *args, **kwargs)

    def parse(self):
        alias = self.match.group()
        url = '%s%s.gif' % (settings.SMILEY_MEDIA_URL, self.alias)
        if smilie_exists(url):
            return '<img src="%s" alt="%s" />' % (url, alias)
        return '%s' % alias


class LOL(AlternativeSmilie):
    # :D, :-D, :-d, :d
    open_pattern = re.compile(':-?(D|d)')


class  Smilie(AlternativeSmilie):
    # :), :-)
    open_pattern = re.compile(':-?\)')


class Wink(AlternativeSmilie):
    # ;), ;-), ;-D, ;D, ;d, ;-d
    open_pattern = re.compile(';-?(\)|d|D)')


class Razz(AlternativeSmilie):
    # :P, :-P, :p, :-p
    open_pattern = re.compile(':-?(P|p)')


class Eek(AlternativeSmilie):
    # o_O....
    open_pattern = re.compile('(o|O|0)_(o|O|0)')


class Sad(AlternativeSmilie):
    # :-(, :(
    open_pattern = re.compile(':-?\(')


class Crying(AlternativeSmilie):
    # ;_;, :'(, :'-(
    open_pattern = re.compile("(;_;|:'-?\()")


class Yell(AlternativeSmilie):
    # ^.^
    open_pattern = re.compile('^\.^')


class Grin(AlternativeSmilie):
    # xD, XD, *g*
    open_pattern = re.compile('(xD|XD|\*g\*)')


class Neutral(AlternativeSmilie):
    # :-|, :|
    open_pattern = re.compile('(:-?\|)')


register(Smilies)
register(LOL)
register(Smilie)
register(Wink)
register(Razz)
register(Eek)
register(Sad)
register(Crying)
register(Yell)
register(Grin)
register(Neutral)
