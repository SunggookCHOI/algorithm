import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));;
		StringTokenizer st = new StringTokenizer(br.readLine());
		int t = Integer.parseInt(st.nextToken());
		int[] temp = new int[3];
		String h = "";
		String w ="";
		for(int i=0; i<t; i++) {
			h="";
			w="";
			st = new StringTokenizer(br.readLine());
			temp = new int[3];
			//높이, 너비, 순서
			for(int j=0;j<3;j++) {
				temp[j]=Integer.parseInt(st.nextToken());
			}
			temp[2]--;
			w=(temp[2]/temp[0]+1)+"";
			h=(temp[2]%temp[0]+1)+"";
			if(w.length()==1) {
				System.out.println(h+"0"+w);
			}else {
				System.out.println(h+w);
			}
		}
		
	}
}
