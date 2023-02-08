"""""
By Andrés Fortunato Mankoch
February 2023,
Edited from a script for Midi Fighter 64 by padi04 available at
https://github.com/padi04/MF64-Ableton-Script

"""""
from __future__ import with_statement
import Live
from _Framework.ControlSurface import ControlSurface
from _Framework.DeviceComponent import DeviceComponent
from _Framework.MixerComponent import MixerComponent # Class encompassing several channel strips to form a mixer
from _Framework.SliderElement import SliderElement
from _Framework.TransportComponent import TransportComponent
from _Framework.InputControlElement import *
from _Framework.ButtonElement import ButtonElement
from _Framework.ButtonMatrixElement import ButtonMatrixElement
from _Framework.SessionComponent import SessionComponent
from _Framework.EncoderElement import *
from Launchpad.ConfigurableButtonElement import ConfigurableButtonElement
from pushbase import colors
from _APC.SkinDefault import make_rgb_skin, make_default_skin

#updated by @offchristianamr, huge thank you to padi04 for originally writing the script and to jademalo for fixing a bug!
class Midi_Fighter_3D(ControlSurface):

    def __init__(self, c_instance):
        super(Midi_Fighter_3D, self).__init__(c_instance)
        self._color_skin = make_rgb_skin()
        self._default_skin = make_default_skin()
        with self.component_guard():
            global _map_modes
            _map_modes = Live.MidiMap.MapMode
            self.current_track_offset = 0
            self.current_scene_offset = 0
            # mixer
            global mixer
            num_tracks = 128
            num_returns = 24
            self.mixer = MixerComponent(num_tracks, num_returns)
            global active_mode
            #self._mode0()
            active_mode = "_mode1"
            self._set_active_mode()
            self._set_track_select_led()
            self.show_message("Midi fighter 3D")


    def _mode1(self):
        self.show_message("Script Loaded")
        # mixer
        global mixer
        # session
        global _session
        num_tracks = 4
        num_scenes = 4
# 		self._session = SessionComponent(auto_name=True, is_enabled=False, enable_skinning=True)
        self._session = SessionComponent(num_tracks, num_scenes)

        LIVE_COLORS_TO_MF3D = {10927616:49, #Lima
                                16149507:25, #orange
                                4047616:61, #green
                                6441901:85, #blue
                                14402304:37, #yellow
                                8754719:60, #dark lime
                                16725558:13, # red
                                3947580:24, #dark red
                                10056267:36, #café
                                8237133:67, #dark green
                                12026454:31, # dark orange
                                12565097:43, # dark yello2
                                13381230:115, #dark pink
                                12243060:49, #light lime
                                16249980:37, #yellow
                                13013643:111, #pink
                                10208397:61, #green
                                695438:73, #cian
                                13821080:49, #lime
                                3101346:90, #Blue
                                16749734:109, #pink
                                8962746:75, #cian
                                5538020:87, #Blue
                                13684944:120, #white
                                15064289:120, #white
                                14183652:99, #purple
                                11442405:85, #blue
                                13408551:31, #cafe
                                1090798:80, #dark cian
                                11096369:35, #dark orage
                                16753961:91, #dark blue
                                1769263:61, #green
                                5480241:72, #dark green
                                1698303:73, #cian
                                16773172:37, #yellow
                                7491393:36, #dark orange
                                8940772:105, #dark purple
                                14837594:17, #red
                                8912743:50, #lime
                                10060650:36, #dark orange
                                13872497:30, #orange
                                16753524:30,  #orange
                                8092539:127, # white
                                2319236:84, #dark cian
                                1716118:95, #Dark blue
                                12349846:110, #pink
                                11481907:121, #dark red
                                15029152:110, #pink
                                73:25, #cian
                                11119017:127, #white(gray)
                                10701741:105, #dark purple
                                15597486:49, #light lime
                                49071:43, #dark yellow
                                10851765:91, #dark blue
                                12558270:98, #purple
                                32192:57, #dark lime
                                8758722:80, #dark cian
                                10204100:75, #cian
                                11958214:98, #purple
                                8623052:85, #blue
                                16726484:110, #pink
                                12581632:48, #lime
                                13958625:84, #dark cyan
                                12173795:85, #light blue
                                13482980:97, #light purple
                                16777215:119, #white
                                6094824:78, #cian
                                13496824:73, #light cian
                                9611263:86, #blue
                                9160191:87} #blue

        RGB_COLOR_TABLE_MF3D = ((0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
                   (5, 0), (6, 0), (7, 0), (8, 0), (9, 0),
                   (10, 0), (11, 0), (12, 0), (13, 14837594),
                   (14, 14837594), (15, 14837594), (16, 14837594), (17, 14837594), (18, 14837594),
                   (19, 3947580), (20, 3947580), (21, 3947580), (22, 3947580), (23, 3947580),
                   (24, 3947580), (25, 16149507), (26, 16149507), (27, 16149507), (28, 16149507),
                   (29, 16149507), (30, 16149507), (31, 12026454), (32, 12026454), (33, 12026454),
                   (34, 12026454), (35, 12026454), (36, 12026454), (37, 14402304), (38, 14402304),
                   (39,14402304), (40, 14402304), (41, 14402304), (42, 14402304), (43, 12565097),
                   (44, 12565097), (45, 12565097), (46, 12565097), (47, 12565097), (48, 12565097), (49, 10927616),
                   (50, 10927616), (51, 10927616), (52, 10927616), (53, 10927616), (54, 10927616),
                   (55, 15597486), (56, 15597486), (57, 15597486), (58, 15597486),
                   (59, 15597486), (60, 15597486), (61, 4047616), (62, 4047616),
                   (63, 4047616), (64, 4047616), (65, 4047616), (66, 4047616), (67, 8237133),
                   (68, 8237133), (69, 8237133), (70, 8237133), (71, 8237133), (72, 8237133),
                   (73, 6094824), (74, 6094824), (75, 6094824), (76, 6094824),
                   (77, 6094824), (78, 6094824), (79, 13958625), (80, 13958625), (81, 13958625),
                   (82, 13958625), (83, 13958625), (84, 13958625), (85, 9611263),
                   (86, 9611263), (87, 9611263), (88, 9611263), (89, 9611263), (90, 9611263),
                   (91, 1716118), (92, 1716118), (93, 1716118), (94, 1716118), (95, 1716118),
                   (96, 1716118), (97, 11958214), (98, 11958214), (99, 11958214),
                   (100, 11958214), (101, 11958214), (102, 11958214), (103, 10701741),
                   (104, 10701741), (105, 10701741), (106, 10701741), (107, 10701741),
                   (108, 10701741), (109, 16726484), (110, 16726484), (111, 16726484),
                   (112, 16726484), (113, 16726484), (114, 16726484), (115, 13381230),
                   (116, 13381230), (117, 13381230), (118, 13381230), (119, 13381230),
                   (120, 13381230), (121, 16777215), (122, 16777215), (123, 16777215),
                   (124, 16777215), (125, 16777215), (126, 16777215), (127, 16777215))

        clip_color_table = LIVE_COLORS_TO_MF3D
        #clip_color_table = colors.LIVE_COLORS_TO_MIDI_VALUES.copy()
        #clip_color_table[16777215] = 119
        self._session.set_rgb_mode(LIVE_COLORS_TO_MF3D, RGB_COLOR_TABLE_MF3D)
        #self._session.set_rgb_mode(colors.LIVE_COLORS_TO_MIDI_VALUES, colors.RGB_COLOR_TABLE)
        track_offset = self.current_track_offset
        scene_offset = self.current_scene_offset
        self._session.set_offsets(track_offset, scene_offset)
        self._session._reassign_scenes()
        self.set_highlighting_session_component(self._session)
        # clip launch buttons
        session_buttons = [48, 49, 50, 51, 44, 45, 46, 47, 40, 41, 42, 43, 36, 37, 38, 39]
        sch = 2
        session_channels = [sch, sch, sch, sch, sch, sch, sch, sch,sch, sch, sch, sch, sch, sch, sch, sch]
        #change all the session channels to 2 in order to use the first bank. This will potentially allow for blinking/flashing animations in the future.
        session_types = [MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE]
        session_is_momentary = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self._pads = [ButtonElement(session_is_momentary[index], session_types[index], session_channels[index], session_buttons[index]) for index in range(num_tracks*num_scenes)]
        self._grid = ButtonMatrixElement(rows=[self._pads[(index*num_tracks):(index*num_tracks)+num_tracks] for index in range(num_scenes)])
        self._session.set_clip_launch_buttons(self._grid)
        # LED feedback
        self._session._enable_skinning()
        for scene_index in range(num_scenes):
            scene = self._session.scene(scene_index)
            for track_index in range(num_tracks):
                clip_slot = scene.clip_slot(track_index)
                clip_slot.set_triggered_to_play_value(72) #dark green
                clip_slot.set_triggered_to_record_value(97) #red
                clip_slot.set_record_button_value(24) #orange
                clip_slot.set_stopped_value(37) #yellow
                clip_slot.set_started_value(61) #dark red
                clip_slot.set_recording_value(13) #red
        # these are written in decimal format, correspond to the RGB_COLOR_TABLE in pushbase/colors.py
        
        # session navigation
        NAV_CHANNEL = 3
        # side buttons, not currently used
        up_button = ButtonElement(True, MIDI_NOTE_TYPE, NAV_CHANNEL, 25)
        down_button = ButtonElement(True, MIDI_NOTE_TYPE, NAV_CHANNEL, 23)
        left_button = ButtonElement(True, MIDI_NOTE_TYPE, NAV_CHANNEL, 21)
        right_button = ButtonElement(True, MIDI_NOTE_TYPE, NAV_CHANNEL, 24)

        up_button2 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 73)
        up_button2.set_on_off_values(109, 109)
        down_button2 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 69)
        down_button2.set_on_off_values(109, 109)
        left_button2 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 68)
        left_button2.set_on_off_values(109, 109)
        right_button2 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 70)
        right_button2.set_on_off_values(109, 109)
        
        #self._session.set_scroll_up_button(up_button2)
        self._session.set_page_up_button(up_button2)
        self._session.set_page_down_button(down_button2)
        self._session.set_page_left_button(left_button2)
        self._session.set_page_right_button(right_button2)
        self.current_track_offset = self._session._track_offset
        self.current_scene_offset = self._session._scene_offset
        self._session.set_mixer(self.mixer)
        #self._session._unlink()
        #self._session = None
        #self.clip_xtra.send_value(0)
        #self.clip_xtra.remove_value_listener(self._activate_mode4)
        #self.clip_xtra = None
        #if((hasattr(self, 'clip_xtra_back')) and (self.clip_xtra_back is not None)):
        #    self.clip_xtra_back.send_value(85)

        # mixer
        # the set_on_off_values were originally completely different, fixed by Jademalo
        global mixer
        arm_specific_0 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 52)
        arm_specific_0.set_on_off_values(13, 0)
        self.mixer.channel_strip(0).set_arm_button(arm_specific_0)
        arm_specific_1 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 53)
        arm_specific_1.set_on_off_values(13, 0)
        self.mixer.channel_strip(1).set_arm_button(arm_specific_1)
        arm_specific_2 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 54)
        arm_specific_2.set_on_off_values(13, 0)
        self.mixer.channel_strip(2).set_arm_button(arm_specific_2)
        arm_specific_3 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 55)
        arm_specific_3.set_on_off_values(13, 0)
        self.mixer.channel_strip(3).set_arm_button(arm_specific_3)

        solo_specific_0 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 56)
        solo_specific_0.set_on_off_values(85, 0)
        self.mixer.channel_strip(0).set_solo_button(solo_specific_0)
        solo_specific_1 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 57)
        solo_specific_1.set_on_off_values(85, 0)
        self.mixer.channel_strip(1).set_solo_button(solo_specific_1)
        solo_specific_2 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 58)
        solo_specific_2.set_on_off_values(85, 0)
        self.mixer.channel_strip(2).set_solo_button(solo_specific_2)
        solo_specific_3 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 59)
        solo_specific_3.set_on_off_values(85, 0)
        self.mixer.channel_strip(3).set_solo_button(solo_specific_3)

        mute_specific_0 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 60)
        mute_specific_0.set_on_off_values(37, 0)
        self.mixer.channel_strip(0).set_mute_button(mute_specific_0)
        self.mixer.channel_strip(0).set_invert_mute_feedback(True)
        mute_specific_1 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 61)
        mute_specific_1.set_on_off_values(37, 0)
        self.mixer.channel_strip(1).set_mute_button(mute_specific_1)
        self.mixer.channel_strip(1).set_invert_mute_feedback(True)
        mute_specific_2 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 62)
        mute_specific_2.set_on_off_values(37, 0)
        self.mixer.channel_strip(2).set_mute_button(mute_specific_2)
        self.mixer.channel_strip(2).set_invert_mute_feedback(True)
        mute_specific_3 = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 63)
        mute_specific_3.set_on_off_values(37, 0)
        self.mixer.channel_strip(3).set_mute_button(mute_specific_3)
        self.mixer.channel_strip(3).set_invert_mute_feedback(True)

        # session track stop
        stop_track_buttons = [64, 65, 66, 67]
        stop_track_channels = [sch, sch, sch, sch]
        stop_track_types = [MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE]
        stop_track_is_momentary = [1, 1, 1, 1]
        self._track_stop_buttons = [ConfigurableButtonElement(stop_track_is_momentary[index], stop_track_types[index], stop_track_channels[index], stop_track_buttons[index]) for index in range(num_tracks)]
        self._session.set_stop_track_clip_buttons(tuple(self._track_stop_buttons))
        # LED feedback
        self._session._enable_skinning()
        self._session.set_stop_clip_triggered_value(97)
        self._session.set_stop_clip_value(103)
        for scene_index in range(num_scenes):
            scene = self._session.scene(scene_index)
            for track_index in range(num_tracks):
                clip_slot = scene.clip_slot(track_index)


        # session scene launch
        scene_buttons = [83, 79, 75, 71]
        #the last buttons in every row, mentioned earlier
        scene_channels = [sch, sch, sch, sch]
        scene_types = [MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE, MIDI_NOTE_TYPE]
        scene_momentarys = [1, 1, 1, 1]
        self._scene_launch_buttons = [ButtonElement(scene_momentarys[index], scene_types[index], scene_channels[index], scene_buttons[index]) for index in range(num_scenes)]
        self._scene_launch_buttons = ButtonMatrixElement(rows=[self._scene_launch_buttons])
        self._session.set_scene_launch_buttons(self._scene_launch_buttons)
        # LED feedback
        self._session._enable_skinning()
        for scene_index in range(num_scenes):
            scene = self._session.scene(scene_index)
            scene.set_scene_value(37)
            scene.set_no_scene_value(0)
            scene.set_triggered_value(61)
            for track_index in range(num_tracks):
                clip_slot = scene.clip_slot(track_index)
                clip_slot.set_triggered_to_play_value(61)
                clip_slot.set_triggered_to_record_value(13)
                clip_slot.set_record_button_value(19)
                clip_slot.set_stopped_value(37)
                clip_slot.set_started_value(61)
                clip_slot.set_recording_value(13)
        self._session._link()
        self.refresh_state()
        if((hasattr(self, 'scene_shift')) and (self.scene_shift is not None)):
            self.scene_shift.send_value(127)
        #def _remove_mode2(self):


        # transport
        global transport
        self.transport = TransportComponent()
        self.transport.name = 'Transport'

        metronome_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 72)
        metronome_button.set_on_off_values(97, 103)
        metronome_button.name = 'metronome_button'
        self.transport.set_metronome_button(metronome_button)

        loop_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 81)
        loop_button.set_on_off_values(73, 79)
        loop_button.name = 'loop_button'
        self.transport.set_loop_button(loop_button)

        seek_forward_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 82)
        seek_forward_button.set_on_off_values(85, 91)
        seek_forward_button.name = 'seek_forward_button'
        self.transport.set_seek_forward_button(seek_forward_button)

        seek_backward_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 80)
        seek_backward_button.set_on_off_values(85, 91)
        seek_backward_button.name = 'seek_backward_button'
        self.transport.set_seek_backward_button(seek_backward_button)

        overdub_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 74)
        overdub_button.set_on_off_values(13, 19)
        overdub_button.name = 'overdub_button'
        self.transport.set_overdub_button(overdub_button)

        play_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 77)
        play_button.set_on_off_values(61, 67)
        play_button.name = 'play_button'
        self.transport.set_play_button(play_button)

        stop_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 76)
        stop_button.set_on_off_values(37, 43)
        stop_button.name = 'stop_button'
        self.transport.set_stop_button(stop_button)

        record_button = ConfigurableButtonElement(1, MIDI_NOTE_TYPE, sch, 78)
        record_button.set_on_off_values(13, 19)
        record_button.name = 'record_button'
        self.transport.set_record_button(record_button)


        if((hasattr(self, 'clip_xtra')) and (self.clip_xtra is not None)):
            self.clip_xtra.send_value(85)

        
    def _remove_mode1(self):
        # mixer
        global mixer
        # session
        global _session
        # clip launch buttons
        self._session.set_clip_launch_buttons(None)
        self.set_highlighting_session_component(None)


    def _set_track_select_led(self):
        self._turn_off_track_select_leds()
        # take sessionbox into account if its present
        offset = 0
        if (hasattr(self, '_session')):
            offset = self._session._track_offset
        num_of_tracks = len(self.song().tracks)
        # next is each track select item
        # select_1
        pos = offset + 0
        pos2 = pos + 1
        if num_of_tracks >= pos2:
            if(self.song().view.selected_track == self.song().tracks[pos]):
                if((hasattr(self, 'select_1')) and (self.select_1 is not None)):
                    self.select_1.send_value(73)
        # select_2
        pos = offset + 1
        pos2 = pos + 1
        if num_of_tracks >= pos2:
            if(self.song().view.selected_track == self.song().tracks[pos]):
                if((hasattr(self, 'select_2')) and (self.select_2 is not None)):
                    self.select_2.send_value(73)
        # select_3
        pos = offset + 2
        pos2 = pos + 1
        if num_of_tracks >= pos2:
            if(self.song().view.selected_track == self.song().tracks[pos]):
                if((hasattr(self, 'select_3')) and (self.select_3 is not None)):
                    self.select_3.send_value(73)
        # select_4
        pos = offset + 3
        pos2 = pos + 1
        if num_of_tracks >= pos2:
            if(self.song().view.selected_track == self.song().tracks[pos]):
                if((hasattr(self, 'select_4')) and (self.select_4 is not None)):
                    self.select_4.send_value(73)
        
        # select_5
        pos = offset + 4
        pos2 = pos + 1
        if num_of_tracks >= pos2:
            if(self.song().view.selected_track == self.song().tracks[pos]):
                if((hasattr(self, 'select_5')) and (self.select_5 is not None)):
                    self.select_5.send_value(73)
        # select_6
        pos = offset + 5
        pos2 = pos + 1
        if num_of_tracks >= pos2:
            if(self.song().view.selected_track == self.song().tracks[pos]):
                if((hasattr(self, 'select_6')) and (self.select_6 is not None)):
                    self.select_6.send_value(73)
        # select_7
        pos = offset + 6
        pos2 = pos + 1
        if num_of_tracks >= pos2:
            if(self.song().view.selected_track == self.song().tracks[pos]):
                if((hasattr(self, 'select_7')) and (self.select_7 is not None)):
                    self.select_7.send_value(73)
        # select_8
        pos = offset + 7
        pos2 = pos + 1
        if num_of_tracks >= pos2:
            if(self.song().view.selected_track == self.song().tracks[pos]):
                if((hasattr(self, 'select_8')) and (self.select_8 is not None)):
                    self.select_8.send_value(73)
        

    def _turn_off_track_select_leds(self):
        num_of_tracks = len(self.song().tracks)
        # take sessionbox into account if its present
        offset = 0
        if (hasattr(self, '_session')):
            offset = self._session._track_offset
        # select_1
        pos = offset + 0
        pos2 = pos + 1
        if ((num_of_tracks >= pos2) and (hasattr(self, 'select_1')) and (self.select_1 is not None)):
            self.select_1.send_value(79)
        elif ((num_of_tracks < pos2) and (hasattr(self, 'select_1')) and (self.select_1 is not None)):
            self.select_1.send_value(0)
        # select_2
        pos = offset + 1
        pos2 = pos + 1
        if ((num_of_tracks >= pos2) and (hasattr(self, 'select_2')) and (self.select_2 is not None)):
            self.select_2.send_value(79)
        elif ((num_of_tracks < pos2) and (hasattr(self, 'select_2')) and (self.select_2 is not None)):
            self.select_2.send_value(0)
        # select_3
        pos = offset + 2
        pos2 = pos + 1
        if ((num_of_tracks >= pos2) and (hasattr(self, 'select_3')) and (self.select_3 is not None)):
            self.select_3.send_value(79)
        elif ((num_of_tracks < pos2) and (hasattr(self, 'select_3')) and (self.select_3 is not None)):
            self.select_3.send_value(0)
        # select_4
        pos = offset + 3
        pos2 = pos + 1
        if ((num_of_tracks >= pos2) and (hasattr(self, 'select_4')) and (self.select_4 is not None)):
            self.select_4.send_value(79)
        elif ((num_of_tracks < pos2) and (hasattr(self, 'select_4')) and (self.select_4 is not None)):
            self.select_4.send_value(0)
            
        # select_5
        pos = offset + 4
        pos2 = pos + 1
        if ((num_of_tracks >= pos2) and (hasattr(self, 'select_5')) and (self.select_5 is not None)):
            self.select_5.send_value(79)
        elif ((num_of_tracks < pos2) and (hasattr(self, 'select_5')) and (self.select_5 is not None)):
            self.select_5.send_value(0)
        # select_6
        pos = offset + 5
        pos2 = pos + 1
        if ((num_of_tracks >= pos2) and (hasattr(self, 'select_6')) and (self.select_6 is not None)):
            self.select_6.send_value(79)
        elif ((num_of_tracks < pos2) and (hasattr(self, 'select_6')) and (self.select_6 is not None)):
            self.select_6.send_value(0)
        # select_7
        pos = offset + 6
        pos2 = pos + 1
        if ((num_of_tracks >= pos2) and (hasattr(self, 'select_7')) and (self.select_7 is not None)):
            self.select_7.send_value(79)
        elif ((num_of_tracks < pos2) and (hasattr(self, 'select_7')) and (self.select_7 is not None)):
            self.select_7.send_value(0)
        # select_8
        pos = offset + 7
        pos2 = pos + 1
        if ((num_of_tracks >= pos2) and (hasattr(self, 'select_8')) and (self.select_8 is not None)):
            self.select_8.send_value(79)
        elif ((num_of_tracks < pos2) and (hasattr(self, 'select_8')) and (self.select_8 is not None)):
            self.select_8.send_value(0)
        
    def track_select_1(self, value):
        if value > 0:
            if (hasattr(self, '_session')):
                move = self._session._track_offset + 1
            else:
                move = 1
            num_of_tracks = len(self.song().tracks)
            if num_of_tracks >= move:
                move = move - 1
                self.song().view.selected_track = self.song().tracks[move]

    def track_select_2(self, value):
        if value > 0:
            if (hasattr(self, '_session')):
                move = self._session._track_offset + 2
            else:
                move = 2
            num_of_tracks = len(self.song().tracks)
            if num_of_tracks >= move:
                move = move - 1
                self.song().view.selected_track = self.song().tracks[move]

    def track_select_3(self, value):
        if value > 0:
            if (hasattr(self, '_session')):
                move = self._session._track_offset + 3
            else:
                move = 3
            num_of_tracks = len(self.song().tracks)
            if num_of_tracks >= move:
                move = move - 1
                self.song().view.selected_track = self.song().tracks[move]

    def track_select_4(self, value):
        if value > 0:
            if (hasattr(self, '_session')):
                move = self._session._track_offset + 4
            else:
                move = 4
            num_of_tracks = len(self.song().tracks)
            if num_of_tracks >= move:
                move = move - 1
                self.song().view.selected_track = self.song().tracks[move]
    
    def track_select_5(self, value):
        if value > 0:
            if (hasattr(self, '_session')):
                move = self._session._track_offset + 5
            else:
                move = 5
            num_of_tracks = len(self.song().tracks)
            if num_of_tracks >= move:
                move = move - 1
                self.song().view.selected_track = self.song().tracks[move]

    def track_select_6(self, value):
        if value > 0:
            if (hasattr(self, '_session')):
                move = self._session._track_offset + 6
            else:
                move = 6
            num_of_tracks = len(self.song().tracks)
            if num_of_tracks >= move:
                move = move - 1
                self.song().view.selected_track = self.song().tracks[move]

    def track_select_7(self, value):
        if value > 0:
            if (hasattr(self, '_session')):
                move = self._session._track_offset + 7
            else:
                move = 7
            num_of_tracks = len(self.song().tracks)
            if num_of_tracks >= move:
                move = move - 1
                self.song().view.selected_track = self.song().tracks[move]

    def track_select_8(self, value):
        if value > 0:
            if (hasattr(self, '_session')):
                move = self._session._track_offset + 8
            else:
                move = 8
            num_of_tracks = len(self.song().tracks)
            if num_of_tracks >= move:
                move = move - 1
                self.song().view.selected_track = self.song().tracks[move]
    
    def _on_selected_track_changed(self):
        ControlSurface._on_selected_track_changed(self)
        self._display_reset_delay = 0
        value = "selected track changed"
        if (hasattr(self, '_set_track_select_led')):
            self._set_track_select_led()
        if (hasattr(self, '_reload_active_devices')):
            self._reload_active_devices(value)
        if (hasattr(self, 'update_all_ab_select_LEDs')):
            self.update_all_ab_select_LEDs(1)

    def _is_prev_device_on_or_off(self):
        self._device = self.song().view.selected_track.view.selected_device
        self._device_position = self.selected_device_idx()
        if (self._device is None) or (self._device_position == 0):
            on_off = "off"
        else:
            on_off = "on"
        return on_off

    def _is_nxt_device_on_or_off(self):
        self._selected_device = self.selected_device_idx() + 1  # add one as this starts from zero
        if (self._device is None) or (self._selected_device == len(self.song().view.selected_track.devices)):
            on_off = "off"
        else:
            on_off = "on"
        return on_off

    def _set_active_mode(self):
        global active_mode
        # activate mode
        if active_mode == "_mode4":
            self._mode4()
        elif active_mode == "_mode1":
            self._mode1()
        elif active_mode == "_mode2":
            self._mode2()
        elif active_mode == "_mode0":
            self._mode0()
        elif active_mode == "_mode3":
            self._mode3()

        if hasattr(self, '_set_track_select_led'):
            self._set_track_select_led()
        if hasattr(self, '_turn_on_device_select_leds'):
            self._turn_off_device_select_leds()
            self._turn_on_device_select_leds()
        if hasattr(self, '_all_prev_device_leds'):
            self._all_prev_device_leds()
        if hasattr(self, '_all_nxt_device_leds'):
            self._all_nxt_device_leds()
        if hasattr(self, 'update_all_ab_select_LEDs'):
            self.update_all_ab_select_LEDs(1)

    def _remove_active_mode(self):
        global active_mode
        # remove activate mode
        if active_mode == "_mode4":
            self._remove_mode4()
        elif active_mode == "_mode1":
            self._remove_mode1()
        elif active_mode == "_mode2":
            self._remove_mode2()
        elif active_mode == "_mode0":
            self._remove_mode0()
        elif active_mode == "_mode3":
            self._remove_mode3()


    def _activate_mode1(self,value):
        global active_mode
        global shift_previous_is_active
        if value > 0:
            shift_previous_is_active = "off"
            self._remove_active_mode()
            active_mode = "_mode1"
            self._set_active_mode()


    
    def selected_device_idx(self):
        self._device = self.song().view.selected_track.view.selected_device
        return self.tuple_index(self.song().view.selected_track.devices, self._device)

    def selected_track_idx(self):
        self._track = self.song().view.selected_track
        self._track_num = self.tuple_index(self.song().tracks, self._track)
        self._track_num = self._track_num + 1
        return self._track_num

    def tuple_index(self, tuple, obj):
        for i in xrange(0, len(tuple)):
            if (tuple[i] == obj):
                return i
        return(False)
     


    def disconnect(self):
        super(Midi_Fighter_3D, self).disconnect()





