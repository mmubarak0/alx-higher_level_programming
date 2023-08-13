#include <Python.h>
#include <stddef.h>

/**
 * print_python_list_info - print basic info about python lists.
 * @p: python list object.
 *
 */
void print_python_list_info(PyObject *p)
{
	int i;
	int size;
	int mem;

	size = Py_SIZE(p);
	if (PyList_Check(p))
	{
		mem = ((PyListObject *)p)->allocated;
		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %d\n", mem);
		i = 0;
		while (i < size)
		{
			printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
			i++;
		}
	}
}
