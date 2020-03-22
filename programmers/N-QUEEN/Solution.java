class Solution {
	
	static int answer = 0;
	static int combi = 0;
	
    public int solution(int n) {
        int[] coord = new int[n];
        
        for(int i=0; i<n ; i++) {
        	coord[0] = i;
        	explore(coord, 1 , n);
        }
        
        return answer;
    }
    
    public void explore(int[] coord, int depth, int n) {
    	if(depth==n) {
    		answer+=1;
    		return ;
    	}
    	for(int i = 0 ; i < n ; i++) {
    		coord[depth] = i ;
    		if(check(coord, depth)) {
//    			System.out.println(coord[0]+" "+coord[1]+" "+coord[2]+" "+ coord[3]+"    "+ depth);
    			explore(coord, depth+1 , n);
    		}
    	}
    }
    
    public boolean check(int[] coord, int depth) {
    	for(int i = 0 ; i< depth ; i++) {
    		if(!checkPair(coord,i,depth)) {
    			return false;
    		}
    	}
    	return true;
    }
    public boolean checkPair(int[] coord, int i, int j) {
    	if(coord[i]==coord[j]) {
    		return false;
    	}else if(Math.abs(i-j)==Math.abs(coord[i]-coord[j])) {
    		return false;
    	}else {
    		return true;
    	}
    }
}
