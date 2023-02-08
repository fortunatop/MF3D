from __future__ import absolute_import, print_function, unicode_literals

from _Framework.Capabilities import CONTROLLER_ID_KEY, PORTS_KEY, NOTES_CC, SCRIPT, SYNC, REMOTE, controller_id, inport, outport

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=2580, product_ids=[8], model_name=[u'Midi Fighter 3D']),
     PORTS_KEY: [inport(props=[NOTES_CC, SCRIPT]), outport(props=[NOTES_CC, SYNC, SCRIPT])]}

def create_instance(c_instance):
    from .midi_fighter_3D import Midi_Fighter_3D
    return Midi_Fighter_3D(c_instance=c_instance)