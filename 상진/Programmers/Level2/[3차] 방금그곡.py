def calculate_sounds(musicinfos, changes):
    infos = []
    for musicinfo in musicinfos:
        info = musicinfo.split(",")

        start = info[0].split(":")
        end = info[1].split(":")
        name = info[2]
        sounds = info[3]

        for key, val in changes.items():
            sounds = sounds.replace(key, val)
        size = len(sounds)

        total = (int(end[0]) - int(start[0])) * 60 + (int(end[1]) - int(start[1]))

        if total < size:
            infos.append([sounds[:total], name, total, info[0]])
        else:
            tmp = "".join(sounds)
            for i in range(total - size):
                tmp += sounds[i % size]
            infos.append([tmp, name, total, info[0]])

    return infos


def solution(m, musicinfos):
    changes = {'C#': '1', 'D#': '2', 'F#': '3', 'G#': "4", 'A#': '5'}

    for key, val in changes.items():
        m = m.replace(key, val)

    infos = calculate_sounds(musicinfos, changes)
    infos.sort(key=lambda x: (-x[2], x[3]))
    for info in infos:
        if m in info[0]:
            return "".join(info[1])

    return "(None)"