class MedianFinder {

    private final PriorityQueue<Integer> left;
    private final PriorityQueue<Integer> right;

    public MedianFinder() {
        this.left = new PriorityQueue<>((a, b) -> b - a);
        this.right = new PriorityQueue<>();
    }
    
    public void addNum(int num) {
        left.add(num);
        right.add(left.poll());
        if (right.size() > left.size()) {
            left.add(right.poll());
        } 
        if (left.size() > right.size() + 1) {
            right.add(left.poll());
        }
    }
    
    public double findMedian() {
        if (left.size() > right.size()) return (double) left.peek();

        return (left.peek() + right.peek()) / 2.0;
        
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */