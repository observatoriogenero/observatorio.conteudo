# -*- coding: utf-8 -*-

from Acquisition import aq_inner
from Acquisition import aq_parent

from plone.app.blob.field import ImageField, BlobField

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.base import ATCTFileContent, ATContentTypeSchema

from observatorio.conteudo import MessageFactory as _
from observatorio.conteudo.config import PROJECTNAME
from observatorio.conteudo.interfaces import IPublicacao

PublicacaoSchema = ATContentTypeSchema.copy() + atapi.Schema((

    BlobField('arquivo',
        widget=atapi.FileWidget(
            label=_(u"Arquivo"),
            description=_(u"Arquivo da publicação."),
        ),
        required=True,
    ),

    ImageField('imagem',
        widget=atapi.ImageWidget(
            label=_(u"Imagem Capa"),
            description=_(u"Imagem da capa da publicação."),
        ),
        required=False,
    ),

))

schemata.finalizeATCTSchema(PublicacaoSchema)


class Publicacao(ATCTFileContent):
    """
    """

    implements(IPublicacao)

    meta_type = "Publicacao"
    schema = PublicacaoSchema

    _at_rename_after_creation = True

atapi.registerType(Publicacao, PROJECTNAME)
