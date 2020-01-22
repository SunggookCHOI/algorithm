import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

class Main {
	static ArrayList<Integer>[] edge = null;
	static int[] access = null;
	
	public void solution() {
		for(int i=1;i<edge.length;i++) {
			boolean[] visit = new boolean[edge.length];
			ArrayList<Integer> stack = new ArrayList<>();
			stack.add(i);
			visit[i]=true;
			dfs(visit,stack);
		}
		int maxAccess = 0;
		ArrayList<Integer> nomi = new ArrayList<>();
		for(int i=1;i<access.length;i++) {
			if(access[i]>maxAccess) {
				maxAccess=access[i];
				nomi=new ArrayList<>();
				nomi.add(i);
			}else if(access[i]==maxAccess) {
				nomi.add(i);
			}
		}
		if(nomi.size()==1) {
			System.out.println(nomi.get(0));
		}else {
			StringBuilder sb = new StringBuilder();
			for(int i=0; i<nomi.size()-1;i++) {
				sb.append(nomi.get(i)+" ");
			}
			sb.append(nomi.get(nomi.size()-1));
			System.out.println(sb.toString());
		}
	}
	
	public void dfs(boolean[] visit, ArrayList<Integer> stack) {
		int nxt = stack.get(stack.size()-1);
		stack.remove(stack.size()-1);
		access[nxt]++;
		for(int nn : edge[nxt]) {
			if(!visit[nn]) {
				visit[nn]=true;
				stack.add(nn);
			}
		}
		if(stack.size()!=0) {
			dfs(visit,stack);
		}
	}
	
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));;
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	
    	int n = Integer.parseInt(st.nextToken());
    	int m = Integer.parseInt(st.nextToken());
    	edge = new ArrayList[n+1];
    	access = new int[n+1];
    	for(int i=0;i<n+1;i++) {
    		edge[i]=new ArrayList<Integer>();
    	}
    	for(int i=0;i<m;i++) {
    		st = new StringTokenizer(br.readLine());
    		int a = Integer.parseInt(st.nextToken());
        	int b = Integer.parseInt(st.nextToken());
        	edge[a].add(b);
    	}
    	Main main = new Main();
    	main.solution();
	}
}
