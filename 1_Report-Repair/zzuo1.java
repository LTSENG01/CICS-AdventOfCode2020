import java.util.*;
import java.io.*;

public class zzuo1 {

	private static String inputFile = "input0.txt"; // input path
	
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
        String input = getInput();
        int mulOfSquares = 0;
        HashSet<Integer> hs = new HashSet<Integer>();
        for (String line : input.split("\n")) {
            int curr = Integer.parseInt(line.strip());
            if(hs.contains(curr)){
                mulOfSquares = curr * (2020-curr);
                break;
            }
            hs.add(2020-curr);
        }
        System.out.println(String.format("Multiple of squares: %d", mulOfSquares));
    }

    public static void part2() {
        String input = getInput();
        ArrayList<Integer> nums = new ArrayList<Integer>();
        int i=0;
        for (String line : input.split("\n")) {
            nums.add(Integer.parseInt(line.strip()));
        }
        Collections.sort(nums);
        for (i = 0; i < nums.size() - 2; i++) {
            if (i == 0 || nums.get(i) != nums.get(i-1)) {
                int low = i + 1, high = nums.size() - 1, sum = 2020 - nums.get(i);
                while (low < high) {
                    if (nums.get(low) + nums.get(high) == sum) {
                        System.out.println(String.format("Multiple of cubes: %d", nums.get(i) * nums.get(low) * nums.get(high)));
                        return;
                    } else if (nums.get(low) + nums.get(high) < sum) {
                        low++;
                    } else {
                        high--;
                    }
                }
            }
        }
        System.out.println("Done!");
    }
}