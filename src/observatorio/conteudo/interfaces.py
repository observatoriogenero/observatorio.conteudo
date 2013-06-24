# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.theme.interfaces import IDefaultPloneLayer

from zope.interface import Interface

from zope import schema


class IObservatorioConteudoLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class IPublicacao(Interface):
    """
    """


class IConteudoSettings(Interface):
    """ Interface para o painel de controle do produto
    """

    area_tematica = schema.List(title=u"Área temática",
                                value_type=schema.TextLine(),
                                unique=True,
                                missing_value=None,
                                required=False)

    eixo_atuacao = schema.List(title=u"Eixo de Atuação",
                               value_type=schema.TextLine(),
                               unique=True,
                               missing_value=None,
                               required=False,)
