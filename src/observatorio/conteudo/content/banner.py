# -*- coding: utf-8 -*-

from plone.app.blob.field import ImageField

from archetypes.referencebrowserwidget.widget import ReferenceBrowserWidget

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.content.link import ATLink, ATLinkSchema

from observatorio.conteudo import MessageFactory as _
from observatorio.conteudo.config import PROJECTNAME
from observatorio.conteudo.interfaces import IBanner

BannerSchema = ATLinkSchema.copy() + atapi.Schema((

    atapi.ReferenceField(
        name='link_interno',
        widget=ReferenceBrowserWidget(
            label=_(u'Link Interno'),
            description=_(u'Caso selecionado o link sera apontado para o local de sua escolha.'),
            allow_search=True,
            allow_browse=True,
        ),
        #allowed_types=('Folder',),
        relationship='link_interno',
        multiValued=False,
    ),

    ImageField(
        name='imagem',
        widget=atapi.ImageWidget(
            label=_(u'Imagem do Banner'),
            description=_(u'Escolha da imagem do banner.'),
        ),
        required=False,
    ),

    atapi.BooleanField(
        name='linkTarget',
        default=False,
        widget=atapi.BooleanWidget(
            label=_(u'Abrir link em nova janela'),
            description=_(u'Caso selecionado o link sera exibido em uma nova janela'),
        ),
        required=False,
    ),
))

schemata.finalizeATCTSchema(BannerSchema)

BannerSchema['remoteUrl'].required = False
BannerSchema['remoteUrl'].default = ''
BannerSchema['remoteUrl'].widget.label = _(u'Link Externo')
BannerSchema['remoteUrl'].widget.description = _(u'Sera utilizado quando nao houver link interno.')


class Banner(ATLink):
    """
    """

    implements(IBanner)

    meta_type = "Banner"
    schema = BannerSchema

    _at_rename_after_creation = True

    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        return self.getField('imagem').tag(self, **kwargs)

    def get_target(self):
        if self.linkTarget:
            return '_blank'
        else:
            return ''

    def get_link(self):
        """Retorna o interno caso nao haja retorna o externo
        """
        field = self.getField('link_interno')

        if field.get(self) is not None:
            return field.get(self).absolute_url()

        if self.remoteUrl.startswith('http'):
            return self.remoteUrl
        elif self.remoteUrl is None or self.remoteUrl == '':
            return ''
        else:
            return 'http://' + self.remoteUrl

atapi.registerType(Banner, PROJECTNAME)
