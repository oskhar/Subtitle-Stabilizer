from datetime import timedelta, datetime
import argparse
import re

# Fungsi untuk mengonversi string waktu ke timedelta
def str_to_timedelta(time_str):
    return datetime.strptime(time_str, "%H:%M:%S,%f") - datetime.strptime("00:00:00,000", "%H:%M:%S,%f")

# Fungsi untuk mengonversi timedelta kembali ke string waktu
def timedelta_to_str(td):
    total_seconds = int(td.total_seconds())
    milliseconds = td.microseconds // 1000
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

# Fungsi untuk memperbarui waktu subtitle
def update_subtitle_time(file_path, offset):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    time_pattern = re.compile(r"(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})")
    updated_lines = []

    for line in lines:
        match = time_pattern.match(line)
        if match:
            start_time = str_to_timedelta(match.group(1))
            end_time = str_to_timedelta(match.group(2))
            new_start_time = timedelta_to_str(start_time + offset)
            new_end_time = timedelta_to_str(end_time + offset)
            updated_line = f"{new_start_time} --> {new_end_time}\n"
            updated_lines.append(updated_line)
        else:
            updated_lines.append(line)

    output_path = 'updated_' + file_path
    with open(output_path, 'w', encoding='utf-8') as file:
        file.writelines(updated_lines)
    
    print(f"Subtitle times updated and saved to '{output_path}'")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Update subtitle timings by adding an offset.')
    parser.add_argument('file_path', type=str, help='Path to the subtitle file (.srt)')
    parser.add_argument('offset', type=str, help='Time offset to add in the format HH:MM:SS,mmm')

    args = parser.parse_args()

    # Parse the offset argument to a timedelta
    offset_parts = args.offset.split(':')
    hours, minutes = int(offset_parts[0]), int(offset_parts[1])
    seconds, milliseconds = map(int, offset_parts[2].split(','))
    offset = timedelta(hours=hours, minutes=minutes, seconds=seconds, milliseconds=milliseconds)

    update_subtitle_time(args.file_path, offset)
