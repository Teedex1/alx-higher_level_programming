#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
#include <time.h>
/**
 * print_python_list_info - function
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	int elem;
	const char *type_name;

	printf("[*] Size of the python List = %ld\n", Py_SIZE(p));
	printf("[*] Allocated = %ld\n",((PyListObject *)p)->allocated);

	for (elem = 0; elem < Py_SIZE(p); elem++)
	{
		PyObject *item = PyList_GetItem(p, elem);
		type_name = Py_TYPE(item)->tp_name;

		printf("Element %d: %s\n", elem, type_name);
	}
}
