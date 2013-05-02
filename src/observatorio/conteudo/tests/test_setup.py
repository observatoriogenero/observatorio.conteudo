# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from observatorio.conteudo.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of observatorio.conteudo into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if observatorio.conteudo is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('observatorio.conteudo'))

    def test_uninstall(self):
        """Test if observatorio.conteudo is cleanly uninstalled."""
        self.installer.uninstallProducts(['observatorio.conteudo'])
        self.assertFalse(self.installer.isProductInstalled('observatorio.conteudo'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IObservatorioConteudoLayer is registered."""
        from observatorio.conteudo.interfaces import IObservatorioConteudoLayer
        from plone.browserlayer import utils
        self.failUnless(IObservatorioConteudoLayer in utils.registered_layers())
