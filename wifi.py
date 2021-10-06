import subprocess

if __name__ == "__main__":
    print("process")
    p = ["netsh", "wlan", "show", "profiles"]
    data = subprocess.check_output(p).decode("utf-8").split("\n")
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

    for i in profiles:
        try:
            results = subprocess.check_output(["netsh", "wlan", "show", "profiles", i, "key=clear"], shell=True,stderr=subprocess.STDOUT).decode("utf-8").split("\n")
        except subprocess.CalledProcessError as e:
            print(e.output)
            continue
        # print(results)
        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
        try:
            print("{:<30} | {:<}".format(i, results[0]))
        except IndexError:
            print("{:<30} | {:<}".format(i, ""))