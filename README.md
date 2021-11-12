# vs-vfi
Using video frame interpolation models with vapoursynth. You can pipe the output directly into mpv or render it.

## Install vapoursynth
```
sudo apt install yasm python3.9 python3.9-venv python3.9-dev
pip install Cython
git clone https://github.com/vapoursynth/vapoursynth.git
cd vapoursynth
./autogen.sh
./configure
make
sudo su
make install
exit
pip install vapoursynth
```
Find `libffms2.so` (you can use `sudo find /home -name "libffms2.so"`) and add it's path to `inference.py`.
```
core.std.LoadPlugin(path='/usr/lib/x86_64-linux-gnu/libffms2.so')
```

## Usage
Modify stuff like resize dimension, fp16 and model within `ìnference.py`. 

Watching video with mpv: (requires `sudo apt install mpv`)
```
vspipe --y4m inference.vpy - | mpv -
```
Rendering with x264: (requires `sudo apt install x264`)
```
vspipe --y4m inference.py - | x264 - --demuxer y4m -o example.mkv
```
