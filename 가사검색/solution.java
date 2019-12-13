import java.util.ArrayList;
import java.util.HashMap;

class Solution {
	static HashMap<Integer, Node> root = new HashMap<>();
	static HashMap<Integer, Node> reverseRoot = new HashMap<>();
	public int[] solution(String[] words, String[] queries) {
		int[] answer = new int[queries.length];
		for (String word : words) {
			if (root.keySet().contains((Integer) word.length())) {
				insert(root.get((Integer) word.length()), word);
				insert(reverseRoot.get((Integer) word.length()), reverseString(word));
			} else {
				root.put((Integer) word.length(), new Node(' '));
				reverseRoot.put((Integer) word.length(), new Node(' '));
				insert(root.get((Integer) word.length()), word);
				insert(reverseRoot.get((Integer) word.length()), reverseString(word));
			}
		}
		for (int i = 0; i < queries.length; i++) {
			answer[i] = search(queries[i]);
		}
		return answer;
	}
	public String reverseString(String s) {
		return (new StringBuffer(s)).reverse().toString();
	}

	public void insert(Node node, String word) {
		Node parent = node;
		int length = word.length();
		for (int i = 0; i < word.length(); i++) {
			parent.numOfChildren++;
			char target = word.charAt(i);
			if (parent.getOneChild(target) != null) {
				parent = parent.getOneChild(target);
			} else {
				parent.insertChild(target);
				parent = parent.getOneChild(target);
			}
		}
	}
	public int search(String query) {
		if (!root.keySet().contains((Integer) query.length()))
			return 0;
		boolean forward = true;
		// index of question mark
		int index = 0;
		if (query.indexOf("?") == 0) {
			forward = false;
			query = reverseString(query);
			index = query.indexOf("?");
		} else {
			index = query.indexOf("?");
		}
		// length of question marks
		int length = query.length() - index;
		Node parent = root.get((Integer) query.length());
		if (!forward) {
			parent = reverseRoot.get((Integer) query.length());
		}
		for (int i = 0; i < index; i++) {
			parent = parent.getOneChild(query.charAt(i));
			if (parent == null) {
				return 0;
			}
		}
		return parent.numOfChildren;
	}
}

class Node {
	char name;
	ArrayList<Node> child = new ArrayList<>();
	int numOfChildren = 0;
	public Node(char name) {
		super();
		this.name = name;
	}
	public void insertChild(char c) {
		child.add(new Node(c));
	}
	public Node getOneChild(char c) {
		Node ans = null;
		for (Node ch : child) {
			if (ch.name == c) {
				ans = ch;
				break;
			}
		}
		return ans;
	}
}
