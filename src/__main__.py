import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from rubric_autofill import *

if __name__ == "__main__":
    # Entrypoint for running as a module
    import rubric_autofill
