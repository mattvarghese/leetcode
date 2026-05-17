#define PY_SSIZE_T_CLEAN
#include <Python.h>

// 1. The Core C Logic
long long pure_c_factorial(int n)
{
    if (n < 0)
        return 0;
    long long result = 1;
    for (int i = 1; i <= n; i++)
    {
        result *= i;
    }
    return result;
}

// 2. The Python Wrapper Function
// This function bridges Python arguments to C variables and returns a PyObject
static PyObject *method_factorial(PyObject *self, PyObject *args)
{
    int n;

    // "i" parses the Python arguments into a standard C integer (int)
    if (!PyArg_ParseTuple(args, "i", &n))
    {
        return NULL; // Raises a TypeError in Python
    }

    if (n < 0)
    {
        PyErr_SetString(PyExc_ValueError, "Factorial is not defined for negative numbers.");
        return NULL;
    }

    long long result = pure_c_factorial(n);

    // "K" packs a C unsigned long long/long long into a Python integer object
    return PyLong_FromLongLong(result);
}

// 3. The Method Registration Table
// Maps the string name you type in Python to the C function pointer
static PyMethodDef MathMethods[] = {
    {"factorial", method_factorial, METH_VARARGS, "Calculate the factorial of an integer."},
    {NULL, NULL, 0, NULL} // Sentinel element marking the end of the table
};

// 4. The Module Definition Structure
static struct PyModuleDef mathmodule = {
    PyModuleDef_HEAD_INIT,
    "custom_math",                                    // Name of the module when imported in Python
    "A custom C extension for fast math operations.", // Module documentation
    -1,                                               // Size of per-interpreter state (-1 = global state)
    MathMethods};

// 5. The Module Initialization Function
// This must be named PyInit_<modulename> and be explicitly exported
PyMODINIT_FUNC PyInit_custom_math(void)
{
    return PyModule_Create(&mathmodule);
}