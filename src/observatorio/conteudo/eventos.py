# -*- coding: utf-8 -*-

from five import grok
from zope.lifecycleevent.interfaces import IObjectAddedEvent

#import subprocess
#import cStringIO
#
#import pyPdf
#from PIL import Image

from observatorio.conteudo.content import IPublicacao


@grok.subscribe(IPublicacao, IObjectAddedEvent)
def cria_capa_publicacao(object, event):
    """

    """
    #import pdb;pdb.set_trace()
