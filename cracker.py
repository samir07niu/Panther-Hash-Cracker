import hashlib
import time
import os
import sys

# --- DEPENDENCY CHECK ---
try:
    from colorama import Fore, Style, init
    init()
except ImportError:
    # Fallback if colorama is not installed
    class Fore: GREEN = ""; RED = ""; YELLOW = ""; CYAN = ""; WHITE = ""
    class Style: RESET_ALL = ""

def panther_banner():
    """Displays the tool banner/logo."""
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
        print(Fore.RED + f"[!] Error: File '{wordlist_file}' not found.")
        return

    print(f"[*] Target Hash: {target_hash}")
    print(Fore.CYAN + "[*] Attack Started... Matching patterns...\n")
    
    # Simulating initialization sequence for UX
    time.sleep(1) 

    count = 0
    start_time = time.time()

    try:
        with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                password = line.strip()
                count += 1
                
                # Encrypting password to MD5 for comparison
                hashed_attempt = hashlib.md5(password.encode('utf-8')).hexdigest()

                # Comparing Hash
                if hashed_attempt == target_hash:
                    end_time = time.time()
                    print(Fore.GREEN + f"=============================================")
                    print(f" [SUCCESS] PASSWORD CRACKED! 🔓")
                    print(f" 🔑 Password: {password}")
                    print(f" ⏱️ Time Taken: {round(end_time - start_time, 2)} seconds")
                    print(f" 🔄 Attempts: {count}")
                    print(f"=============================================" + Style.RESET_ALL)
                    return

        print(Fore.RED + "\n[FAILED] Password not found in the provided wordlist.")
        
    except Exception as e:
        print(Fore.RED + f"[!] Runtime Error: {e}")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Clear Screen based on OS
    os.system('cls' if os.name == 'nt' else 'clear') 
    panther_banner()

    # User Inputs
    try:
        target = input(Fore.WHITE + "Enter MD5 Hash: ").strip()
        wordlist = input("Enter Wordlist File (e.g. pass.txt): ").strip()
        crack_password(target, wordlist)
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Operation Cancelled by User.")
