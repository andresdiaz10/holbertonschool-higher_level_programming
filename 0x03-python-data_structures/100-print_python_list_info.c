#include <Python.h>
/**
 * print_python_list_info - a.
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
	PyObject *ob;
	int memo;
	int index;
	Py_ssize_t size;

	memo = ((PyListObject *)p)->allocated;
	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %d\n", memo);
	for (index = 0; index < size; index++)
	{
		printf("Element %d: ", index);
		ob = PyList_GetItem(p, index);
		printf("%s\n", Py_TYPE(ob)->tp_name);
	}
}
