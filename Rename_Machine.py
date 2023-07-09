import os
import shutil
import zipfile
import re
from pydantic import BaseModel, ValidationError, FilePath, DirectoryPath

class SubtitleRenameInput(BaseModel):
    video_directory: DirectoryPath
    subtitle_zip_file: FilePath

    @classmethod
    def create_from_input(cls):
        while True:
            try:
                video_directory = input('Enter the Video Directory: ')
                subtitle_zip_file = input('Enter the Subtitle Zip File: ')
                return cls(
                    video_directory=os.path.abspath(video_directory),
                    subtitle_zip_file=os.path.abspath(subtitle_zip_file),
                )
            except ValidationError as e:
                print(f"Input validation error: {e.errors()}")

def extract_episode_number(file_name):
    if match := re.search(r'[sS](\d+)[eE](\d+)', file_name):
        return match[1], match[2]
    return None

def rename_machine(input_data):  # sourcery skip: low-code-quality
    video_path = input_data.video_directory
    subtitle_zip_file = input_data.subtitle_zip_file

    video_files = {}
    for file in os.listdir(video_path):
        file_path = os.path.join(video_path, file)
        if os.path.isfile(file_path) and os.path.splitext(file)[1].lower() in ('.mkv', '.mp4'):
            video_files[os.path.splitext(file)[0]] = file

    files_directory = os.path.join(os.getcwd(), 'Files')
    os.makedirs(files_directory, exist_ok=True)
    print(f"Files Directory: {files_directory}")

    try:
        with zipfile.ZipFile(subtitle_zip_file, 'r') as local_obj:
            local_obj.extractall(files_directory)
        print("Subtitle files extracted successfully.")
    except Exception as e:
        print(f"Subtitle Extraction Error: {str(e)}")

    subtitle_files = {}
    for file_name in os.listdir(files_directory):
        file_path = os.path.join(files_directory, file_name)
        if os.path.isfile(file_path) and os.path.splitext(file_name)[1].lower() == '.srt':
            episode = extract_episode_number(file_name)
            subtitle_files[episode] = file_name

    print("Subtitle Files:")
    for episode, subtitle_file in subtitle_files.items():
        print(f"Episode: {episode} - Subtitle File: {subtitle_file}")
    print()

    renamed_files = set()

    for video_name, video_file in video_files.items():
        video_episode = extract_episode_number(video_name)
        print(f"Video File: {video_file} - Episode: {video_episode}")
        if video_episode and video_episode in subtitle_files:
            subtitle_file = subtitle_files[video_episode]
            new_file_name = f'{video_name}.srt'
            old_file_path = os.path.join(files_directory, subtitle_file)
            new_file_path = os.path.join(video_path, new_file_name)

            if not os.path.exists(new_file_path):
                try:
                    shutil.move(old_file_path, new_file_path)
                    renamed_files.add(subtitle_file)
                    print(f"Integration Successful: Renamed subtitle file {subtitle_file} to {new_file_name}")
                except Exception as e:
                    print(f"Integration Error: {str(e)}")
            else:
                choice = input(f"Subtitle file '{new_file_name}' already exists. Replace? (Y/N): ").lower()
                if choice == 'y':
                    try:
                        shutil.move(old_file_path, new_file_path)
                        renamed_files.add(subtitle_file)
                        print(f"Integration Successful: Renamed subtitle file {subtitle_file} to {new_file_name}")
                    except Exception as e:
                        print(f"Integration Error: {str(e)}")
                else:
                    print(f"Integration Skipped: Subtitle file {subtitle_file} already exists as {new_file_name}")

    shutil.rmtree(files_directory, ignore_errors=True)

    if not renamed_files:
        print("Error: No video files matched with any subtitle files.")
        return

    return renamed_files

def main():
    while True:
        input_data = SubtitleRenameInput.create_from_input()
        renamed_files = rename_machine(input_data)
        if not renamed_files:
            print("Error: No video files matched with any subtitle files.")
            break

        again = input("Rename Again (Y/N): ").lower()
        if again != 'y':
            print("\nThanks for using!\n")
            break

if __name__ == '__main__':
    main()
