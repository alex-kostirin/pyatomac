#include <Python.h>

#ifndef _PYCOMPATABILITY_H_
#define _PYCOMPATABILITY_H_

#if PY_MAJOR_VERSION >= 3

    #define MOD_DEF(m, name, doc, methods) \
        static struct PyModuleDef moduledef = { \
            PyModuleDef_HEAD_INIT, name, doc, -1, methods, }; \
        m = PyModule_Create(&moduledef);

     #define MOD_INIT(name) PyMODINIT_FUNC PyInit_##name(void)

     #define MOD_ERROR_VAL NULL

     #define MOD_SUCCESS_VAL(val) val

     #define STRING_TO_C_STRING(string) PyBytes_AsString(string)

#else
    #define MOD_DEF(m, name, doc, methods) \
        m = Py_InitModule3(name, methods, doc);

    #define MOD_INIT(name) PyMODINIT_FUNC init##name(void)

      #define MOD_ERROR_VAL

      #define MOD_SUCCESS_VAL(val)

      #define STRING_TO_C_STRING(string) PyString_AsString(string)

#endif

#endif //#ifndef _PYCOMPATABILITY_H_
