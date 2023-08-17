#include <Python.h>

/**
  * print_python_bytes - print basic info about python bytes objects.
  * @p: python object to use.
  */
void print_python_bytes(PyObject *p)
{
	int size;
	int i;
	int n;
	const char *str;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		size = (((PyVarObject *)(p))->ob_size);
		str = (((PyBytesObject *)(p))->ob_sval);
		n = (size < 10) ? size + 1 : 10;
		printf("  size: %d\n", size);
		printf("  trying string: %s\n", str);
		printf("  first %d bytes:", n);
		i = 0;
		while (i < 10 && i < size)
		{
			printf(" %02x", (unsigned char)str[i]);
			i++;
		}
		if (i < 10)
			printf(" 00\n");
		else
			printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

/**
  * print_python_list - print basic info about python lists.
  * @p: python object to use.
  */
void print_python_list(PyObject *p)
{
	int i;
	int size;
	int mem;
	const char *str;

	size = (((PyVarObject *)(p))->ob_size);
	if (PyList_Check(p))
	{
		printf("[*] Python list info\n");
		mem = ((PyListObject *)p)->allocated;
		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %d\n", mem);
		i = 0;
		while (i < size)
		{
			str = (((((PyListObject *)(p))->ob_item[i]))->ob_type)->tp_name;
			printf("Element %d: %s\n", i, str);
			if (!strcmp(str, "bytes"))
				print_python_bytes((((PyListObject *)(p))->ob_item[i]));
			i++;
		}
	}
}
