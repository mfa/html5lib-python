from __future__ import absolute_import, division, unicode_literals

from html5lib import treewalkers

from .htmlserializer import HTMLSerializer


def serialize(input, tree="simpletree", format="html", encoding=None,
              **serializer_opts):
    # XXX: Should we cache this?
    walker = treewalkers.getTreeWalker(tree)
    if format == "html":
        s = HTMLSerializer(**serializer_opts)
    else:
        raise ValueError("type must be html")
    return s.render(walker(input), encoding)
