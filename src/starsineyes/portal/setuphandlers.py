# -*- coding: utf-8 -*-

from Products.CMFPlone.interfaces import INonInstallable
from plone import api
from zope.interface import implementer

TO_DELETE = [
    "Members",
    "events",
    "front-page",
    "news",
]


@implementer(INonInstallable)
class HiddenProfiles(object):
    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return ["starsineyes.portal:uninstall"]


def post_install(context):
    """Post install script"""

    portal = api.portal.get()
    for content_id in TO_DELETE:
        content = getattr(portal, content_id, None)
        if content:
            api.content.delete(content)


def uninstall(context):
    """Uninstall script"""
