# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

import unittest2 as unittest

from Products.CMFCore.utils import getToolByName

from observatorio.conteudo.config import PROJECTNAME
from observatorio.conteudo.testing import INTEGRATION_TESTING
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID


class TestInstall(unittest.TestCase):
    """Test installation of observatorio.conteudo into Plone."""

    layer = INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.app = self.layer['app']
        self.portal = self.layer['portal']
        self.qi = getToolByName(self.portal, 'portal_quickinstaller')

    def test_installed(self):
        self.assertTrue(self.qi.isProductInstalled(PROJECTNAME))

    # browserlayer.xml
#    def test_browserlayer(self):
#        """Test that IObservatorioConteudoLayer is registered."""
#        from observatorio.conteudo.interfaces import IObservatorioConteudoLayer
#        from plone.browserlayer import utils
#        self.failUnless(IObservatorioConteudoLayer in utils.registered_layers())


class UninstallTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.qi = self.portal['portal_quickinstaller']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.qi.uninstallProducts(products=[PROJECTNAME])

    def test_uninstalled(self):
        self.assertFalse(self.qi.isProductInstalled(PROJECTNAME))
