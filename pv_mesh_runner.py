import subprocess
import os

BASE_DIR = os.path.expanduser("~/PrivateVault.ai")

def run_mesh_decision():
    try:
        result = subprocess.run(
            ["python", "coordination/mesh/demo_full_pipeline.py"],
            cwd=BASE_DIR,
            capture_output=True,
            text=True
        )

        output = result.stdout.strip()
        error = result.stderr.strip()

        # Debug (important)
        if not output:
            output = f"[NO STDOUT]\n{error}"

        if "BLOCK" in output:
            return False, output
        elif "APPROVE" in output:
            return True, output

        return False, output

    except Exception as e:
        return False, f"Runner error: {str(e)}"
