import moviepy.editor as mpe

clip = mpe.VideoFileClip("output.mp4")
audio_bg = mpe.AudioFileClip("story.mp3")
final_clip = clip.set_audio(audio_bg)
final_clip.write_videofile("final.mp4")