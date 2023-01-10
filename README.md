# smh\_midi\_utils

# Introduction
This is a repository where I store all the midi tools I create.
They have no other purpose but to serve my purposes, if they are useful to you too... Congratulations!


# Programs

## channel\_splitter
This program takes a simple midi file (i.e. [`.smf`](https://www.midi.org/specifications-old/item/standard-midi-files-smf)) and separate the events per channel. It creates as many midi files as channels there are in the original file.

I created this utility because I have a [Juno-DS](https://www.roland.com/es-es/products/juno-ds/) and the export format of a pattern did not suit my workflow. A pattern is a combination of 8 instruments with a fixed lenght (n bars). The export format mix all the instruments on a single file with different channels and I wanted to have them separated so I can edit them indepently.

Usage example:
```bash
python -m smh_midi_utils.channel_splitter -1 -v multichannel_midi.smf
```



# Functionalities
Things that are already done with the right tools. No need to code!

## List MIDI devices
List the available MIDI ports

```bash
amidi -l
```

## Record/Play MIDI messages
Connect to a port and write all the received messages to a file.
_I.E. Get `sysex` messages to configure the tone of a synth._

```bash
amidi -p "hw:1,0,0" -r "test.mid" -d
```


## Play MIDI messages
Connect to a port and send messages from a file.
_I.E. Set a patch tone with `sysex` messages._
```bash
amidi -p "hw:1,0,0" -s "test.mid"
```
