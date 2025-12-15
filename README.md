# Aplikacja do nauki teorii prawa jazdy

*[English version below](#driving-test-practice-application)*

---

Lokalna aplikacja webowa do nauki pytań z egzaminu teoretycznego na prawo jazdy (kategoria B). Zawiera pytania z czasomierzem, zapisywanie postępów, tryby nauki.

## Funkcje

- **Filtrowanie kategorii B**: Automatycznie filtruje pytania dla kategorii B
- **Czasomierz 40 sekund**: Zgodny z czasem na prawdziwym egzaminie, z wizualnymi ostrzeżeniami
- **Liczniki wyników**: Poprawne/błędne odpowiedzi, procent skuteczności, średni czas na pytanie
- **Zapis postępów**: Postępy zapisywane w localStorage, przetrwają odświeżenie przeglądarki
- **Flagowanie pytań**: Oznacz trudne pytania do późniejszej powtórki
- **Auto-flagowanie**: Automatyczne flagowanie pytań po 2 błędnych odpowiedziach (konfigurowalne)
- **Tryby nauki**: Losowy, oflagowane pytania, powtórka błędnych odpowiedzi
- **Tryb ciemny**: Przełączanie między jasnym a ciemnym motywem
- **Podsumowanie sesji**: Szczegółowe statystyki i przegląd błędnych odpowiedzi
- **Historia nauki**: Śledzenie postępów dziennych/tygodniowych z wykresami trendów
- **Skróty klawiszowe**: Pełna obsługa klawiatury dla szybszej nauki

## Wymagania

- Python 3.x (do lokalnego serwera HTTP)
- Nowoczesna przeglądarka (Chrome, Firefox, Edge, Safari)
- Baza pytań i pliki multimedialne (patrz Konfiguracja zawartości poniżej)

## Szybki start

### Windows
1. Wykonaj kroki z sekcji Konfiguracja zawartości (poniżej)
2. Kliknij dwukrotnie `start_app.bat`
3. Aplikacja otworzy się automatycznie w przeglądarce

### Ręczne uruchomienie
1. Wykonaj kroki z sekcji Konfiguracja zawartości (poniżej)
2. Otwórz terminal w folderze projektu
3. Uruchom: `python start_app.py`
4. Otwórz przeglądarkę na `http://localhost:8000`

## Konfiguracja zawartości

Ta aplikacja wymaga oficjalnej bazy pytań egzaminacyjnych i plików multimedialnych, które nie są dołączone do tego repozytorium z powodu ograniczeń licencyjnych.

### Krok 1: Pobierz oficjalne materiały

1. Odwiedź oficjalną stronę Ministerstwa Infrastruktury:
   https://www.gov.pl/web/infrastruktura/prawo-jazdy
2. Przewiń do sekcji "Pytania egzaminacyjne na prawo jazdy"
3. Pobierz plik Excel (`pytania_egzaminacyjne_na_kierowce_2025.xlsx`)

### Krok 2: Przygotuj bazę pytań

1. Otwórz pobrany plik Excel
2. Eksportuj/Zapisz jako CSV z kodowaniem UTF-8
3. Nazwij plik `pytania.csv` i umieść w głównym folderze projektu

### Krok 3: Przygotuj pliki multimedialne

1. Pobierz pliki multimedialne (obrazy i filmy) z oficjalnego źródła
2. Utwórz folder `wizualizacje/` w głównym folderze projektu
3. Umieść wszystkie pliki multimedialne w tym folderze
4. Jeśli filmy nie odtwarzają się w przeglądarce, upewnij się że są w formacie `.mp4` (zalecany kodek H.264)

### Struktura plików po konfiguracji

```
prawko/
  index.html
  start_app.py
  start_app.bat
  README.md
  LICENSE
  pytania.csv          <- Dodajesz sam
  wizualizacje/        <- Dodajesz ten folder
    obraz1.jpg
    film1.mp4
    ...
```

## Użytkowanie

### Skróty klawiszowe

| Klawisz | Funkcja |
|---------|---------|
| `1` `2` `3` | Wybierz odpowiedź A/B/C |
| `T` `N` | Wybierz Tak/Nie |
| `Enter` / `Spacja` | Sprawdź odpowiedź / Następne pytanie |
| `Backspace` | Poprzednie pytanie |
| `P` | Pauza/wznów czasomierz |
| `F` | Oznacz flagą |
| `V` | Odtwórz/zatrzymaj wideo |

### Przyciski

| Przycisk | Funkcja |
|----------|---------|
| Sprawdź | Sprawdź odpowiedź |
| Następne | Przejdź do następnego pytania |
| Poprzednie | Wróć do poprzedniego pytania |
| Historia | Pokaż historię nauki i trendy |
| Ikona pauzy | Wstrzymaj/wznów czasomierz |
| Ikona flagi | Oznacz pytanie do powtórki |
| Ikona motywu | Przełącz tryb jasny/ciemny |

### Tryby nauki

- **Tryb normalny**: Losowe pytania z kategorii B
- **Tryb oflagowanych**: Tylko pytania które oznaczyłeś flagą
- **Tryb błędnych odpowiedzi**: Powtórka pytań na które odpowiedziałeś błędnie

### Zarządzanie sesją

- **Zakończ sesję i pokaż statystyki**: Wyświetl podsumowanie sesji ze szczegółami błędnych odpowiedzi
- **Zresetuj sesję**: Wyczyść postępy i zacznij od nowa

## Konfiguracja

### Czas na pytanie

Edytuj `index.html` i zmień stałą:
```javascript
const DEFAULT_TIME = 40; // sekundy
```

### Auto-flagowanie

Pytania są automatycznie flagowane po określonej liczbie błędnych odpowiedzi. Możesz to skonfigurować w `index.html`:
```javascript
const AUTO_FLAG_WRONG = true;  // true = włączone, false = wyłączone
const AUTO_FLAG_THRESHOLD = 2; // liczba błędów przed auto-flagowaniem
```

## Szczegóły techniczne

- **Serwer**: Wbudowany serwer HTTP Pythona (port 8000)
- **Auto-wyłączenie**: Serwer zatrzymuje się po 3 godzinach
- **Przechowywanie danych**: localStorage przeglądarki:
  - `prawko_session` - postępy bieżącej sesji
  - `prawko_flags` - oflagowane pytania
  - `prawko_wrong_counts` - liczniki błędów (do auto-flagowania)
  - `prawko_history` - historia nauki (ostatnie 30 dni)
  - `prawko_theme` - preferencja motywu
- **Kodowanie**: UTF-8 dla poprawnej obsługi polskich znaków

## Rozwiązywanie problemów

### "pytania.csv not found"
Upewnij się, że wykonałeś kroki z sekcji Konfiguracja zawartości.

### Filmy się nie odtwarzają
- Sprawdź czy pliki są w formacie `.mp4`
- Sprawdź czy nazwy plików w CSV odpowiadają rzeczywistym plikom
- Spróbuj przekonwertować filmy do formatu MP4 H.264

### "Port 8000 already in use"
Zamknij inne aplikacje używające tego portu lub zmień PORT w `start_app.py`.

### Polskie znaki wyświetlają się niepoprawnie
Upewnij się, że `pytania.csv` jest zapisany z kodowaniem UTF-8.

## Licencja

Zobacz plik [LICENSE](LICENSE).

- **Kod aplikacji** (HTML, CSS, JavaScript, Python): Licencja MIT
- **Baza pytań i pliki multimedialne**: Oddzielna licencja Ministerstwa Infrastruktury (CC BY-NC-ND 3.0 PL)

## Źródło materiałów

Baza pytań egzaminacyjnych i powiązane pliki multimedialne są publikowane przez Ministerstwo Infrastruktury na licencji Creative Commons BY-NC-ND 3.0 PL.

Źródło: https://www.gov.pl/web/infrastruktura/prawo-jazdy

Materiały te są udostępnione wyłącznie do celów edukacyjnych, niekomercyjnych.

---

# Driving Test Practice Application

A local, browser-based application for practicing Polish driving theory exam questions (category B). Features timed questions, progress tracking, session persistence, and study modes.

## Features

- **Category B Filtering**: Automatically filters questions relevant to category B license
- **40-Second Timer**: Matches real exam timing with visual warnings
- **Score Tracking**: Correct/incorrect counts, accuracy percentage, average time per question
- **Session Persistence**: Progress saved to localStorage, survives browser refresh
- **Question Flagging**: Mark difficult questions for focused review later
- **Auto-Flagging**: Automatically flags questions after 2 wrong answers (configurable)
- **Study Modes**: Normal random mode, flagged questions mode, wrong answers review
- **Dark Mode**: Toggle between light and dark themes
- **Session Summary**: End session to see detailed statistics and review wrong answers
- **Learning History**: Track daily/weekly performance with trend charts
- **Keyboard Shortcuts**: Full keyboard navigation for faster practice

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

### Keyboard Shortcuts

| Key | Function |
|-----|----------|
| `1` `2` `3` | Select answer A/B/C |
| `T` `N` | Select Yes/No (Tak/Nie) |
| `Enter` / `Space` | Check answer / Next question |
| `Backspace` | Previous question |
| `P` | Pause/resume timer |
| `F` | Toggle flag |
| `V` | Play/pause video |

### Controls

| Button | Function |
|--------|----------|
| Sprawdź | Check your answer |
| Następne | Go to next question |
| Poprzednie | Go back to previous question |
| Historia | Show learning history and trends |
| Pause icon | Pause/resume timer |
| Flag icon | Mark question for later review |
| Theme icon | Toggle dark/light mode |

### Study Modes

- **Normal Mode**: Random questions from category B
- **Flagged Mode**: Practice only questions you've flagged
- **Wrong Answers Mode**: Review questions you answered incorrectly

### Session Management

- **Zakończ sesję i pokaż statystyki**: View session summary with wrong answer details
- **Zresetuj sesję**: Clear all progress and start fresh

## Configuration

### Timer Duration

Edit `index.html` and change the constant:
```javascript
const DEFAULT_TIME = 40; // seconds
```

### Auto-Flagging

Questions are automatically flagged after a certain number of wrong answers. Configure in `index.html`:
```javascript
const AUTO_FLAG_WRONG = true;  // true = enabled, false = disabled
const AUTO_FLAG_THRESHOLD = 2; // wrong attempts before auto-flag
```

## Technical Details

- **Server**: Python's built-in HTTP server (port 8000)
- **Auto-shutdown**: Server stops after 3 hours
- **Data Storage**: Browser localStorage with multiple keys:
  - `prawko_session` - current session progress
  - `prawko_flags` - flagged questions
  - `prawko_wrong_counts` - wrong answer counts (for auto-flagging)
  - `prawko_history` - learning history (last 30 days)
  - `prawko_theme` - theme preference
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
