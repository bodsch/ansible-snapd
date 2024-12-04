#!/usr/bin/python3
# -*- coding: utf-8 -*-

# (c) 2024, Bodo Schulz <bodo@boone-schulz.de>

from __future__ import (absolute_import, print_function)
__metaclass__ = type

from ansible.utils.display import Display

display = Display()


class FilterModule(object):
    """
    """

    def filters(self):
        return {
            'snap_mounts': self.snap_mounts,
        }

    def snap_mounts(self, data):
        """
        """
        display.vv(f"snap_mounts({data})")

        # extract mount points
        mount_points = [x.get('mount') for x in data for k, v in x.items() if k == 'mount']

        # snap mount_points
        snap_mount_points = [i for i in mount_points if i.startswith('/var/snap')]

        display.vv(f"= {snap_mount_points}")

        return snap_mount_points
