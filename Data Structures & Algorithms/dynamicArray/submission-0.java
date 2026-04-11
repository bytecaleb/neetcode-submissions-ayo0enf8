class DynamicArray {
    private int[] array;
    private int size = 0;
    private int capacity;

    public DynamicArray(int capacity) {
        this.capacity = capacity;
        this.size = size;
        this.array = new int[this.capacity];
        
    }

    public int get(int i) {
        return this.array[i];
    }

    public void set(int i, int n) {
        this.array[i] = n;
    }

    public void pushback(int n) {
        if (size == capacity){
            resize();
        }

        this.array[size] = n;
        size ++;
    }

    public int popback() {
        size --;
        return this.array[size];
    }

    private void resize() {
        this.capacity *= 2;

        int[] new_arr = new int[capacity];

        for (int i = 0; i < size; i ++)
        {
            new_arr[i] = this.array[i];
        }

        this.array = new_arr;

    }

    public int getSize() {
        return this.size;
    }

    public int getCapacity() {
        return this.capacity;
    }
}
