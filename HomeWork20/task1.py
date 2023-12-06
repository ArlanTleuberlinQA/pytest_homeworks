import subprocess
import platform


def ping_websites(websites, count=3):
    system_platform = platform.system().lower()

    if system_platform == "windows":
        command = ["ping", "-n", str(count)]
    elif system_platform == "linux":
        command = ["ping", "-c", str(count)]
    else:
        print("Unsupported operating system")
        return

    for website in websites:
        print(f"Pinging {website}")
        command.append(website)
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError:
            print(f"Failed to ping {website}")
        command.pop()


if __name__ == '__main__':
    websites_to_ping = input("Введіть адреси сайтів через пробіл ").split()
    ping_websites(websites_to_ping)
