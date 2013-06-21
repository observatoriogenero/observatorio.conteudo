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


class FolderExtenderStringField(ExtensionField, StringField):
    """ Um campo string simples """


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
            widget=InAndOutWidget(
                label="Eixo de Atuação",
            )
        ),

        ContentTypeExtenderLinesField(
            name="area",
            widget=InAndOutWidget(
                label="Área Temática",
            )
        ),
        ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields


class FolderExtender(object):
    """
    """

    adapts(IATFolder)
    implements(ISchemaExtender)

    fields = [

        ContentTypeExtenderBooleanField(
            name="destaque",
            widget=BooleanWidget(
                label="Destaque",
                description="Selecione caso queira que o conteúdo seja um destaque",
            ),
        ),

        FolderExtenderStringField(
            name="os",
            widget=StringWidget(
                label="OS",
                description="Informe o número da OS",
            ),
        ),
        ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields
