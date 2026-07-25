"""Interactive music theory practice tool.

This module provides scale drills, chord drills, progressions, chord-note lookup,
quiz mode, random practice, and simple practice stats.
"""

import json
import random
from typing import List, Optional, Tuple

PRACTICE_TYPES = [
    "Scales",
    "Chords",
    "Progressions",
    "Chord Notes",
    "Stats",
    "Coach",
    "Random",
    "Quiz",
]
VALID_MODES = {"major": "Major", "minor": "Minor"}
VALID_RATINGS = {"easy": "Easy", "medium": "Medium", "hard": "Hard"}

practice_log: List[dict] = []

major_scales = {
    "C": ["C", "D", "E", "F", "G", "A", "B"],
    "Db": ["Db", "Eb", "F", "Gb", "Ab", "Bb", "C"],
    "D": ["D", "E", "F#", "G", "A", "B", "C#"],
    "Eb": ["Eb", "F", "G", "Ab", "Bb", "C", "D"],
    "E": ["E", "F#", "G#", "A", "B", "C#", "D#"],
    "F": ["F", "G", "A", "Bb", "C", "D", "E"],
    "Gb": ["Gb", "Ab", "Bb", "Cb", "Db", "Eb", "F"],
    "G": ["G", "A", "B", "C", "D", "E", "F#"],
    "Ab": ["Ab", "Bb", "C", "Db", "Eb", "F", "G"],
    "A": ["A", "B", "C#", "D", "E", "F#", "G#"],
    "Bb": ["Bb", "C", "D", "Eb", "F", "G", "A"],
    "B": ["B", "C#", "D#", "E", "F#", "G#", "A#"],
}

minor_scales = {
    "C": ["C", "D", "Eb", "F", "G", "Ab", "Bb"],
    "Db": ["Db", "Eb", "E", "Gb", "Ab", "A", "Bb"],
    "D": ["D", "E", "F", "G", "A", "Bb", "C"],
    "Eb": ["Eb", "F", "Gb", "Ab", "Bb", "Cb", "Db"],
    "E": ["E", "F#", "G", "A", "B", "C", "D"],
    "F": ["F", "G", "Ab", "Bb", "C", "Db", "Eb"],
    "Gb": ["Gb", "Ab", "A", "B", "Db", "D", "E"],
    "G": ["G", "A", "Bb", "C", "D", "Eb", "F"],
    "Ab": ["Ab", "Bb", "Cb", "Db", "Eb", "E", "Gb"],
    "A": ["A", "B", "C", "D", "E", "F", "G"],
    "Bb": ["Bb", "C", "Db", "Eb", "F", "Gb", "Ab"],
    "B": ["B", "C#", "D", "E", "F#", "G", "A"],
}

major_chords = {
    "C": ["C", "Dm", "Em", "F", "G", "Am", "Bdim"],
    "Db": ["Db", "Ebm", "Fm", "Gb", "Ab", "Bbm", "Cdim"],
    "D": ["D", "Em", "F#m", "G", "A", "Bm", "C#dim"],
    "Eb": ["Eb", "Fm", "Gm", "Ab", "Bb", "Cm", "Ddim"],
    "E": ["E", "F#m", "G#m", "A", "B", "C#m", "D#dim"],
    "F": ["F", "Gm", "Am", "Bb", "C", "Dm", "Edim"],
    "Gb": ["Gb", "Abm", "Bbm", "Cb", "Db", "Ebm", "Fdim"],
    "G": ["G", "Am", "Bm", "C", "D", "Em", "F#dim"],
    "Ab": ["Ab", "Bbm", "Cm", "Db", "Eb", "Fm", "Gdim"],
    "A": ["A", "Bm", "C#m", "D", "E", "F#m", "G#dim"],
    "Bb": ["Bb", "Cm", "Dm", "Eb", "F", "Gm", "Adim"],
    "B": ["B", "C#m", "D#m", "E", "F#", "G#m", "A#dim"],
}

minor_chords = {
    "C": ["Cm", "Ddim", "Eb", "Fm", "Gm", "Ab", "Bb"],
    "Db": ["Dbm", "Ebdim", "E", "Gbm", "Abm", "A", "B"],
    "D": ["Dm", "Edim", "F", "Gm", "Am", "Bb", "C"],
    "Eb": ["Ebm", "Fdim", "Gb", "Abm", "Bbm", "Cb", "Db"],
    "E": ["Em", "F#dim", "G", "Am", "Bm", "C", "D"],
    "F": ["Fm", "Gdim", "Ab", "Bbm", "Cm", "Db", "Eb"],
    "Gb": ["Gbm", "Abdim", "A", "Bbm", "Dbm", "D", "Eb"],
    "G": ["Gm", "Adim", "Bb", "Cm", "Dm", "Eb", "F"],
    "Ab": ["Abm", "Bbdim", "Cb", "Dbm", "Ebm", "E", "Gb"],
    "A": ["Am", "Bdim", "C", "Dm", "Em", "F", "G"],
    "Bb": ["Bbm", "Cdim", "Db", "Ebm", "Fm", "Gb", "Ab"],
    "B": ["Bm", "C#dim", "D", "Em", "F#m", "G", "A"],
}

chord_notes = {
    "C": ["C", "E", "G"],
    "Db": ["Db", "F", "Ab"],
    "D": ["D", "F#", "A"],
    "Eb": ["Eb", "G", "Bb"],
    "E": ["E", "G#", "B"],
    "F": ["F", "A", "C"],
    "Gb": ["Gb", "Bb", "Db"],
    "G": ["G", "B", "D"],
    "Ab": ["Ab", "C", "Eb"],
    "A": ["A", "C#", "E"],
    "Bb": ["Bb", "D", "F"],
    "B": ["B", "D#", "F#"],
    "Cm": ["C", "Eb", "G"],
    "Dbm": ["Db", "E", "Ab"],
    "Dm": ["D", "F", "A"],
    "Ebm": ["Eb", "Gb", "Bb"],
    "Em": ["E", "G", "B"],
    "Fm": ["F", "Ab", "C"],
    "Gbm": ["Gb", "A", "Db"],
    "Gm": ["G", "Bb", "D"],
    "Abm": ["Ab", "B", "Eb"],
    "Am": ["A", "C", "E"],
    "Bbm": ["Bb", "Db", "F"],
    "Bm": ["B", "D", "F#"],
    "Bdim": ["B", "D", "F"],
    "Cdim": ["C", "Eb", "Gb"],
    "C#dim": ["C#", "E", "G"],
    "Ddim": ["D", "F", "Ab"],
    "D#dim": ["D#", "F#", "A"],
    "Edim": ["E", "G", "Bb"],
    "Fdim": ["F", "Ab", "B"],
    "F#dim": ["F#", "A", "C"],
    "Gdim": ["G", "Bb", "Db"],
    "Abdim": ["Ab", "B", "D"],
    "Adim": ["A", "C", "Eb"],
    "A#dim": ["A#", "C#", "E"],
    "Bbdim": ["Bb", "Db", "E"],
    "Ebdim": ["Eb", "Gb", "A"],
}

progressions = {
    "2-5-1": [1, 4, 0],
    "7-3-6": [6, 2, 5],
    "1-4-5": [0, 3, 4],
    "6-2-5-1": [5, 1, 4, 0],
}


def save_progress() -> None:
    with open("practice_log.json", "w") as file:
        json.dump(practice_log, file)


def load_progress() -> List[dict]:
    try:
        with open("practice_log.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def normalize_key(key_string: str) -> str:
    if not key_string:
        return ""

    normalized = (
        key_string.strip()
        .lower()
        .replace("sharp", "#")
        .replace("♯", "#")
        .replace("flat", "b")
        .replace("♭", "b")
        .replace(" ", "")
    )

    if len(normalized) >= 2 and normalized[1] in {"#", "b"}:
        return normalized[0].upper() + normalized[1]

    return normalized.upper()


def normalize_mode(mode_string: str) -> str:
    return VALID_MODES.get(mode_string.strip().lower(), "")


def print_list(title: str, items: List[str]) -> None:
    print(f"\n{title}:")
    for item in items:
        print(item)


def get_music_data(
    practice_type: str,
    key: str,
    mode: str,
    progression_name: Optional[str] = None,
) -> Tuple[Optional[str], Optional[List[str]]]:
    if practice_type == "Scales":
        if mode == "Major" and key in major_scales:
            return f"{key} Major Scale", major_scales[key]
        if mode == "Minor" and key in minor_scales:
            return f"{key} Minor Scale", minor_scales[key]

    if practice_type == "Chords":
        if mode == "Major" and key in major_chords:
            return f"{key} Major Chords", major_chords[key]
        if mode == "Minor" and key in minor_chords:
            return f"{key} Minor Chords", minor_chords[key]

    if practice_type == "Progressions" and progression_name:
        progression_name = progression_name.strip()
        if progression_name in progressions:
            chord_indices = progressions[progression_name]
            if mode == "Major" and key in major_chords:
                chords = major_chords[key]
            elif mode == "Minor" and key in minor_chords:
                chords = minor_chords[key]
            else:
                return None, None
            return (
                f"{progression_name} Progression in {key} {mode}",
                [chords[index] for index in chord_indices],
            )

    return None, None


def show_stats() -> None:
    if not practice_log:
        print("\nNo practice data yet.")
        return

    print(f"\nTotal drills completed: {len(practice_log)}")

    hard_keys = [entry["key"] for entry in practice_log if entry["rating"] == "Hard"]
    if hard_keys:
        print(f"Weak keys: {set(hard_keys)}")
    else:
        print("Weak keys: None yet")

    key_counts = {}
    for entry in practice_log:
        key_counts[entry["key"]] = key_counts.get(entry["key"], 0) + 1

    print(f"Most practiced key: {max(key_counts, key=key_counts.get)}")


def ask_rating() -> str:
    while True:
        rating = input("\nHow hard was this? Easy, Medium, Hard: ").strip().lower()
        if rating in VALID_RATINGS:
            return VALID_RATINGS[rating]
        print("Invalid rating. Please enter Easy, Medium, or Hard.")


def log_drill(key: str, practice_type: str, mode: str, items: List[str]) -> None:
    rating = ask_rating()
    practice_log.append(
        {
            "key": key,
            "practice_type": practice_type,
            "mode": mode,
            "items": items,
            "rating": rating,
        }
    )
    save_progress()
    print(f"\nYou've completed {len(practice_log)} drill(s).")


def show_chord_notes(key: str, mode: str) -> None:
    chords = major_chords.get(key) if mode == "Major" else minor_chords.get(key)

    if not chords:
        print("Invalid key or mode.")
        return

    print(f"\nChord Notes in {key} {mode}:")
    for chord in chords:
        notes = chord_notes.get(chord)
        if notes:
            print(f"{chord}: {' '.join(notes)}")
        else:
            print(f"{chord}: Notes not found.")


def coach_mode() -> None:
    hard_entries = [entry for entry in practice_log if entry["rating"] == "Hard"]
    if not hard_entries:
        print("\nNo hard-rated drills to review. Keep practicing!")
        return

    last_hard = hard_entries[-1]
    print("\nCoach Mode: Reviewing your last hard-rated drill.")
    print(f"Practice this again: {last_hard['key']} {last_hard['mode']} {last_hard['practice_type']}")
    print("Material:")
    for item in last_hard["items"]:
        print(item)


def random_drill() -> None:
    drill_type = random.choice(["Scales", "Chords", "Progressions"])
    mode = random.choice(["Major", "Minor"])
    key = random.choice(list(major_scales.keys() if drill_type == "Scales" else major_chords.keys()))

    progression_name = None
    
    if drill_type == "Progressions":
        progression_name = random.choice(list(progressions.keys()))

    title, items = get_music_data(drill_type, key, mode, progression_name)
    if title and items:
        print("\nRandom Drill:")
        print_list(title, items)
        log_drill(key, drill_type, mode, items)
    else:
        print("Could not generate a random drill. Please try again.")


def quiz_mode() -> None:
    key = normalize_key(input("Quiz key: ").strip())
    mode = normalize_mode(input("Major or Minor: ").strip())
    quiz_type = input("Scales, Chords, or Progressions: ").strip().title()
    progression_name = None

    if quiz_type == "Progressions":
        progression_name = input("Enter the progression name (e.g., 2-5-1): ").strip()

    title, items = get_music_data(quiz_type, key, mode, progression_name)
    if not title or not items:
        print("Invalid quiz setup.")
        return

    answer = input(f"\nType the answer for {title}, separated by spaces: ").strip().split()
    if answer == items:
        print("Correct.")
        rating = "Easy"
    else:
        print("Not quite.")
        print_list("Correct answer was:", items)
        rating = "Hard"

    practice_log.append(
        {
            "key": key,
            "practice_type": f"Quiz {quiz_type}",
            "mode": mode,
            "items": items,
            "rating": rating,
        }
    )
    save_progress()


def ask_for_mode() -> str:
    while True:
        mode = normalize_mode(input("Major or Minor: ").strip())
        if mode:
            return mode
        print("Invalid mode. Enter Major or Minor.")


def main() -> None:
    global practice_log
    practice_log = load_progress()

    while True:
        practice_type = input(
            "Scales, Chords, Progressions, Chord Notes, Stats, Coach, Random, Quiz: "
        ).strip().title()

        if practice_type == "Stats":
            show_stats()
            continue

        if practice_type == "Coach":
            coach_mode()
            continue

        if practice_type == "Random":
            random_drill()
            continue

        if practice_type == "Quiz":
            quiz_mode()
            continue

        key = normalize_key(input("Enter the key (e.g., C, D#, Bb): ").strip())

        if practice_type == "Chord Notes":
            mode = ask_for_mode()
            show_chord_notes(key, mode)
            continue

        mode = ask_for_mode()
        progression_name = None

        if practice_type == "Progressions":
            progression_name = input("Enter the progression name (e.g., 2-5-1): ").strip()

        title, items = get_music_data(practice_type, key, mode, progression_name)
        if title and items:
            print_list(title, items)
            log_drill(key, practice_type, mode, items)
        else:
            print("Invalid input. Please try again.")
            continue

        hard_keys = [entry["key"] for entry in practice_log if entry["rating"] == "Hard"]
        if hard_keys:
            print(f"You're struggling with: {set(hard_keys)}")

        if input("\nPractice again? y/n: ").strip().lower() != "y":
            print("Practice session ended.")
            break


if __name__ == "__main__":
    main()
