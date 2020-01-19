import java.util.ArrayList;

class Solution {
	static int answer = 0;
	static int[][] condition ;
    public int solution(int[][] baseball) {
    	condition = baseball;
        getNumbers();
        return answer;
    }
    
    public boolean check(String target , int[] condition) {
    	ArrayList<Character> t = new ArrayList<>();
    	ArrayList<Character> c = new ArrayList<>();
    	int strike = 0;
    	int ball = 0;
    	for(int i = 0 ; i<3 ; i++) {
    		t.add((target+"").charAt(i));
    		c.add((condition[0]+"").charAt(i));
    	}
    	for(int i=0; i<3 ; i++) {
    		if(c.contains(t.get(i))) {
    			if(c.indexOf(t.get(i))==i) {
    				strike++;
    			}else {
    				ball++;
    			}
    		}
    	}
    	if(strike==condition[1] && ball==condition[2]) {
    		return true;
    	}
    	return false;
    }
    public void getNumbers() {
    	int[] arr = new int[3];
    	for(int i = 1 ; i<10 ; i++) {
    		arr[0] = i;
    		makeNumbers(arr,1);
    	}
    }
    public void makeNumbers(int[] arr, int depth) {
		if(depth==3) {
			String temp = ""+arr[0]+arr[1]+arr[2];
			boolean tf = true;
			for(int[] c : condition) {
				if(!check(temp,c)) {
					tf=false;
					break;
				}
			}
			if(tf) {
				answer +=1 ;
			}
			return ;
		}
		for(int i = 1 ; i<10 ; i++) {
			boolean c = true;
			for(int d =0; d<depth+1 ; d++) {
				if(arr[d]==i) {
					c=false;
					break;
				}
			}if(c) {
				arr[depth] = i;
				makeNumbers(arr, depth+1);
			}
		}
    }
}
