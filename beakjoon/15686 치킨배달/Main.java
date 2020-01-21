import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Main {
	static int answer = 99999999;
	
	public static void select(int m, int depth, int lastIdx, ArrayList<int[]> home, ArrayList<int[]> chicken, int[][] selected) {
		if(depth==m) {
			calDistance(home,selected);
		}else {
			for(int i=lastIdx; i<chicken.size(); i++) {
				selected[depth] = chicken.get(i);
				select(m,depth+1,i+1,home,chicken,selected);
			}
		}
	}
	
	public static void calDistance(ArrayList<int[]> home, int[][] selected) {
		int ans = 0;
		int[] distance = new int[home.size()];
		for(int i=0;i<home.size();i++) {
			distance[i] = 200;
		}
		for(int i=0;i<home.size();i++) {
			int[] h = home.get(i);
			for(int[] s: selected) {
				int temp = Math.abs(s[0]-h[0])+Math.abs(s[1]-h[1]);
				if(distance[i]>temp) {
					distance[i]=temp;
				}
			}
		}
		for(int d: distance) {
			ans += d;
		}
		if(answer>ans) {
			answer=ans;
		}
	}
	
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));;
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	int n = Integer.parseInt(st.nextToken());
    	int m = Integer.parseInt(st.nextToken());
    	ArrayList<int[]> home = new ArrayList<>();
    	ArrayList<int[]> chicken = new ArrayList<>();
    	for(int i=0;i<n;i++) {
    		st = new StringTokenizer(br.readLine());
    		for(int j=0;j<n;j++) {
    			int temp = Integer.parseInt(st.nextToken());
    			if(temp==1) {
    				home.add(new int[] {i,j});
    			}else if(temp==2) {
    				chicken.add(new int[] {i,j});
    			}
    		}
    	}
    	select(m, 0,0, home, chicken, new int[m][2]);
    	System.out.println(answer);
	}
}
