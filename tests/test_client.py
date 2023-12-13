"""
Test the Client class
"""

import pytest  # noqa: F401, F403

import paho.mqtt.client as mqtt  # type: ignore
import bambulabs_api as bl  # noqa: F401, F403


class TestAPI:
    """
    TestAPI Class for testing the Client
    """

    def test_init(self):
        """
        test_init Test the __init__ method of the Client class
        """
        client = bl.Client('', '', '')
        assert client.ip_address == ''
        assert client.access_code == ''
        assert client.serial == ''
        assert isinstance(client.client, mqtt.Client)
