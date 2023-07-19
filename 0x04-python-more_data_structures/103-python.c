#include <Python.h>

/**
 * print_python_bytes - prints the Object information
 * @p: input object
 */

void print_python_bytes(PyObject *p)
{
	PyVarObject *obj;
	PyBytesObject *bytes;
	Py_ssize_t idx = 0, end;

	obj = (PyVarObject *)p;
	bytes = (PyBytesObject *)p;
	puts("[.] bytes object info");

	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		puts("  [ERROR] Invalid Bytes Object");
		return;
	}

	printf("  size: %li\n", obj->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	end = obj->ob_size + 1 >= 11 ? 10 : obj->ob_size + 1;
	printf("  first %li bytes: ", end);

	while (idx < end)
	{
		printf("%02hx", (unsigned char)bytes->ob_sval[idx]);
		if (idx < end - 1){
			putchar(' ');
	        }
        	idx++;
	}
	putchar('\n');
}


/**
 * print_python_list - print python list object info
 * @p: input python list object
 */

void print_python_list(PyObject *p)
{
	Py_ssize_t idx = 0;
	PyVarObject *obj;
	PyListObject *list;

	list = (PyListObject *)p;
	obj = (PyVarObject *)p;
    
	puts("[*] Python list info");
	printf("[*] Size of the Python List = %li\n", obj->ob_size);
	printf("[*] Allocated = %li\n", list->allocated);
	while (idx < obj->ob_size)
	{
		printf("Element %li: %s\n", idx, list->ob_item[idx]->ob_type->tp_name);

		if (strcmp(list->ob_item[idx]->ob_type->tp_name, "bytes") == 0){
			print_python_bytes(list->ob_item[idx]);
        	}
        	idx++;
	}
}
