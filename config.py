from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

DAILY_LOGS_DIR = PROJECT_ROOT / "logs" 
DATASETS_DIR = PROJECT_ROOT / "archive"

def ensure_dirs():
    dirs = [
        DAILY_LOGS_DIR,
        DATASETS_DIR,
    ]

    for d in dirs:
        try:
            d.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print(f"Could not create directory {d}: {e}")

if __name__ == "__main__":
    ensure_dirs()
    print("All required directories ensured.")