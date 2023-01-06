# -*- coding: utf-8 -*-
"""Split a multi-channel midi file into single channel midi files."""


import argparse
import logging

from . import channel_splitter


def run():
    """CLI progam.
    Execute the whole process from a terminal with user defined
    params.
    """
    parser = argparse.ArgumentParser(
        description="Split a multi-chanel midi file in single channel midi files (1 per channel).",
        epilog="by: Samuel M.H. <samuel.mh@gmail.com>",
    )
    parser.add_argument(
        "midi_file",
        help="Midi file with mixed channels",
        type=argparse.FileType("rb"),
    )
    parser.add_argument(
        "-1",
        "--to_channel1",
        action="store_true",
        help="redirect events to channel 1 in the independent midi files",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="count",
        default=0,
        help="Verbose mode -vv will be even more",
    )
    args = parser.parse_args()
    logging.basicConfig(
        level={
            0: logging.ERROR,
            1: logging.INFO,
            2: logging.DEBUG,
        }.get(args.verbose, logging.DEBUG)
    )
    args.midi_file.close()
    channel_splitter.channel_splitter(
        args.midi_file.name,
        args.to_channel1,
    )
