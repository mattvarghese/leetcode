# Custom C Extension for Python (Factorial Implementation)

This project contains a high-performance C extension module for Python that optimizes mathematical operations. It demonstrates how to wrap low-level C logic using the CPython C-API, compile it as a shared binary, and import it directly into a Python runtime environment.

## Project Structure

* `mathmodule.c` - The core C source code containing the factorial logic, Python argument parsing, and module registration.
* `setup.py` - The compilation metadata script using `setuptools` to drive the compiler.
* `build.sh` - An un-hardcoded bash automation script to manage dependencies and trigger the extension build pipeline.
* `main.py` - A Python driver script used to verify execution boundaries and error-handling mechanisms.

---

## Prerequisites & System Setup

Before building the C extension, your local environment requires the structural C development headers for Python and an isolated Python runtime environment.

### 1. Install System Development Headers
On Debian/Ubuntu-based systems, standard runtime environments strip out the requisite compilation headers (`Python.h`). Install them by executing the following terminal command (this build matches Python 3.13):

```bash
sudo apt update
sudo apt install python3-dev python3-setuptools
```

### 2. Configure Your IDE (VS Code IntelliSense)
To resolve linting red squiggles under `#include <Python.h>` and activate full code autocompletion:
1. Open the Command Palette (`Ctrl + Shift + P`).
2. Type and select **C/C++: Edit Configurations (UI)**.
3. Locate the **Include path** matrix and append the literal folder path to your active headers:
   ```text
   /usr/include/python3.13
   ```
*(Alternatively, you can manually add this string to the `includePath` array inside your `.vscode/c_cpp_properties.json` file).*

---

## Getting Started

Follow these steps to initialize your isolated runtime, install compilation dependencies, and run the compilation matrix.

### 1. Environment Isolation (Virtual Environment)
Isolate your workspace dependencies from global system space using a virtual environment:

```bash
# Create the virtual environment
python3 -m venv .venv

# Activate the virtual environment
source .venv/bin/activate
```

### 2. Dependency Resolution
With the `.venv` activated, install or upgrade `setuptools` to ensure the compilation engine is accessible to your environment:

```bash
pip install --upgrade pip setuptools
```

### 3. Compilation
Run the automated build script to execute the `setuptools` extension build layout in place:

```bash
# Ensure execution permissions are granted to the script
chmod +x build.sh

# Run the build execution pass
./build.sh
```

This compilation step runs a localized GCC compilation pass, linking your `mathmodule.c` logic into a shared binary object file (a `.so` file on Linux/macOS or a `.pyd` file on Windows) right inside your root workspace directory.

### 4. Verification Pass
Execute the Python driver script to verify that Python loads the shared binary library cleanly and maps the execution boundaries as expected:

```bash
python3 main.py
```

---

## Technical Details: The Python C-API Layer

The translation boundary between Python's dynamic runtime and C's native performance maps across these key architectural pillars inside `mathmodule.c`:

* **Argument Unpacking:** The function utilizes `PyArg_ParseTuple(args, "i", &n)` where the `"i"` formatting token acts as a structural gate, dynamically validating and transforming a Python integer object into a flat C raw `int`.
* **Result Packaging:** After computing the factorial loop using an independent `long long` C vector, the result is marshalled back into the Python ecosystem via `PyLong_FromLongLong(result)`.
* **Module Linkage:** Initialization hooks are handled by the explicit export macro `PyMODINIT_FUNC PyInit_custom_math(void)`, which calls `PyModule_Create(&mathmodule)` to safely bind the C function table to the Python namespace wrapper.