typedef char BTDataType;
typedef struct BTNode
{
BTDataType x;
struct BTNode* left;
struct BTNode* right;
}BTNode;
BTNode* BuyNode(BTDataType x)
{
BTNode* temp = (BTNode*)malloc(sizeof(BTNode));
if (temp == NULL)
{
perror("BuyNode::malloc");
exit(-1);
}
temp->x = x;
temp->left = temp->right = NULL;
return temp;
}

template <typename T>
class min_heap
{
public:
inline size_t get_parent(size_t i)
{
try
{
size_t index;
if (i > 1)
index = floor(i / 2) - 1;
else if (i == 1)
index = 0;
 
assert(index < heap_size && index >= 0);
return index;
}
catch (const std::exception& e)
{
std::cout << e.what() << '\n';
throw;
}
}
 
inline size_t get_left(size_t i)
{
try
{
size_t index = 2 * i + 1;
assert(index >= 0 && index < heap_size);
return index;
}
catch (const std::exception& e)
{
std::cout << e.what() << '\n';
throw;
}
}
 
inline size_t get_right(size_t i)
{
try
{
size_t index = 2 * i + 2;
assert(index >= 0 && index < heap_size);
return index;
}
catch (const std::exception& e)
{
std::cout << e.what() << '\n';
throw;
}
}
 
void min_heapify(size_t i, int n)
{
assert(i < n + 1);
if (leaf_class(i, n) == 2)
{
size_t l = get_left(i);
size_t r = get_right(i);
size_t smallest;
 
if (l<n && data_array.at(l)<data_array.at(i))
{
smallest = l;
}
 
else
{
smallest = i;
}
 
if (r<n + 1 && data_array.at(r)<data_array.at(smallest))
{
smallest = r;
}
 
if (smallest != i)
{
T tmp;
 
tmp = data_array.at(smallest);
data_array.at(smallest) = data_array.at(i);
data_array.at(i) = tmp;
 
min_heapify(smallest, n);
}
}
else if (leaf_class(i, n) == 1)
{
size_t l = get_left(i);
if (data_array.at(l) < data_array.at(i))
{
T tmp = data_array.at(i);
 
data_array.at(i) = data_array.at(l);
data_array.at(l) = tmp;
}
}
}
size_t get_heap_size()
{
return heap_size;
}
int leaf_class(size_t i, int n)
{
if ((2 * i) < n && (2 * i + 1) < n)
return 2;
if ((2 * i) < n + 1 && (2 * i + 1) == n)
return 1;
else
return 0;
}
void build_min_heap()
{
for (int i = floor(heap_size / 2) + 1; i >= 0; i--)
min_heapify(i, get_heap_size() - 1);
}
 
void init_data(T* input, int n)
{
for (int i = 0; i < n; i++)
{
data_array.at(i) = *(input + i);
heap_size++;
}
}
 
void print_heap()
{
for (int i = 0; i < heap_size; i++)
cout << data_array.at(i) << endl;
}
 
array<T, 1024> data_array = { 0 };
size_t heap_size = 0;
 
private:
protected:
};
template<typename T>
class min_priority_queue :public min_heap<T>
{
public:
T minimum()
{
if ((this->heap_size) == 0)
assert("the max heap is empty!!!");
else
return this->data_array[0];
}
 
T heap_extract_min()
{
if (this->heap_size == 0)
assert("the queue is empty!!1");
else
{
T min = this->data_array.at(0);
this->data_array.at(0) = this->data_array.at(this->heap_size - 1);
this->heap_size--;
this->min_heapify(0, this->heap_size - 1);
return min;
}
}
 
void heap_increase_key(int i, T key)
{
assert(0 <= i && i < this->heap_size);
if (key > this->data_array.at(i))
assert("new key is larger than current key!");
else
{
this->data_array.at(i) = key;
while (i > 0 && this->data_array.at(this->get_parent(i)) > this->data_array.at(i))
{
std::swap(this->data_array.at(i), this->data_array.at(this->get_parent(i)));
i = this->get_parent(i);
}
}
}

