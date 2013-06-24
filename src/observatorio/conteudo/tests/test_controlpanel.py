# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from zope.component import getMultiAdapter

from plone.registry import Registry

from observatorio.conteudo.interfaces import IConteudoSettings
from observatorio.conteudo.testing import INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.app.testing import logout


class TestControlPanel(unittest.TestCase):
    """Test installation of observatorio.conteudo into Plone."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi = getToolByName(self.portal, 'portal_quickinstaller')
        self.registry = Registry()
        self.registry.registerInterface(IConteudoSettings)

    def test_conteudo_controlpanel_view(self):
        # Test the conteudo setting control panel view
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                name="conteudo-settings")
        view = view.__of__(self.portal)
        self.failUnless(view())

    def test_conteudo_controlpanel_view_protected(self):
        # Test that the conteudo setting control panel view can not be accessed
        # by anonymous users
        from AccessControl import Unauthorized
        logout()
        self.assertRaises(Unauthorized,
            self.portal.restrictedTraverse,
            '@@conteudo-settings')

    def test_conteudo_in_controlpanel(self):
        # Check that there is an conteudo entry in the control panel
        self.controlpanel = getToolByName(self.portal, "portal_controlpanel")
        self.failUnless('conteudo' in [a.getAction(self)['id']
                                      for a in self.controlpanel.listActions()])

    def test_record_area_tematica(self):
        # Test that the area_tematica record is in the control panel
        settings = self.registry.forInterface(IConteudoSettings)
        record_area_tematica = settings.area_tematica
        self.failUnless('area_tematica' in IConteudoSettings)
        self.assertEquals(record_area_tematica, None)

    def test_record_eixo_atuacao(self):
        settings = self.registry.forInterface(IConteudoSettings)
        record_eixo_atuacao = settings.eixo_atuacao
        self.failUnless('eixo_atuacao' in IConteudoSettings)
        self.assertEquals(record_eixo_atuacao, None)
