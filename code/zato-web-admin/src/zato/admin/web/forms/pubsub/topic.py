# -*- coding: utf-8 -*-

"""
Copyright (C) 2018, Zato Source s.r.o. https://zato.io

Licensed under LGPLv3, see LICENSE.txt for terms and conditions.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

# Django
from django import forms

# Zato
from zato.common import PUBSUB
from zato.admin.web.forms import add_pubsub_services

class CreateForm(forms.Form):
    id = forms.CharField(widget=forms.HiddenInput())
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'required', 'style':'width:100%'}))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'checked':'checked'}))
    has_gd = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    is_api_sub_allowed = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    hook_service_id = forms.ChoiceField(widget=forms.Select())

    max_depth_gd = forms.CharField(widget=forms.TextInput(
        attrs={'class':'required', 'style':'width:20%'}), initial=PUBSUB.DEFAULT.TOPIC_MAX_DEPTH_GD)
    max_depth_non_gd = forms.CharField(widget=forms.TextInput(
        attrs={'class':'required', 'style':'width:20%'}), initial=PUBSUB.DEFAULT.TOPIC_MAX_DEPTH_NON_GD)

    depth_check_freq = forms.CharField(widget=forms.TextInput(
        attrs={'class':'required', 'style':'width:15%'}), initial=PUBSUB.DEFAULT.DEPTH_CHECK_FREQ)

    pub_buffer_size_gd = forms.CharField(widget=forms.TextInput(
        attrs={'class':'required', 'style':'width:20%'}), initial=PUBSUB.DEFAULT.PUB_BUFFER_SIZE_GD)

    # This is not used for now
    pub_buffer_size_non_gd = forms.CharField(widget=forms.HiddenInput(
        attrs={'class':'required', 'style':'width:20%'}), initial=PUBSUB.DEFAULT.PUB_BUFFER_SIZE_NON_GD)

    deliv_task_sync_interv_gd = forms.CharField(widget=forms.TextInput(
        attrs={'class':'required', 'style':'width:20%'}), initial=PUBSUB.DEFAULT.DELIV_TASK_SYNC_INTERVAL_GD)

    deliv_task_sync_interv_non_gd = forms.CharField(widget=forms.TextInput(
        attrs={'class':'required', 'style':'width:20%'}), initial=PUBSUB.DEFAULT.DELIV_TASK_SYNC_INTERVAL_NON_GD)

    def __init__(self, req, *args, **kwargs):
        super(CreateForm, self).__init__(*args, **kwargs)
        add_pubsub_services(self, req, by_id=True)

class EditForm(CreateForm):
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput())
