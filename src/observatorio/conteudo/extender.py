# -*- coding: utf-8 -*-

from Products.Archetypes.public import BooleanField, LinesField
from Products.Archetypes.public import InAndOutWidget

from Products.ATContentTypes.interfaces import IATLink, IATFile

from zope.component import adapts
from zope.interface import implements

from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender, IBrowserLayerAwareExtender

from observatorio.conteudo.interfaces import IObservatorioConteudoLayer
from observatorio.conteudo.interfaces import IPublicacao


class ContentTypeExtenderLinesField(ExtensionField, LinesField):
    """ Um campo de linhas simples """


class ContentTypeExtenderBooleanField(ExtensionField, BooleanField):
    """ Um campo booleano simples """


fields = [
    ContentTypeExtenderLinesField(
        name="eixo",
        index="KeywordIndex",
        widget=InAndOutWidget(
            label="Eixo de Atuação",
        ),
        schemata="categorization",
        enforceVocabulary=True,
        multiValued=True,
        vocabulary_factory='observatorio.conteudo.eixos_atuacao',
    ),

    ContentTypeExtenderLinesField(
        name="area",
        index="KeywordIndex",
        widget=InAndOutWidget(
            label="Área Temática",
        ),
        schemata="categorization",
        enforceVocabulary=True,
        multiValued=True,
        vocabulary_factory='observatorio.conteudo.areas_tematicas',
    ),
]


class PublicacaoExtender(object):
    """
    """

    adapts(IPublicacao)
    implements(ISchemaExtender, IBrowserLayerAwareExtender)

    layer = IObservatorioConteudoLayer

    fields = fields

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields


class FileExtender(object):
    """
    """

    adapts(IATFile)
    implements(ISchemaExtender)

    fields = fields

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields


class LinkExtender(object):
    """
    """

    adapts(IATLink)
    implements(ISchemaExtender, IBrowserLayerAwareExtender)

    layer = IObservatorioConteudoLayer

    fields = fields

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
