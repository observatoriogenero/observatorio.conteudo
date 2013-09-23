# -*- coding: utf-8 -*-

import unicodedata

from five import grok

from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from Products.CMFCore.utils import getToolByName

from observatorio.conteudo.interfaces import IConteudoSettings


class AreasTematicas(object):
    """ vocabulario que retorna as areas tematicas
    """
    grok.implements(IVocabularyFactory)

    def __call__(self, context):

        registry = getUtility(IRegistry)
        settings = registry.forInterface(IConteudoSettings)
        areas = settings.area_tematica

        if areas is not None:
            termos = [SimpleTerm(unicodedata.normalize('NFKD', area).encode('ascii', 'ignore').lower(), unicodedata.normalize('NFKD', area).encode('ascii', 'ignore').lower(), area) for area in areas]
        else:
            termos = []
        return SimpleVocabulary(termos)

grok.global_utility(AreasTematicas, name=u"observatorio.conteudo.areas_tematicas")


class EixoAtuacao(object):
    """ vocabulario que retorna os eixos de atuacao
    """
    grok.implements(IVocabularyFactory)

    def __call__(self, context):

        registry = getUtility(IRegistry)
        settings = registry.forInterface(IConteudoSettings)
        eixos = settings.eixo_atuacao

        if eixos is not None:
            termos = [SimpleTerm(unicodedata.normalize('NFKD', eixo).encode('ascii', 'ignore').lower(), unicodedata.normalize('NFKD', eixo).encode('ascii', 'ignore').lower(), eixo) for eixo in eixos]
        else:
            termos = []
        return SimpleVocabulary(termos)

grok.global_utility(EixoAtuacao, name=u"observatorio.conteudo.eixos_atuacao")


class PathBiblioteca(object):
    """ vocabulario que retorna o path dos conteudos da biblioteca
    """
    grok.implements(IVocabularyFactory)

    def __call__(self, context):

        portal = getToolByName(context, 'portal_url').getPortalObject()
        biblioteca = getattr(portal, 'biblioteca', None)

        if biblioteca:
            termos = [SimpleTerm('/'.join(obj.getPhysicalPath()), obj.Title()) for obj in biblioteca.objectValues() if obj.portal_type == 'Folder']
        else:
            termos = []
        return SimpleVocabulary(termos)

grok.global_utility(PathBiblioteca, name=u"observatorio.conteudo.path_biblioteca")
