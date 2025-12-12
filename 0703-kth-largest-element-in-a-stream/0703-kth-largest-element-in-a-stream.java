class KthLargest {

    private static PriorityQueue<Integer> q;
    private static int K;

    public KthLargest(int k, int[] nums) {

        this.q = new PriorityQueue<>();
        this.K = k;

        for (int num: nums) {
            if (q.size() < k) q.add(num);
            else {
                if (num > q.peek()){
                    q.poll();
                    q.add(num);
                }
            }
        }     
    }
    
    public int add(int val) {
        if (q.size() < K) q.add(val);
        else if (val > q.peek()){
            q.add(val);
            q.poll();
        }      
        return q.peek();
        
        
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */