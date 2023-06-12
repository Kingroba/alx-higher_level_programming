include <Python.h>

void print_python_list_info(PyObject *p)
{

/**
 * Get the size and allocated size of the list.
 */
	int size = Py_SIZE(p);
	int alloc = ((PyListObject *)p)->allocated;

/** Print the size and allocated size of the list.
 */
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

/**Iterate over the list and print the type of each element.
 */
	for (int i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

/**Get the element at the current index.
 */
	PyObject *obj = PyList_GetItem(p, i);

/**Print the type of the element.
 * */
	printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
