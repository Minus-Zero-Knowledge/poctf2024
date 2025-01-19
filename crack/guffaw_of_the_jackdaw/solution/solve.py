import multiprocessing
import subprocess
from datetime import datetime
import hashlib

multiprocessor = True
openstego_path = "openstego.jar"
stego_file = "../public/Crack300-1.png"
output_directory = "output/"
wordlist_file = "./wordlists/monstertrucks.txt"

def try_password(password: str) -> bool:
    process_result = subprocess.run(["/usr/bin/java", "-jar", openstego_path,
                  "extract", "-sf", stego_file,
                  "-xd", output_directory,
                  "-p", password], 
                  stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    process_output = process_result.stdout
    #print(process_output)
    if process_output.startswith(b"Extracted file"):
        print(process_output)
        print(f"correct password found: {password}")
        return True
    else:  # if process_output.startswith(b"Embedded data is corrupt"):
        return False


def main():
    with open(stego_file, "rb") as f:
        assert hashlib.md5(f.read()).hexdigest() == "d97bdbf47999d3d78e9bf317244d663a"

    start_time = datetime.now()
    print(f"start time: {start_time}")
    
    with open(wordlist_file, "r") as f:
        wordlist = [w.rstrip() for w in f]
        n = len(wordlist)
    
    time_elapsed = (datetime.now() - start_time).total_seconds()
    print(f"loaded {n} words into memory in {time_elapsed:.2f} seconds")
    print(wordlist[:5] + ["..."] + wordlist[-5:])
    
    cpu_count = multiprocessing.cpu_count()
    if multiprocessor and cpu_count > 1:
        print(f"parallel processing using {cpu_count} cores")
        with multiprocessing.Pool(cpu_count) as pool:
            for result in pool.imap_unordered(try_password, wordlist, chunksize=n//cpu_count):
                if result:
                    print("password found, stopping pool...")
                    break
    else:
        print("sequential processing")
        for i, line in enumerate(words, start=1):
            if try_password(line):
                print(f"line {i}")
                break
    
    stop_time = datetime.now()
    time_elapsed = (stop_time - start_time).total_seconds()
    
    print(f"stop time: {stop_time}")
    print(f"done in {time_elapsed:.2f} seconds")
   
if __name__ == "__main__":
    main()
