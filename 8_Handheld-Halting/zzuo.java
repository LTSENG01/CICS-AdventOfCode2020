import java.io.File;
import java.io.FileNotFoundException;
import java.text.DecimalFormat;
import java.text.ParseException;
import java.util.*;

public class zzuo {
    public static void main(String[] args) throws FileNotFoundException, ParseException {
        String path = "input8.txt"; // full path to input file
        part1(new Scanner(new File(path)));
        part2(new Scanner(new File(path)));
    }

    public static void part1(Scanner scn) throws ParseException {
        ArrayList<String> instructions = new ArrayList<>();
        HashSet<Integer> executed = new HashSet<>();
        while(scn.hasNextLine()) {
            instructions.add(scn.nextLine());
        }
        int accumulator = 0, pointer = 0; // pointer points to current instruction
        DecimalFormat df = new DecimalFormat("+#;-#");
        while(!executed.contains(pointer)) {
            executed.add(pointer);
            String str = instructions.get(pointer);
            String ins = str.substring(0, str.indexOf(" ")); // instruction = "nop"/"acc"/"jmp"
            int val = df.parse(str.substring(str.indexOf(" ")+1)).intValue(); // value such as "-50"/"+200"
            switch (ins) {
                case "nop" -> pointer++;
                case "acc" -> {
                    accumulator += val;
                    pointer++;
                }
                case "jmp" -> pointer += val;
            }
        }
        System.out.println("Value of the accumulator before infinite loop = "+ accumulator);
    }

    public static void part2(Scanner scn) throws ParseException {
        ArrayList<String> instructions = new ArrayList<>();
        LinkedList<Integer> executed = new LinkedList<>();// contains line # of executed instructions (in order)
        while(scn.hasNextLine()) {
            instructions.add(scn.nextLine());
        }
        int accumulator = 0, pointer = 0;
        DecimalFormat df = new DecimalFormat("+#;-#");
        while(pointer < instructions.size()) {
            executed.add(pointer);
            String str = instructions.get(pointer);
            String ins = str.substring(0, str.indexOf(" "));
            int val = df.parse(str.substring(str.indexOf(" ")+1)).intValue();
            switch (ins) {
                case "nop" -> pointer++;
                case "acc" -> {
                    accumulator += val;
                    pointer++;
                }
                case "jmp" -> pointer += val;
            }
            if(executed.contains(pointer)) { // encounter duplicate
                boolean success = false;
                while(!success) {
                    int prev = executed.removeLast();
                    str = instructions.get(prev);
                    ins = str.substring(0, str.indexOf(" "));
                    if(ins.equals("acc")) {
                        accumulator -= df.parse(str.substring(str.indexOf(" ")+1)).intValue();
                        continue;
                    } // else, try change the instruction
                    instructions.set(prev, (ins.equals("nop")? "jmp" : "nop") + str.substring(str.indexOf(" ")));
                    success = test(instructions);
                    if(!success) { // change instruction back and pop the next one
                        instructions.set(prev, str);
                    } else { // success
                        pointer = prev; // move pointer back to changed instruction
                    }
                }
            }
        }
        System.out.println("Value of accumulator after the program terminates = "+accumulator);
    }

	// test if there is an infinite loop (returns true/false)
    public static boolean test(ArrayList<String> instructions) throws ParseException {
        int pointer = 0;
        HashSet<Integer> executed = new HashSet<>();
        DecimalFormat df = new DecimalFormat("+#;-#");
        while(pointer < instructions.size()) {
            executed.add(pointer);
            String str = instructions.get(pointer);
            String ins = str.substring(0, str.indexOf(" "));
            switch (ins) {
                case "nop", "acc" -> pointer++;
                case "jmp" -> pointer += df.parse(str.substring(str.indexOf(" ")+1)).intValue();
            }
            if(executed.contains(pointer) || pointer < 0) {
                return false;
            }
        }
        return true;
    }
}