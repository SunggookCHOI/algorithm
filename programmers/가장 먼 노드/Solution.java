import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;

class Solution {
	ArrayList<int[]> arr = null;
    public int solution(int n, int[][] edge) {
        int answer = 0;
        int[] distance = new int[n+1];
        for(int i=2;i<=n;i++) {
        	distance[i]=1111111111;
        }
        ArrayList<Integer> queue = new ArrayList<>();
        arr = new ArrayList<int[]>(Arrays.asList(edge));
        queue.add(1);
        while(!queue.isEmpty()) {
        	int target = queue.get(0);
        	queue.remove(0);
        	ArrayList<Integer> neighbor = findNeighbor(target);
        	int temp = distance[target]+1;
        	for(int nei:neighbor) {
        		if(distance[nei]>temp) {
        			distance[nei]=temp;
        			queue.add(nei);
        		}
        	}
        }
        return getAnswer(distance, n);
    }
    public ArrayList<Integer> findNeighbor(int target){
    	ArrayList<Integer> answer = new ArrayList<>();
    	Iterator<int[]> tempArr = arr.iterator();
    	while(tempArr.hasNext()) {
    		int[] a = tempArr.next();
    		if(a[0]==target) {
    			answer.add(a[1]);
    			tempArr.remove();
    		}else if(a[1]==target){
    			answer.add(a[0]);
    			tempArr.remove();
    		}
    	}
    	return answer;
    }
    
    public int getAnswer(int[] distance, int n) {
    	int max = 0;
    	int answer = 0;
    	for(int i=2; i<=n; i++) {
    		if(distance[i]>max) {
    			max = distance[i];
    			answer = 1;
    		}else if(distance[i]==max) {
    			answer++;
    		}
    	}
    	return answer;
    }
}
