import os
import sys



fsb_conv_path = "./conv"

if not os.path.isfile(fsb_conv_path):
    os.system("gcc conv.c -logg -lvorbis -lvorbisfile -o conv")

OFFSET_FRESH_BEATS = 21218144

res_path = "./resources.resource"

res_path_out = "./resources.resource.patched"

def edit_res():
    f = open(res_path, "rb")
    cont = f.read()
    # cont = bytearray(cont)
    f.close()
    
    fsb_file_p = open("./out.fsb5", "rb")
    fsb_file = fsb_file_p.read()
    fsb_file = bytearray(fsb_file)
    fsb_file_p.close()
    
    fsb_size = os.path.getsize("./out.fsb5")
    
    if fsb_size > 11006016:
        print("Your song is too large! It should be under 10MB!")
        sys.exit(-1)
    
    # cont[OFFSET_FRESH_BEATS:fsb_size] = fsb_file
    
    f = open(res_path_out, "wb")
    f.write(cont)
    f.seek(OFFSET_FRESH_BEATS)
    f.write(fsb_file)
    f.close()

def make_fsb(ogg_path):
    os.system(fsb_conv_path+ " "+ogg_path + " ./out.fsb5")
    
    

make_fsb(input("Path to your song (.ogg): "))
edit_res()
print("Done!")
