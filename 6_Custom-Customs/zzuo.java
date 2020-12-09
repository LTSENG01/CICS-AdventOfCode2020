import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Scanner;

public class zzuo {

    public static void main(String[] args) throws FileNotFoundException {
        String path = "input6.txt"; // full file path to input file
        part1(new Scanner(new File(path)));
        part2(new Scanner(new File(path)));
    }

    public static void part1(Scanner scn) {
        int sum = 0;
        HashSet<Character> answers = new HashSet<>();
        while(scn.hasNextLine()) {
            String s = scn.nextLine();
            if(s.isEmpty()) {
                sum += answers.size();
                answers.clear();
            } else {
                for(Character c : s.toCharArray()) {
                    answers.add(c);
                }
            }
        }
        sum += answers.size();
        System.out.println("Part1 sum of count = "+sum);
    }

    public static void part2(Scanner scn) {
        int sum = 0;
        LinkedList<Character> answers = new LinkedList<>();
        for(Character c : scn.nextLine().toCharArray()) {
            answers.add(c);
        }
        while(scn.hasNextLine()) {
            String s = scn.nextLine();
            if(s.isEmpty()) {
                sum += answers.size();
                answers.clear();
                if(scn.hasNextLine()) {
                    for(Character c : scn.nextLine().toCharArray()) {
                        answers.add(c);
                    }
                }
            } else {
                answers.removeIf(c -> !s.contains(c + ""));
            }
        }
        sum += answers.size();
        System.out.println("Part2 sum of count = "+sum);
    }
}