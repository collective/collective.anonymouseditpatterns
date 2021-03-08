# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import collective.anonymouseditpatterns


class CollectiveAnonymouseditpatternsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=collective.anonymouseditpatterns)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.anonymouseditpatterns:default')


COLLECTIVE_ANONYMOUSEDITPATTERNS_FIXTURE = CollectiveAnonymouseditpatternsLayer()


COLLECTIVE_ANONYMOUSEDITPATTERNS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_ANONYMOUSEDITPATTERNS_FIXTURE,),
    name='CollectiveAnonymouseditpatternsLayer:IntegrationTesting',
)


COLLECTIVE_ANONYMOUSEDITPATTERNS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_ANONYMOUSEDITPATTERNS_FIXTURE,),
    name='CollectiveAnonymouseditpatternsLayer:FunctionalTesting',
)


COLLECTIVE_ANONYMOUSEDITPATTERNS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_ANONYMOUSEDITPATTERNS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='CollectiveAnonymouseditpatternsLayer:AcceptanceTesting',
)
