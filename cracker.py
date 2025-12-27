import hashlib
import time
import os
try:
    from colorama import Fore, Style, init
    init()
except ImportError:
    # Agar colorama install nahi hai to basic color use karein
    class Fore: GREEN = ""; RED = ""; YELLOW = ""; CYAN = ""; WHITE = ""
    class Style: RESET_ALL = ""

def panther_banner():
    # Ye tumhara Personal Brand hai
    print(Fore.GREEN + """
    =============================================
       🐆 PANTHER HASH CRACKER v1.0 🐆
       [ MD5 Dictionary Attack Tool ]
       Created by: Samir Raja (Cyber Security)
    =============================================
    """ + Style.RESET_ALL)

def crack_password(target_hash, wordlist_file):
    print(Fore.YELLOW + f"\n[*] Loading Database: {wordlist_file}...")
    
    if not os.path.exists(wordlist_file):
        print(Fore.RED + f"[!] Error: File '{wordlist_file}' nahi mili!")
        return

    print(f"[*] Target Hash: {target_hash}")
    print(Fore.CYAN + "[*] Attack Started... Matching patterns...\n")
    time.sleep(1) # Thoda hacker wala feel dene ke liye

    count = 0
    start_time = time.time()

    with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            password = line.strip()
            count += 1
            
            # Password ko Hash mein badalna (MD5)
            hashed_attempt = hashlib.md5(password.encode('utf-8')).hexdigest()

            # Match Check karna
            if hashed_attempt == target_hash:
                end_time = time.time()
                print(Fore.GREEN + f"=============================================")
                print(f" [SUCCESS] PASSWORD CRACKED! 🔓")
                print(f" 🔑 Password: {password}")
                print(f" ⏱️ Time Taken: {round(end_time - start_time, 2)} seconds")
                print(f" 🔄 Attempts: {count}")
                print(f"=============================================" + Style.RESET_ALL)
                return

    print(Fore.RED + "\n[FAILED] Password wordlist mein nahi mila.")

# --- Tool Start Yahan Se Hoga ---
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear') # Screen saaf karna
    panther_banner()

    # User se Input lena
    target = input(Fore.WHITE + "Enter MD5 Hash: ").strip()
    wordlist = input("Enter Wordlist File (e.g. pass.txt): ").strip()

    crack_password(target, wordlist)