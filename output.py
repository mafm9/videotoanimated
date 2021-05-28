import os
import moviepy.editor as mp
os.system("blender -b jsons/Vincent.blend -P scripts/animation.py -a")
outputclip = mp.VideoFileClip("outputvideo/output.mp4")
myclip = mp.VideoFileClip("testvideos/test4.mp4")
myclip.audio.write_audiofile("test4_audio.mp3")
audioclip = mp.AudioFileClip("test4_audio.mp3")
new_audioclip = mp.CompositeAudioClip([audioclip])
outputclip.audio = new_audioclip
outputclip.write_videofile("Vincent.mp4")
