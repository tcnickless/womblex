import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    abs_working_path = os.path.abspath(working_directory)
    target_file = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_file.startswith(abs_working_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        cp = subprocess.run(
            ["python", target_file, *args],
            capture_output=True,
            cwd=abs_working_path,
            text=True,
            timeout=30,
        )

        out = []
        if cp.stdout:
            out.append(f"STDOUT: {cp.stdout.strip()}")
        if cp.stderr:
            out.append(f"STDERR: {cp.stderr.strip()}")
        if cp.returncode != 0:
            out.append(f"Process exited with code {cp.returncode}")
        if not out:
            return "No output produced."
        return "\n".join(out)
    except Exception as e:
        return f"Error: executing Python file: {e}"

    