# Music Theory Practice Suite

An interactive Python command-line application designed to help musicians practice music theory through guided drills, quizzes, randomized exercises, and progress tracking.

## Features

- Major and minor scale drills
- Major and minor diatonic chord practice
- Chord-note lookup
- Common progression drills:
  - 2-5-1
  - 7-3-6
  - 1-4-5
  - 6-2-5-1
- Quiz mode
- Random practice mode
- Coach mode for reviewing hard-rated drills
- Practice statistics
- JSON-based practice history
- Input normalization and validation

## Technologies Used

- Python
- JSON
- Python standard library modules:
  - `random`
  - `typing`

## How to Run

1. Download or clone this repository.
2. Open the project folder in Visual Studio Code or a terminal.
3. Run the following command:

```bash
python3 music_theory_practice_suite.py
```

On some Windows systems, use:

```bash
python music_theory_practice_suite.py
```

The application automatically creates a `practice_log.json` file after practice data is recorded.

## How It Works

The user selects a musical key and practice mode. Depending on the selected mode, the application can display scales, chords, chord notes, or progressions; generate a randomized drill; administer a quiz; or review previously difficult material.

After completing a guided drill, the user rates it as Easy, Medium, or Hard. The application saves this information and uses it to display practice statistics and recommend material for review.

## Project Purpose

I created this project to combine my interests in computer science and music while solving a personal problem: organizing structured music-theory practice. The application helps musicians review important concepts, identify difficult keys, and track completed drills across multiple sessions.

## Current Scope

The current version is a command-line application that includes major and natural minor scales, diatonic chords, triad note lookup, four common chord progressions, practice logging, quizzes, and basic progress analysis.

## Future Improvements

- Graphical user interface
- Seventh and extended chords
- Improved progress analytics
- Practice streak tracking
- MIDI keyboard integration
- More personalized practice recommendations

## Author

Chaise Hubbard  
Computer Science Student at Alabama Agricultural and Mechanical University

