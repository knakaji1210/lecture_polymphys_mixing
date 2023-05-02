import moviepy.editor as mp

default_path = "./gif/"
gif_file_name = input("name of gif file: ")
gif_file = default_path+gif_file_name+".gif"
mp4_file = default_path+gif_file_name+".mp4"

print(gif_file)

clip = mp.VideoFileClip(gif_file)
clip.write_videofile(mp4_file)

clip.close()