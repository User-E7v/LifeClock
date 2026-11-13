# LifeClock

**LifeClock** (internally titled *Age in Days Calculator*) is a command-line utility written in Python that computes precise chronological age metrics and generates a comprehensive personal profile based on a user's birth date. Beyond standard calendar calculations, the application evaluates astrological classifications, developmental life stages, physiological estimations, and exports structured text reports.

---

## Table of Contents

1. [Core Capabilities](#core-capabilities)
2. [Prerequisites and Dependencies](#prerequisites-and-dependencies)
3. [Installation and Setup](#installation-and-setup)
4. [Usage and Execution Flow](#usage-and-execution-flow)
5. [Calculation Methodology and Logic](#calculation-methodology-and-logic)
6. [Report Export Specification](#report-export-specification)
7. [Code Architecture](#code-architecture)
8. [Error Handling](#error-handling)

---

## Core Capabilities

* **High-Precision Chronological Breakdown:** Utilizes calendar-aware delta calculations to determine exact age in years, months, and days, alongside cumulative totals in months, weeks, days, hours, minutes, and seconds.
* **Birthday Countdown Engine:** Dynamically calculates the exact number of days remaining until the user's next birthday, triggering special terminal notifications if the event is within 7 days or occurring on the current date.
* **Astrological and Seasonal Profiling:**
  * **Western Zodiac:** Maps the birth month and day to the corresponding tropical astrological sign.
  * **Chinese Zodiac:** Computes the 12-year cyclical animal sign based on the birth year.
  * **Meteorological Season:** Identifies the Northern Hemisphere season corresponding to the birth month.
  * **Day of Week:** Determines the exact day of the week on which the user was born.
* **Developmental Classification and Guidance:** Categorizes the user into one of nine distinct developmental life stages (ranging from *Infant* to *Elder*) and provides age-appropriate wellness recommendations and dynamic ASCII banners.
* **Physiological Estimations and Wisdom:** Generates randomized biological estimates (e.g., total heartbeats, breaths taken, hours spent sleeping) and curates philosophical quotes.
* **Automated File Reporting:** Exports a formatted `.txt` summary report timestamped with the user's birth date for offline archiving.

---

## Prerequisites and Dependencies

* **Python Runtime:** Python 3.6 or higher.
* **Third-Party Packages:**
  * `python-dateutil`: Required for `relativedelta` to accurately handle leap years and varying month lengths during age calculation.
* **Standard Library Modules:** `datetime`, `os`, `random`.

---

## Installation and Setup

1. **Verify Python Installation:**
   Ensure Python 3 is installed and accessible from your system path:
   ```bash
   python --version
   ```

2. **Install Required Dependencies:**
   Install the `python-dateutil` library using `pip`:
   ```bash
   pip install python-dateutil
   ```

3. **Run the Application:**
   Navigate to the directory containing `LifeClock.py` and execute the script:
   ```bash
   python LifeClock.py
   ```

---

## Usage and Execution Flow

1. **Initialization:** Upon execution, the terminal screen is cleared (`cls` on Windows, `clear` on Unix-like systems) and the application header is displayed.
2. **Input Phase:** The user is prompted sequentially to enter:
   * Birth Year (`YYYY`)
   * Birth Month (`1-12`)
   * Birth Day (`1-31`)
3. **Processing and Display:** The screen refreshes to render an age-tiered ASCII art banner followed by categorized sections detailing chronological age, countdown metrics, astrological data, physiological trivia, health advice, and a philosophical quote.
4. **Export Prompt:** At the conclusion of the display, the user is prompted (`Save results to file? (y/n):`). Entering `y` generates a local text report.

---

## Calculation Methodology and Logic

### Chronological Metrics
* **Exact Age:** Calculated via `dateutil.relativedelta.relativedelta(today, birth_date)`, ensuring calendar-accurate year, month, and day remainders.
* **Cumulative Totals:** Derived from the exact day delta (`(today - birth_date).days`):
  * $\text{Total Weeks} = \lfloor \text{Total Days} / 7 \rfloor$
  * $\text{Total Hours} = \text{Total Days} \times 24$
  * $\text{Total Minutes} = \text{Total Hours} \times 60$
  * $\text{Total Seconds} = \text{Total Minutes} \times 60$

### Classification Matrices

#### Life Stage Tiers
| Age Range (Years) | Assigned Classification | ASCII Banner Tier |
| :--- | :--- | :--- |
| `< 2` | Infant | Young Star (`< 10`) |
| `2 - 3` | Toddler | Young Star (`< 10`) |
| `4 - 5` | Preschooler | Young Star (`< 10`) |
| `6 - 11` | Child | Young Star (`< 10`) / Golden Age (`10 - 11`) |
| `12 - 17` | Teenager | Golden Age (`10 - 19`) |
| `18 - 39` | Young Adult | Golden Age (`18 - 19`) / Prime Time (`20 - 39`) |
| `40 - 59` | Middle Age | Sage Age (`40 - 59`) |
| `60 - 79` | Senior | Legendary (`60+`) |
| `80+` | Elder | Legendary (`60+`) |

#### Chinese Zodiac Formula
The 12-year cycle is calculated programmatically using modular arithmetic anchored to the start of the cycle:
$$\text{Index} = (\text{Birth Year} - 4) \bmod 12$$

#### Physiological Estimation Constants
The trivia engine applies standard daily averages across the user's total lived days:
* **Sleep:** $8\text{ hours/day}$
* **Heart Rate:** $70\text{ beats/minute}$
* **Respiration Rate:** $20\text{ breaths/minute}$
* **Blinking Rate:** $20\text{ blinks/minute}$

---

## Report Export Specification

When the export option is confirmed, the script writes a plain-text file to the current working directory using the naming convention:

```text
age_report_YYYYMMDD.txt
```

### Sample Output Structure
```text
AGE IN DAYS CALCULATOR - DETAILED REPORT
==================================================

BIRTH DATE: January 15, 1995
WEEKDAY BORN: Sunday

YEARS: 31
MONTHS: 9
DAYS: 29
TOTAL DAYS: 11625
TOTAL WEEKS: 1660
TOTAL MONTHS: 381
TOTAL HOURS: 279000
TOTAL MINUTES: 16740000
TOTAL SECONDS: 1004400000
DAYS UNTIL BIRTHDAY: 63
NEXT BIRTHDAY: January 15, 2027

ZODIAC: Capricorn
CHINESE ZODIAC: Pig
SEASON OF BIRTH: Winter
LIFE STAGE: Young Adult

FUN FACT: Your heart has beaten about 1,171,800,000 times
HEALTH TIP: Maintain work-life balance and build healthy habits
WISDOM: Life is like riding a bicycle, to keep balance you must keep moving
```

---

## Code Architecture

The script follows a procedural, single-responsibility design pattern:

* **Input & Validation Layer (`get_birth_date`):** Enforces integer parsing, validates calendar legality (e.g., rejecting February 30), and prevents future dates.
* **Computation Engine (`calculate_age_details`):** Centralizes all date-math operations and returns a unified dictionary of chronological metrics.
* **Domain Analyzers (`get_zodiac_sign`, `get_chinese_zodiac`, `get_weekday_name`, `get_season`, `get_life_stage`):** Pure functions mapping temporal inputs to categorical string outputs.
* **Content Generators (`get_health_tips`, `get_fun_fact`, `generate_wisdom`):** Rule-based and randomized string providers for user engagement.
* **Presentation & I/O Layer (`display_ascii_art`, `print_header`, `main`):** Manages terminal formatting, screen clearing, user prompts, and file serialization.

---

## Error Handling

* **Invalid Date Inputs (`ValueError`):** Non-numeric strings or impossible calendar dates are caught within an input loop, prompting the user to re-enter values without crashing the application.
* **Future Date Prevention:** Explicitly compares input against `datetime.date.today()` to ensure logical consistency.
* **File System Exceptions (`IOError`):** Wraps the report generation block in a `try-except` structure to handle read-only directories or permission restrictions gracefully.
* **Graceful Termination (`KeyboardInterrupt`):** Intercepts `Ctrl+C` signals at the entry point to exit cleanly with a status message rather than a stack trace.