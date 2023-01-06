# -*- coding: utf-8 -*-
"""Split a multi-channel midi file into single channel midi files."""


from collections import defaultdict
import logging
import math

import mido


def channel_splitter(path_file, to_channel1):
    f_mid_in = path_file
    logging.info(f"Multi-channel midi file path: {f_mid_in}")
    mid_in = mido.MidiFile(f_mid_in)
    logging.info(f"Ticks per beat: {mid_in.ticks_per_beat}")
    n_beats = math.ceil(sum([x.time for x in mid_in.tracks[0]]) / mid_in.ticks_per_beat)
    logging.info(f"Estimated number of beats: {n_beats}")
    max_tick = n_beats * mid_in.ticks_per_beat - 1
    logging.info(f"Max tick time: {max_tick}")

    # Mixed tracks
    channels = {m.channel for m in mid_in.tracks[0] if hasattr(m, "channel")}
    logging.info(f"Detected tracks: {len(channels)}")

    channel_tracks = defaultdict(lambda: mido.MidiTrack())
    channel_times = defaultdict(lambda: 0)  # Last event time per channel
    time = -1  # Tick time
    for msg in mid_in.tracks[0]:
        if time < 0:
            time = 0
        time += msg.time
        if msg.type in {"note_on", "note_off"}:
            m = msg.copy()
            m.time = (
                time - channel_times[msg.channel]
            )  # Delta from last event in the channel
            if to_channel1:
                m.channel = 0
            channel_times[msg.channel] = time
            channel_tracks[msg.channel].append(m)
    # Write files
    for channel, track in channel_tracks.items():
        f_mid_out = f"{channel+1:02}.mid"
        logging.info(f"Exporting channel num {channel} to {f_mid_out}")
        mido.MidiFile(ticks_per_beat=mid_in.ticks_per_beat, tracks=[track]).save(
            f_mid_out
        )
