# example usage: python main.py
# vapoursynth does not have audio support and processing multiple files is not really possible
# hacky script to make batch processing with audio and subtitle support
# make sure tmp_dir is also set in inference.py
# maybe should pass arguments instead of a text file instead
import glob
import os

input_dir = "/home/input/"
tmp_dir = "tmp/"
output_dir = "/home/output/"
files = glob.glob(input_dir + '/**/*.mkv', recursive=True)
files.sort()

for f in files:
    # creating folders if they dont exist
    if os.path.exists(tmp_dir) == False:
        os.mkdir(tmp_dir)
    if os.path.exists(output_dir) == False:  
        os.mkdir(output_dir)

    # paths
    txt_path = os.path.join(tmp_dir, "tmp.txt")
    subs_path = os.path.join(tmp_dir, "subs.srt")
    audio_path = os.path.join(tmp_dir, "audio.ogg") # ogg, aac
    out_path = os.path.join(output_dir, os.path.splitext(os.path.basename(f))[0] + "_mux.mkv")

    # writing filepath into temp txt
    # workaround to pass filename parameter
    f_txt = open(txt_path, "w")
    f_txt.write(str(f))
    f_txt.close()

    # calling vspipe and piping into ffmpeg
    os.system(f"ffmpeg -i {f} -vn -acodec copy {audio_path}")
    os.system(f"ffmpeg -i {f} -map 0:s:0 {subs_path}")
    os.system(f"vspipe --y4m inference.py - | ffmpeg -i {subs_path} -c:s mov_text -i pipe: {out_path} -i {audio_path} -c copy ")

    # deleting temp files
    os.remove(txt_path)
    os.remove(subs_path)
    os.remove(audio_path)
