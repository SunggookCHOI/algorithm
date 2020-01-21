class Solution {
    public boolean solution(int[][] key, int[][] lock) {
        int lockLen = lock.length;
        int[][] l = new int[lockLen*3][lockLen*3];
    	for(int i=0;i<lockLen;i++) {
        	for(int j=0;j<lockLen;j++) {
        		l[i+lockLen][j+lockLen] = lock[i][j];
        	}
        }
    	for(int r=0; r<4;r++) {
    		key=rotate(key);
    		boolean check = compare(key,l);
    		if(check)return true;
    	}
        return false;
    }
    public int[][] rotate(int[][] key){
    	int len = key.length;
    	int[][] ans = new int[len][len];
    	for(int i=0;i<len;i++) {
    		for(int j=0;j<len;j++) {
    			ans[j][len-1-i] = key[i][j];
    		}
    	}
    	return ans;
    }
    public boolean compare(int[][] key, int[][] lock) {
    	int keyLen = key.length;
    	int lockLen = lock.length;
    	int diff = lockLen-keyLen;
    	for(int iMove=0; iMove<=diff;iMove++) {
    		for(int jMove=0; jMove<=diff;jMove++) {
    			int[][] tempKey = new int[lockLen][lockLen];
    			for(int i=0;i<keyLen;i++) {
    				for(int j=0;j<keyLen;j++) {
    					tempKey[i+iMove][j+jMove] = key[i][j];
    				}
    			}
    			boolean check = check(tempKey,lock);
    			if(check)return true;
    		}
    	}
    	return false;
    }
    public boolean check(int[][] key, int[][] lock) {
    	int len = lock.length/3;
    	for(int i=len;i<len*2;i++) {
    		for(int j=len;j<len*2;j++) {
    			if(key[i][j]+lock[i][j]!=1) {
    				return false;
    			}
    		}
    	}
    	return true;
    }
}
