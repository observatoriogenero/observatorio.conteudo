# -*- coding: utf-8 -*-

from Products.Archetypes.public import BooleanField, StringField, LinesField
from Products.Archetypes.public import BooleanWidget, StringWidget, InAndOutWidget

from Products.ATContentTypes.interface import IATContentType, IATFolder

from zope.component import adapts
from zope.interface import implements

from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender

from zope.interface import Interface


class IContentTypeExtender(Interface):
    """
    """


class ContentTypeExtenderLinesField(ExtensionField, LinesField):
    """ Um campo de linhas simples """


class ContentTypeExtenderBooleanField(ExtensionField, BooleanField):
    """ Um campo booleano simples """


class ContentTypeExtender(object):
    """
    """

    adapts(IATContentType)
    implements(ISchemaExtender)

    fields = [
        ContentTypeExtenderBooleanField(
            name="destaque",
            widget=BooleanWidget(
                label="Destaque",
                description="Selecione caso queira que o conteúdo seja um destaque",
            ),
        ),

        ContentTypeExtenderLinesField(
            name="eixo",
            index="KeywordIndex:brains",
            widget=InAndOutWidget(
                label="Eixo de Atuação",
            ),
            enforceVocabulary=True,
            multiValued=True,
            vocabulary_factory='observatorio.conteudo.eixos_atuacao',
        ),

        ContentTypeExtenderLinesField(
            name="area",
            index="KeywordIndex:brains",
            widget=InAndOutWidget(
                label="Área Temática",
            ),
            enforceVocabulary=True,
            multiValued=True,
            vocabulary_factory='observatorio.conteudo.areas_tematicas',
        ),
        ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields