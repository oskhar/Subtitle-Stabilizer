# Subtitle Stabilizer

Subtitle Stabilizer is a comprehensive toolset for managing, manipulating, and synchronizing subtitle files. It provides a variety of functionalities to adjust subtitle timings, merge and split subtitle files, convert formats, and more. This tool is essential for anyone working with subtitle files, whether for video editing, translation, or improving viewing experiences.

## Features

- **Adjust Subtitle Start Times:** Shift the start times of subtitle entries by a specified offset.
- **Adjust Subtitle End Times:** Shift the end times of subtitle entries by a specified offset.
- **Synchronize Subtitles:** Synchronize subtitle timings with a video based on a given sync point.
- **Merge Subtitles:** Combine multiple subtitle files into one.
- **Split Subtitles:** Divide a subtitle file into multiple files based on duration or time points.
- **Convert Subtitle Formats:** Convert between different subtitle formats (e.g., SRT, VTT).
- **Search and Replace Text:** Find and replace text within subtitle files.
- **Check and Fix Subtitle Errors:** Detect and correct common format errors in subtitle files.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Install Dependencies

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/subtitle-stabilizer.git
cd subtitle-stabilizer
pip install -r requirements.txt
```

## Usage

### Adjust Subtitle Start Times

Shift the start times of all subtitle entries by a specified offset.

```bash
python scripts/update_start_time.py path/to/subtitle.srt 01:01:02,500
```

### Adjust Subtitle End Times

Shift the end times of all subtitle entries by a specified offset.

```bash
python scripts/update_end_time.py path/to/subtitle.srt 01:01:02,500
```

### Synchronize Subtitles

Synchronize subtitle timings with a video based on original and target sync points.

```bash
python scripts/synchronize_subtitle.py path/to/subtitle.srt 00:10:00,000 00:12:00,000
```

### Merge Subtitles

Combine multiple subtitle files into one.

```bash
python scripts/merge_subtitles.py path/to/subtitle1.srt path/to/subtitle2.srt path/to/output.srt
```

### Split Subtitles

Divide a subtitle file into multiple files based on duration or specific time points.

```bash
python scripts/split_subtitles.py path/to/subtitle.srt 00:10:00,000 00:20:00,000
```

### Convert Subtitle Formats

Convert between different subtitle formats, e.g., SRT to VTT.

```bash
python scripts/convert_subtitles.py path/to/subtitle.srt path/to/output.vtt
```

### Search and Replace Text

Find and replace text within subtitle files.

```bash
python scripts/search_replace_subtitle.py path/to/subtitle.srt "old text" "new text"
```

### Check and Fix Subtitle Errors

Detect and correct common format errors in subtitle files.

```bash
python scripts/check_fix_subtitle.py path/to/subtitle.srt
```

## Examples

### Example: Adjust Start and End Times

To shift both start and end times by an offset of 01:01:02,500:

```bash
python scripts/update_start_time.py path/to/subtitle.srt 01:01:02,500
python scripts/update_end_time.py path/to/subtitle.srt 01:01:02,500
```

### Example: Merge Subtitles

To merge `subtitle1.srt` and `subtitle2.srt` into `merged.srt`:

```bash
python scripts/merge_subtitles.py subtitle1.srt subtitle2.srt merged.srt
```

## Contributing

We welcome contributions to Subtitle Stabilizer! Here are some ways you can help:

- **Report Bugs:** If you find a bug, please open an issue with detailed steps to reproduce the problem.
- **Suggest Features:** Have an idea for a new feature? Open an issue and let's discuss it.
- **Submit Pull Requests:** If you'd like to contribute code, please fork the repository, make your changes, and submit a pull request.

### Guidelines

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

Subtitle Stabilizer is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contact

For any inquiries or support, please contact us at [muhamadoskhar@gmail.com](mailto:muhamadoskhar@gmail.com).

## Acknowledgements

We'd like to thank the open-source community for their invaluable contributions and support. Your feedback and involvement help us to continuously improve Subtitle Stabilizer.

## Frequently Asked Questions (FAQ)

### How do I install Subtitle Stabilizer?

Please refer to the [Installation](#installation) section for detailed instructions.

### What subtitle formats are supported?

Currently, Subtitle Stabilizer supports SRT and VTT formats. More formats will be added in future releases.

### Can I contribute to Subtitle Stabilizer?

Absolutely! We welcome all contributions. Please refer to the [Contributing](#contributing) section for more information.

### How can I contact the developers?

For any inquiries or support, please contact us at [muhamadoskhar@gmail.com](mailto:muhamadoskhar@gmail.com).

---

Thank you for using Subtitle Stabilizer! We hope this tool helps you manage and synchronize your subtitles with ease.
