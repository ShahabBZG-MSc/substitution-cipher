from pathlib import Path

def get_repo_root() -> Path:
    current = Path(__file__).resolve()
    for parent in current.parents:
        if (parent / ".git").exists() or (parent / "README.md").exists():
            return parent
    return Path(__file__).resolve().parents[2]  # fallback

REPO_ROOT = get_repo_root()
DATA_DIR = REPO_ROOT / "data"
DOCS_DIR = REPO_ROOT / "docs"
NOTEBOOKS_DIR = REPO_ROOT / "notebooks"
