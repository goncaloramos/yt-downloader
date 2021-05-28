import os
import pathlib
import dlfuncs

#get current dir
cwd = os.getcwd()
print("Current dir: " + cwd)

#create dls dir if not exists
path = pathlib.Path(cwd + "/dls")
path.mkdir(parents=True, exist_ok=True)

#main
yt = dlfuncs.user_input()
dlfuncs.content_info(yt)
ys = dlfuncs.locate_highest_res(yt)
dlfuncs.start_download(ys, path)