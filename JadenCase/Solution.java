package programmers;

class Solution {
	public String solution(String s) {
		StringBuilder sb = new StringBuilder();
		boolean first = true;
		for (int i =0; i<s.length() ; i++) {
			char c = s.charAt(i);
			if(first) {
				if(isAlpha(c)) {
					sb.append(Character.toUpperCase(c));
					first=false;
				}else if(c==' ') {
					sb.append(c);
				}
				else {
					sb.append(c);
					first=false;
				}
			}else {
				if(isAlpha(c)) {
					sb.append(Character.toLowerCase(c));
				}else if(c == ' ') {
					sb.append(c);
					first=true;
				}else {
					sb.append(c);
				}
			}
		}
		
		return sb.toString();
	}
	public boolean isAlpha(char c) {
		if((c>='a' && c<='z') || (c>='A' && c<='Z')) {
			return true;
		}else {
			return false;
		}
	}
}