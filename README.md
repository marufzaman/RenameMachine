# Rename Machine (Subtitle Renamer)

---

Rename Machine (Subtitle Renamer) is a Python script that allows you to rename subtitle files in bulk based on the corresponding video files in a directory.

## Project Description

The Subtitle Renamer script simplifies the process of renaming subtitle files to match the video files they belong to. It extracts episode information from the video and subtitle file names based on a common pattern: `S01E01`, where `S` represents the season number, `E` represents the episode number, and both the season and episode numbers can include leading zeros. The extracted information is then used to rename the subtitle files accordingly, making it easier to organize and manage subtitle files for your video collection.

## Features

- Rename subtitle files in bulk based on video files.
- Extract episode information from video and subtitle file names.
- Intelligent matching of video and subtitle files.
- Interactive prompt for replacing existing subtitle files.
- Cross-platform compatibility (Windows, macOS, Linux).

## Future Plans

- Improved error handling and error messages.
- Support for renaming subtitle files in any video format and pattern.
- Batch processing of multiple video directories and subtitle zip files.
- Integration with subtitle databases for automatic matching.
- Graphical user interface (GUI) for a more user-friendly experience.

## Requirements

- Python 3.7 or higher
- pydantic

## Getting Started

To get started with the Rename Machine (Subtitle Renamer), make sure you have Python 3.7 or later installed on your system. You can check
your Python version by running the following command on your terminal or command prompt:

- ##### On a Windows-based system:

```shell
python --version
```

- ##### On a Linux or macOS-based system:

```shell
python3 --version
```

If you have an older Python version installed, it is recommended to upgrade to Python 3.7.x or later for compatibility
with the Rename Machine (Subtitle Renamer).

### Installation and Usage

**1.** Clone the repository:

```shell
git clone https://github.com/marufzaman/RenameMachine.git
```

> **Note:** Please after cloning the repository, go inside the `RenameMachine/` directory.

```shell
cd ./RenameMachine/
```

> The `RenameMachine/.` directory tree should look like as the following:

```
RenameMachine/.
├── LICENSE
├── README.md
├── Rename_Machine.py
└── requirements.txt
```

**2.** Create and activate a virtual environment inside the project directory (optional but recommended):

- ##### On a Windows-based system:

```shell
python -m venv venv && venv\Scripts\activate
```

- ##### On a Linux or macOS-based system:

```shell
python3 -m venv venv && source venv/bin/activate
```

**3.** Install the dependencies using pip inside the project directory and make sure you are using a virtual
environment:

- ##### On a Windows-based system:

```shell
pip install --no-cache-dir -r requirements.txt
```

- ##### On a Linux or macOS-based system:

```shell
pip3 install --no-cache-dir -r requirements.txt
```

> **Note:** Here, `--no-cache-dir` is used to avoid cache dir for the pip installation.

**4.** Run the script:

- ##### On a Windows-based system:

```shell
python Rename_Machine.py
```

- ##### On a Linux or macOS-based system:

```shell
python3 Rename_Machine.py
```

**5.** Follow the prompts to enter the path of the video directory and the subtitle zip file. Please ensure that: - The video directory contains the video files you want to rename the subtitles for. The supported video file formats are `.mkv` and `.mp4`. - The subtitle zip file contains the subtitle files corresponding to the video files. The supported subtitle file format is `.srt`.

**6.** The script will extract the subtitle files from the zip file and attempt to rename them based on the corresponding video files in the specified directory.

**7.** If a subtitle file with the same name already exists in the video directory, the script will ask whether to replace it. Enter 'Y' for Yes or 'N' for No.

**8.** The script will rename the subtitle files and display a summary of the results.

**9.** If no video files match with any subtitle files, an error message will be shown.

## **10.** You can choose to rename again by entering 'Y' when prompted. To exit the script, enter 'N'.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, please submit a pull request. For major changes, please open an issue first to discuss the proposed changes.

## Licence

This project is licenced under the [MIT Licence](LICENSE).
