# -*- coding: utf-8 -*-

import logging
from five import grok
from Products.Archetypes.interfaces import IObjectInitializedEvent, IObjectEditedEvent
import subprocess

from observatorio.conteudo.content import IPublicacao

logger = logging.getLogger('observatorio.conteudo')


def _cria_capa_publicacao(object):
    """
    """
    pdf = str(object.getArquivo())
    gs_cmd = [ "gs",
               "-q",
               "-sDEVICE=png16m",
               "-dGraphicsAlphaBits=4",
               "-dSAFER",
               "-dBATCH",
               "-dNOPAUSE",
               "-dFirstPage=1",
               "-dLastPage=1",
               "-sOutputFile=%stdout",
               "-",
               ]
    png = None
    gs_process = subprocess.Popen(gs_cmd,stdout=subprocess.PIPE,stdin=subprocess.PIPE,)
    gs_process.stdin.write(pdf)
    png = gs_process.communicate()[0]
    gs_process.stdin.close()
    return_code = gs_process.returncode
    if return_code == 0:
        logger.info("Ghostscript processou uma pagina do arquivo pdf.")
    else:
        logger.warn("O processo Ghostscript nao terminou corretamente! Error Code: %d" % (return_code))
        png = None
    if png:
        object.setImage(png)


@grok.subscribe(IPublicacao, IObjectInitializedEvent)
def cria_capa_publicaca_inclusao(object, event):
    _cria_capa_publicacao(object)


@grok.subscribe(IPublicacao, IObjectEditedEvent)
def cria_capa_publicacao_edicao(object, event):
    _cria_capa_publicacao(object)
