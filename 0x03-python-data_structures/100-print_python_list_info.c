#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: input value
 * Return: none
 */

void print_python_list_info(PyObject *p)
{
	PyObject *entry;
	int idx = 0, count, space;

	space = ((PyListObject *)p)->allocated;
	count = Py_SIZE(p);

	printf("[*] Size of the Python List = %i\n", count);
	printf("[*] Allocated = %i\n", space);

	while (idx < count)
	{
		printf("Element %i: ", idx);
		entry = PyList_GetItem(p, idx);
		printf("%s\n", Py_TYPE(entry)->tp_name);

		idx++
	}
}
