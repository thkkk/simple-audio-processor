# simple-audio-processor
A simple audio processor(SAP) based on pydub and ffmpeg. 

First, please download ffmpeg via http://ffmpeg.org/, install it and set up the environment variable. You can try `ffmpeg –version` to check if ffmpeg is installed correctly.


| arg | default | example | choice |  help |
| :---: | :---: | :---: | :---: | :---: | 
| --type | merge | --type=merge | merge, cut |  - |
| --files | - | -f c.mp3 d.mp3 | merge, cut |  The lists of audio files that needs to be cut or merged. **If --type=cut, number of files must be 1.** For exmample, -f a.mp3 b.mp3 |
| --time_intervals | merge | -t 0 13 51 -1 | merge, cut |  **Only used when --type=cut.** The time period that needs to be cut. Unit: second. For example, -t 0 14 17 28 means [0, 14] merged on [17, 28]. By the way, -1 means the end. |
| --output_type | mp3 | -o mp3 | - | 'mp3', 'wav', 'raw', 'ogg' or other ffmpeg/avconv supported files |


Some examples:

```shell
python sap.py --type=merge -f c.mp3 d.mp3
python sap.py --type=cut -f a.m4a -t 0 13 16 20
python sap.py --type=cut -f a.m4a -t 0 13 51 -1
```


## TODO

Adjust the audio to be merged so that the loudness is consistent.
