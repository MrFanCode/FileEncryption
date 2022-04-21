import os
import time


check_folder = os.listdir()

if "Keys" not in check_folder:
    os.system("mkdir Keys")

time.sleep(2)



check_keys = os.listdir("Keys")

if "private.key" in check_folder and "public.key" in check_folder:
    exit()
elif "private.key" not in check_keys and "public.key" not in check_keys:
    os.system(f"openssl genrsa -aes-256-cbc -out private.key")
    os.system(f"openssl rsa -in private.key -pubout -out public.key")
    os.system(f"mv private.key Keys/")
    os.system(f"mv public.key Keys/")
    print("Key files generated.")




#os.listdir("Keys")

#if 
    #os.system(f"openssl genrsa -aes-256-cbc -out private.key")
    #os.system(f"openssl rsa -in private.key -pubout -out public.key")
    #os.system(f"mv private.key Keys/")
    #os.system(f"mv public.key Keys/")
    #print("Key files generated.")
#else:
    #print("There was an error!")




