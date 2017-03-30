# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# coding: utf-8
# pylint: skip-file
from msrest.serialization import Model


class ShutdownNotificationContent(Model):
    """ShutdownNotificationContent.

    :param skip_url: The URL to skip auto-shutdown.
    :type skip_url: str
    :param delay_url60: The URL to delay shutdown by 60 minutes.
    :type delay_url60: str
    :param delay_url120: The URL to delay shutdown by 2 hours.
    :type delay_url120: str
    :param vm_name: The virtual machine to be shut down.
    :type vm_name: str
    :param guid: The GUID for the virtual machine to be shut down.
    :type guid: str
    :param owner: The owner of the virtual machine.
    :type owner: str
    :param event_type: The event for which a notification will be sent.
    :type event_type: str
    :param text: The text for the notification.
    :type text: str
    :param subscription_id: The subscription ID for the schedule.
    :type subscription_id: str
    :param resource_group_name: The resource group name for the schedule.
    :type resource_group_name: str
    :param lab_name: The lab for the schedule.
    :type lab_name: str
    """

    _attribute_map = {
        'skip_url': {'key': 'skipUrl', 'type': 'str'},
        'delay_url60': {'key': 'delayUrl60', 'type': 'str'},
        'delay_url120': {'key': 'delayUrl120', 'type': 'str'},
        'vm_name': {'key': 'vmName', 'type': 'str'},
        'guid': {'key': 'guid', 'type': 'str'},
        'owner': {'key': 'owner', 'type': 'str'},
        'event_type': {'key': 'eventType', 'type': 'str'},
        'text': {'key': 'text', 'type': 'str'},
        'subscription_id': {'key': 'subscriptionId', 'type': 'str'},
        'resource_group_name': {'key': 'resourceGroupName', 'type': 'str'},
        'lab_name': {'key': 'labName', 'type': 'str'},
    }

    def __init__(self, skip_url=None, delay_url60=None, delay_url120=None, vm_name=None, guid=None, owner=None, event_type=None, text=None, subscription_id=None, resource_group_name=None, lab_name=None):
        self.skip_url = skip_url
        self.delay_url60 = delay_url60
        self.delay_url120 = delay_url120
        self.vm_name = vm_name
        self.guid = guid
        self.owner = owner
        self.event_type = event_type
        self.text = text
        self.subscription_id = subscription_id
        self.resource_group_name = resource_group_name
        self.lab_name = lab_name