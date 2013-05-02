# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from plone.theme.interfaces import IDefaultPloneLayer

from zope.interface import Interface


class IObservatorioConteudoLayer(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer."""


class IPublicacao(Interface):
    """
    """
