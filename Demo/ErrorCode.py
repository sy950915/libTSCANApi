from libTSCANAPI import *
with open("./ErrorCode.txt", "w+") as f:
    for i in range(0, 69):
        ret = c_char_p()
        tscan_get_error_description(i, ret)
        f.write(str(i)+"          "+ret.value.decode("utf8")+"\n")


    