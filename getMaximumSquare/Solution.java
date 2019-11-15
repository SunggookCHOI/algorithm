package programmers;

class Solution{
    public int solution(int [][]board)    {
        int answer = 0;
        int x = board[0].length;
        int y = board.length;
        for(int i = 0 ; i < x ; i++) {
        	for(int j = 0 ; j < y ; j++) {
        		if(board[j][i]==1) {
    				int temp = maxSquare(board,new int[] {i,j},x,y, answer);
    				System.out.println(i+ " "+j+" "+temp);
    				if(answer < temp) {
    					answer = temp;
    				}
    				if(y-j<=answer) {
    					break;
    				}
        		}
        		if(x-i<=answer) {
        			break;
        		}
        	}
        }
        return answer;
    }
    
    public int maxSquare(int[][] board, int[] start, int x, int y, int answer) {
    	int size = (int) Math.sqrt(answer);
    	boolean check = true;
    	while(check) {
			if((start[0]+size)>x || (start[1]+size)>y) {
				check=false;
				break;
			}
			for(int i = start[0] ; i<start[0]+size ; i++) {
				for(int j = start[1] ; j<start[1]+size ; j++) {
					System.out.println(i+" "+j+" "+size+"   aaaa"+board[j][i]);
					if(board[j][i] != 1) {
						check = false;
						break;
					}
				}
			}
			if(check) {
				size++;
			}
    	}
//    	if(size==answer) {
//    		return 0;
//    	}
    	return (size-1)*(size-1);
    }
    
	public static void main(String[] args) {
//		int[][] board = {{0,1,1,1},{1,1,1,1},{1,1,1,1},{0,0,1,0}};
		int[][] board = {{0,0,0,1},{0,0,0,0}};
		Solution sol = new Solution();
		System.out.println(sol.solution(board));
	}
}