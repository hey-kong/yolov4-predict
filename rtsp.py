import platform
import subprocess as sp


def get_sp(width, height, fps, rtsp_url):
    command = ['ffmpeg',
                   '-y',
                   '-f', 'rawvideo',
                   '-vcodec', 'rawvideo',
                   '-pix_fmt', 'bgr24',
                   '-s', "{}x{}".format(width, height),
                   '-r', str(fps),
                   '-i', '-',
                   '-c:v', 'libx264',
                   '-pix_fmt', 'yuv420p',
                   '-preset', 'ultrafast',
                   '-f', 'rtsp',
                   rtsp_url]
    sys = platform.system()
    if sys == "Windows":
        p = sp.Popen(command, stdin=sp.PIPE, shell=True)
    else:
        p = sp.Popen(command, stdin=sp.PIPE)
    return p
