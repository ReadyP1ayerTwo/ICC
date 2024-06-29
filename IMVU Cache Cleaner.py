import os
import time
import psutil
import shutil

def check_process(process_name):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process_name:
            return True
    return False

def delete_http_cache():
    http_cache_path = os.path.join(os.getenv('APPDATA'), 'IMVU', 'HttpCache')
    if os.path.exists(http_cache_path):
        shutil.rmtree(http_cache_path)
    os.makedirs(http_cache_path)
    print("\033[92mHttpCache contents deleted.\033[0m")

def delete_imvu_studio():
    imvu_studio_path = os.path.join(os.getenv('APPDATA'), 'imvu-studio')
    if os.path.exists(imvu_studio_path):
        shutil.rmtree(imvu_studio_path)
    print("\033[92mIMVU Studio folder deleted.\033[0m")

def exit_message():
    print("\n\033[93m########################################################")
    print("#                                                      #")
    print("#            Exiting... Shop Spikes!                   #")
    print("#                                                      #")
    print("########################################################\033[0m")
    time.sleep(5)
    exit()

def main_menu():
    print("\033[92m")
    print("     ___/\/\/\/\/\__/\/\/\/\/\____/\/\/\/\__/\/\____/\/\__/\/\/\/\/\/\____/\/\/\/\/\_                ")
    print("    _/\/\__________/\/\____/\/\____/\/\____/\/\__/\/\____/\____________/\/\_________                ")
    print("   ___/\/\/\/\____/\/\/\/\/\______/\/\____/\/\/\/\______/\/\/\/\/\______/\/\/\/\___                ")
    print("  _________/\/\__/\/\____________/\/\____/\/\__/\/\____/\/\__________________/\/\_                ")
    print(" _/\/\/\/\/\____/\/\__________/\/\/\/\__/\/\____/\/\__/\/\/\/\/\/\__/\/\/\/\/\___                ")
    print("________________________________________________________________________________                ")
    print("     ___/\/\/\/\/\__/\/\________/\/\/\/\/\/\______/\/\______/\/\____/\/\__/\/\/\/\/\/\__/\/\/\/\/\___")
    print("    _/\/\__________/\/\________/\______________/\/\/\/\____/\/\/\__/\/\__/\____________/\/\____/\/\_")
    print("   _/\/\__________/\/\________/\/\/\/\/\____/\/\____/\/\__/\/\/\/\/\/\__/\/\/\/\/\____/\/\/\/\/\___")
    print("  _/\/\__________/\/\________/\/\__________/\/\/\/\/\/\__/\/\__/\/\/\__/\/\__________/\/\__/\/\___")
    print(" ___/\/\/\/\/\__/\/\/\/\/\__/\/\/\/\/\/\__/\/\____/\/\__/\/\____/\/\__/\/\/\/\/\/\__/\/\____/\/\_")
    print("________________________________________________________________________________________________")
    print("\033[0m")

    print("Select an option:")
    print("1. Delete contents of IMVU Classic HttpCache")
    print("2. Delete the IMVU Studio folder")
    print("3. Perform both actions")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        delete_http_cache()
    elif choice == "2":
        delete_imvu_studio()
    elif choice == "3":
        delete_http_cache()
        delete_imvu_studio()
    elif choice == "4":
        exit_message()
    else:
        print("\033[91mInvalid choice, please select a valid option.\033[0m")
        main_menu()

if __name__ == "__main__":
    if check_process("imvuclient.exe"):
        print("\033[91mIMVU Classic is running. Please close IMVU Classic before running the cache cleaner.\033[0m")
        exit()
    
    if check_process("imvu-studio.exe"):
        print("\033[91mIMVU Studio is running. Please close IMVU Studio before running the cache cleaner.\033[0m")
        exit()
    
    main_menu()
    exit_message()
