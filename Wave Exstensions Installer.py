import os
import time
import win32com.client
from git import Repo

def clone_and_move_repo(repo_url, target_dir):
    try:
        # Clone the repository
        repo = Repo.clone_from(repo_url, target_dir)
        print(f"Cloned repository from {repo_url} to {target_dir}")

        # Check if target directory exists
        if os.path.exists(target_dir):
            print(f"Files cloned successfully to {target_dir}")
            return True
        else:
            print(f"Error: Target directory {target_dir} does not exist.")
            return False
    except Exception as e:
        print(f"Error cloning repository: {e}")
        return False

def wait_for_file(file_path, timeout=30):
    start_time = time.time()
    while not os.path.exists(file_path):
        if time.time() - start_time > timeout:
            return False
        time.sleep(1)
    return True

def create_shortcut(target_file, shortcut_location, icon_path=None):
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_location)
    shortcut.TargetPath = target_file
    if icon_path:
        shortcut.IconLocation = icon_path
    shortcut.save()
    print(f"Shortcut created for {target_file} at {shortcut_location}")

# Example usage
repo_url = 'https://github.com/DarkWareV2/Fix-Wave-And-Rate-Wave.git'
target_dir = os.path.join(os.getenv('APPDATA'), 'FixWaveAndRateWave')

success = clone_and_move_repo(repo_url, target_dir)
if success:
    # Path to Wave Exstension.py file
    wave_extension_path = os.path.join(target_dir, 'Fix Wave And Rate Wave', 'Wave Exstension.py')

    # Wait for the icon file to be available
    icon_path = os.path.join(target_dir, 'Fix Wave And Rate Wave', 'Textures', 'wave.ico')
    if not wait_for_file(icon_path):
        print(f"Error: Icon file '{icon_path}' not found within timeout period.")
    else:
        # Create a shortcut to Wave Exstension.py on the desktop
        desktop = os.path.join(os.environ['USERPROFILE'], 'Desktop')
        shortcut_location = os.path.join(desktop, 'Wave Exstension.lnk')

        create_shortcut(wave_extension_path, shortcut_location, icon_path=icon_path)
else:
    print("Failed to clone repository.")
