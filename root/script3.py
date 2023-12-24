from pathlib import Path
import pyzipper
from tqdm import tqdm
 
def crack_password(word_list_path, zip_file_path):
    n_words = sum(1 for _ in open(word_list_path, 'r', encoding='utf-8'))
 
    print('[2] Total passwords to test:', f'{n_words:,}')
 
    password_found = False
 
    with open(word_list_path, 'r', encoding='utf-8') as wordlist:
        with pyzipper.AESZipFile(zip_file_path) as zip_file:
            for word in tqdm(wordlist, total=n_words, unit='word'):
                password = word.strip()
                print('[*] Testing password:', password)
 
                try:
                    zip_file.extractall(pwd=password.encode('utf-8'))
                except RuntimeError as e:
                    if 'Bad password for file' in str(e):
                        continue
                    else:
                        print("[!] Exception during execution:", e)
                        continue
                except Exception as e:
                    print('[!] Exception during extraction:', e)
                    continue
                else:
                    print('\n[+] Password found:', password)
                    password_found = True
                    break
 
    if not password_found:
        print("\n[!] Password not found, try other wordlist.")
 
def main():
    word_list_path = input('[0] Word List Path: ')
    zip_file_path = input('[1] Zip File Path: ')
 
    word_list = Path(word_list_path)
    zip_file = Path(zip_file_path)
 
    if word_list.exists() and zip_file.exists():
        crack_password(word_list_path, zip_file_path)
    else:
        print('[x] An incorrect or non-existent path was entered')
 
if __name__ == '__main__':
    main()