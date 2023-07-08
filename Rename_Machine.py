import os
import shutil
import zipfile

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


def rename_machine(input_data):
    video_path = input_data.video_directory
    subtitle_zip_file = input_data.subtitle_zip_file

    video_files = [
        os.path.splitext(file)[0]
        for file in os.listdir(video_path)
        if os.path.isfile(os.path.join(video_path, file))
        and os.path.splitext(file)[1].lower() in ('.mkv', '.mp4')
    ]

    files_directory = os.path.join(os.getcwd(), 'Files')
    os.makedirs(files_directory, exist_ok=True)

    with zipfile.ZipFile(subtitle_zip_file, 'r') as local_obj:
        local_obj.extractall(files_directory)

    for i, file in enumerate(os.listdir(files_directory)):
        new_file_name = f'{video_files[i]}.srt'
        old_file_path = os.path.join(files_directory, file)
        new_file_path = os.path.join(video_path, new_file_name)
        shutil.move(old_file_path, new_file_path)

    shutil.rmtree(files_directory, ignore_errors=True)

    return input("Rename Again (Y/N): ").lower()


def main():
    while True:
        input_data = SubtitleRenameInput.create_from_input()
        again = rename_machine(input_data)
        if again != 'y':
            print("\nThanks for using!\n")
            break


if __name__ == '__main__':
    main()
