# vs-vfi
Using video frame interpolation models with vapoursynth. You can pipe the output directly into mpv or render it.

This repo uses a lot of code from [HolyWu/vs-rife](https://github.com/HolyWu/vs-rife).

## Install vapoursynth
```
sudo apt install yasm python3.9 python3.9-venv python3.9-dev
git clone https://github.com/sekrit-twc/zimg.git
cd zimg
./autogen.sh
./configure
make -j4
sudo make install
cd ..
pip install Cython
git clone https://github.com/vapoursynth/vapoursynth.git
cd vapoursynth
./autogen.sh
./configure
make
sudo su
make install
exit
cd ..
sudo ldconfig
sudo ln -s /usr/local/lib/python3.9/site-packages/vapoursynth.so /usr/lib/python3.9/lib-dynload/vapoursynth.so
pip install vapoursynth
sudo apt install ffmsindex libffms2-4 libffms2-dev
```
Just in case your `libffms2.so` path is different from mine, find it with `sudo find /home -name "libffms2.so"` and add it's path to `inference.py`.
```
core.std.LoadPlugin(path='/usr/lib/x86_64-linux-gnu/libffms2.so')
```

## Usage
Modify stuff like input filename, resize dimension, fp16 and model within `ìnference.py`. 

Watching video with mpv: (requires `sudo apt install mpv`)
```
vspipe --y4m inference.vpy - | mpv -
```
Rendering with x264: (requires `sudo apt install x264`)
```
vspipe --y4m inference.py - | x264 - --demuxer y4m -o example.mkv
```
Rendering with ffmpeg:
```
vspipe --y4m inference.py - | ffmpeg -i pipe: example.mkv
```
