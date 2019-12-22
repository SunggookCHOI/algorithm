import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

//코스트가 작은것 부터 이어 붙인다
class Solution {
    public static int solution(int n, int[][] costs) {
        int answer = 0;
        ArrayList<int[]> costs2 = new ArrayList<>();
        ArrayList<Integer> giant = new ArrayList<>();
        
        
        for(int[] e : costs) {
        	costs2.add(e);
        }
        
        Comparator<int[]> solutionComparator = new Comparator<int[]>() {
    		public int compare(int[] a, int[] b) {

    			if(a[2]>b[2]) {
    				return 1;
    			}else if(a[2]<b[2]) {
    				return -1;
    			}else {
    				return 0;
    			}
    		}
    	};
        
    	Collections.sort(costs2, solutionComparator);
    	giant.add(costs2.get(0)[0]);
    	giant.add(costs2.get(0)[1]);
    	answer+=costs2.get(0)[2];
    	while(giant.size()<n) {
    		for(int[] e : costs2) {
    			if(!giant.contains(e[0]) && giant.contains(e[1])) {
    				giant.add(e[0]);
    				costs2.remove(costs2.indexOf(e));
    				answer+=e[2];
    				break;
    			}else if(giant.contains(e[0]) && !giant.contains(e[1])){
    				giant.add(e[1]);
    				costs2.remove(costs2.indexOf(e));
    				answer+=e[2];
    				break;
    			}
    		}
    	}
    	
    	return answer;
    }
}
