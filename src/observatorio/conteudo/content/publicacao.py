# -*- coding: utf-8 -*-

from plone.app.blob.field import ImageField, BlobField

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.base import ATCTFileContent, ATContentTypeSchema

from observatorio.conteudo import MessageFactory as _
from observatorio.conteudo.config import PROJECTNAME
from observatorio.conteudo.interfaces import IPublicacao

PublicacaoSchema = ATContentTypeSchema.copy() + atapi.Schema((

    BlobField(
        name='arquivo',
        widget=atapi.FileWidget(
            label=_(u'Arquivo'),
            description=_(u'Arquivo da publicacao.'),
        ),
        required=True,
        primary=True,
    ),

    ImageField(
        name='image',
        widget=atapi.ImageWidget(
            label=_(u'Imagem Capa'),
            description=_(u'Imagem da capa da publicacao.'),
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

    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        return self.getField('imagem').tag(self, **kwargs)

atapi.registerType(Publicacao, PROJECTNAME)
