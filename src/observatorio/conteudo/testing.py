# -*- coding: utf-8 -*-
"""Base module for unittesting."""

from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer


class Fixture(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import observatorio.conteudo
        self.loadZCML(package=observatorio.conteudo)

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'observatorio.conteudo:default')

FIXTURE = Fixture()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,),
    name="observatorio.conteudo:Integration",
)
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,),
    name="observatorio.conteudo:Functional",
)
