class InterfaceHelper(object):
    @staticmethod
    def convert_name(port):
        """Convert port name

        :param port: port resource full address (PerfectSwitch/Chassis 0/FastEthernet0-23)
        :return: port name (FastEthernet0/23)
        :rtype: string
        """

        if not port:
            err_msg = 'Failed to get port name.'
            raise Exception('get_port_name', err_msg)

        temp_port_name = port.split('/')[-1]
        if 'port-channel' not in temp_port_name.lower():
            temp_port_name = temp_port_name.replace('-', '/')
        return temp_port_name
