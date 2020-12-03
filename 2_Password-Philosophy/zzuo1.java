import java.util.*;
import java.io.*;

public class zzuo1 {

	private static String inputFile = "input1.txt"; // input path

	public static void main(String[] args) {
		part1();
		part2();
	}

	public static String getInput() {
		try {
			File f = new File(inputFile);
			if (!f.exists()) {
				System.out.println(String.format("%s not found", inputFile));
				return null;
			}
			Scanner scanner = new Scanner(f);
			return scanner.useDelimiter("\\Z").next();
		} catch (IOException e) {
			e.printStackTrace();
			return null;
		}
	}

	public static void part1() {
		// Good luck!
		String input = getInput();
		Scanner fc = new Scanner(input);
		int total = 0;
		while(fc.hasNextLine()) {
			int count = 0;
			String cs = fc.nextLine();
			String[] strs = cs.split("[\\p{Punct}\\s]+");
			int lower = Integer.parseInt(strs[0]);
			int upper = Integer.parseInt(strs[1]);
			char c = strs[2].charAt(0);
			String str = strs[3];
			for(int i=0; i<str.length(); i++) {
				if (str.charAt(i) == c) {count++;}
			}
			if(count >= lower && count <= upper) {total++;}
		}
		fc.close();
		System.out.println("Total "+total);
	}

	public static void part2() {
		String input = getInput();
		Scanner fc = new Scanner(input);
		int total = 0;
		while(fc.hasNextLine()) {
			int count = 0;
			String cs = fc.nextLine();
			String[] strs = cs.split("[\\p{Punct}\\s]+");
			int lower = Integer.parseInt(strs[0])-1;
			int upper = Integer.parseInt(strs[1])-1;
			char c = strs[2].charAt(0);
			String str = strs[3];
			int len = str.length();
			if(str.charAt(lower) == c) {count++;}
			if(str.charAt(upper) == c) {count++;}
				if(count == 1) {total++;}
		}
		fc.close();
		System.out.println("Total "+total);
	}
}
