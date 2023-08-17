import re


NONE_MUSIC_NAME = "(None)"


def solution(m, musicinfos):
    that_music_name, that_music_length = NONE_MUSIC_NAME, 0

    for musicinfo in musicinfos:
        start_time, end_time, music_name, music_melody = musicinfo.split(',')
        start_time, end_time = convert_time(start_time), convert_time(end_time)
        memory_melody, music_melody = convert_melody(m), convert_melody(music_melody)
        repeats, remain = divmod(end_time - start_time, len(music_melody))
        music_melody = music_melody * repeats + music_melody[: remain]
        is_melody_matched = re.search(memory_melody, music_melody)

        if is_melody_matched and that_music_length < len(music_melody):
            that_music_name, that_music_length = music_name, len(music_melody)

    return that_music_name


def convert_time(time_str):
    hh, mm = map(int, time_str.split(':'))

    return hh * 60 + mm


def convert_melody(music_str):
    convert_table = {"C#": 'c', "D#": 'd', "F#": 'f', "G#": 'g', "A#": 'a'}
    for key, value in convert_table.items():
        music_str = re.sub(key, value, music_str)

    return music_str