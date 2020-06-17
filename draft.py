from typing import List


def unique_tags(payload: dict) -> List[str]:
    result = []
    for tag in payload.get('tags', []):
        if tag not in result:
            result.append(tag)
        else:
            for elem in result:
                if tag is not elem and tag == elem:
                    result.append(tag)
                    break
    return result


payload = {
    "title": "Звездные войны 1: Империя приносит баги",
    "description": "Эпичная сага по поиску багов в старом легаси проекте Империи",
    "tags": [2, "семейное кино", "космос", 1.0, "сага", "эпик", "добро против зла", True, "челмедведосвин", "debug",
             "ipdb", "PyCharm", "боевик", "боевик", "эникей", "дарт багус", 5, 6, 4, "блокбастер", "кино 2020", 7, 3, 9,
             12, "каникулы в космосе", "коварство", 1],
    "version": 17
}

actual = [2, 'семейное кино', 'космос', 1.0, 'сага', 'эпик', 'добро против зла', True, 'челмедведосвин', 'debug',
          'ipdb', 'PyCharm', 'боевик', 'эникей', 'дарт багус', 5, 6, 4, 'блокбастер', 'кино 2020', 7, 3, 9, 12,
          'каникулы в космосе', 'коварство', 1]

assert actual == unique_tags(payload)
