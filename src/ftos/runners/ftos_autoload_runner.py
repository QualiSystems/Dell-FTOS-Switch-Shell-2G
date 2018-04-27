#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.devices.runners.autoload_runner import AutoloadRunner
from ftos.flows.ftos_autoload_flow import FTOSSnmpAutoloadFlow


class FTOSAutoloadRunner(AutoloadRunner):
    def __init__(self, logger, resource_config, snmp_handler):
        super(FTOSAutoloadRunner, self).__init__(resource_config)
        self._logger = logger
        self.snmp_handler = snmp_handler

    @property
    def autoload_flow(self):
        return FTOSSnmpAutoloadFlow(self.snmp_handler, self._logger)
