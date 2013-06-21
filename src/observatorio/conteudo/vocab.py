# -*- coding: utf-8 -*-

import collections
import unicodedata

from five import grok

from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.component import getUtility
from plone.registry.interfaces import IRegistry


@grok.provider(IContextSourceBinder)
def validar_termo(context):
    """ funcao para validar se existe algum termo repetido
    """

    registry = getUtility(IRegistry)
    import pdb;pdb.set_trace()

#    terms = [ SimpleTerm(value=unicodedata.normalize('NFKD', pair).encode('ascii', 'ignore').lower(), token=unicodedata.normalize('NFKD', pair).encode('ascii', 'ignore').lower(), title=pair) for pair in items ]

    return True