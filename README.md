# Driving Test Practice Application

A local, browser-based application for practicing Polish driving theory exam questions (category B). Features timed questions, progress tracking, session persistence, and study modes.

## Features

- **Category B Filtering**: Automatically filters questions relevant to category B license
- **40-Second Timer**: Matches real exam timing with visual warnings
- **Score Tracking**: Correct/incorrect counts, accuracy percentage, average time per question
- **Session Persistence**: Progress saved to localStorage, survives browser refresh
- **Question Flagging**: Mark difficult questions for focused review later
- **Study Modes**: Normal random mode, flagged questions mode, wrong answers review
- **Dark Mode**: Toggle between light and dark themes
- **Session Summary**: End session to see detailed statistics and review wrong answers

## Requirements

- Python 3.x (for local HTTP server)
- Modern web browser (Chrome, Firefox, Edge, Safari)
- Question database and media files (see Content Setup below)

## Quick Start

### Windows
1. Complete the Content Setup (below)
2. Double-click `start_app.bat`
3. Application opens automatically in your browser

### Manual Start
1. Complete the Content Setup (below)
2. Open terminal in the project folder
3. Run: `python start_app.py`
4. Open browser to `http://localhost:8000`

## Content Setup

This application requires the official Polish driving exam question database and media files, which are not included in this repository due to licensing restrictions.

### Step 1: Download Official Materials

1. Visit the official Ministry of Infrastructure page:
   https://www.gov.pl/web/infrastruktura/prawo-jazdy
2. Scroll to "Pytania egzaminacyjne na prawo jazdy"
3. Download the Excel file (`pytania_egzaminacyjne_na_kierowce_2025.xlsx`)

### Step 2: Prepare Question Database

1. Open the downloaded Excel file
2. Export/Save As CSV format with UTF-8 encoding
3. Name it `pytania.csv` and place in the project root folder

### Step 3: Prepare Media Files

1. Download media files (images and videos) from the official source
2. Create a `wizualizacje/` folder in the project root
3. Place all media files in this folder
4. If videos don't play in browser, ensure they are in `.mp4` format (H.264 codec recommended)

### File Structure After Setup

```
prawko/
  index.html
  start_app.py
  start_app.bat
  README.md
  LICENSE
  pytania.csv          <- You add this
  wizualizacje/        <- You add this folder
    image1.jpg
    video1.mp4
    ...
```

## Usage

### Controls

| Button | Function |
|--------|----------|
| Sprawdz | Check your answer |
| Nastepne | Go to next question |
| Poprzednie | Go back to previous question |
| Pause icon | Pause/resume timer |
| Flag icon | Mark question for later review |
| Theme icon | Toggle dark/light mode |

### Study Modes

- **Normal Mode**: Random questions from category B
- **Flagged Mode**: Practice only questions you've flagged
- **Wrong Answers Mode**: Review questions you answered incorrectly

### Session Management

- **Zakoncz sesje i pokaz statystyki**: View session summary with wrong answer details
- **Zresetuj sesje**: Clear all progress and start fresh

## Configuration

### Timer Duration

Edit `index.html` and change the constant:
```javascript
const DEFAULT_TIME = 40; // seconds
```

### Target Category

Edit `index.html` to change the license category filter:
```javascript
const TARGET_CATEGORY = 'B'; // Change to A, C, D, etc.
```

## Technical Details

- **Server**: Python's built-in HTTP server (port 8000)
- **Auto-shutdown**: Server stops after 3 hours
- **Storage**: Uses browser localStorage for session persistence
- **Encoding**: UTF-8 for proper Polish character support

## Troubleshooting

### "pytania.csv not found"
Ensure you've completed the Content Setup steps above.

### Videos not playing
- Verify files are in `.mp4` format
- Check that filenames in CSV match actual files exactly
- Try converting videos to H.264 MP4 format

### "Port 8000 already in use"
Close other applications using the port or modify PORT in `start_app.py`.

### Polish characters display incorrectly
Ensure `pytania.csv` is saved with UTF-8 encoding.

## License

See [LICENSE](LICENSE) file for details.

- **Application code** (HTML, CSS, JavaScript, Python): MIT License
- **Question database and media files**: Separate license from Polish Ministry of Infrastructure

## Content Attribution

The driving exam question database and associated media files are published by the Polish Ministry of Infrastructure under the Creative Commons BY-NC-ND 3.0 PL license.

Source: https://www.gov.pl/web/infrastruktura/prawo-jazdy

These materials are provided for educational, non-commercial use only.
