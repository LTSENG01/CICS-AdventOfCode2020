package Day2;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.*;

public class zzuo{

    public static String path = "input.txt"; // input file path

    public static void main(String[] args) throws FileNotFoundException {
        part1();
        part2();
    }

    public static void part1() throws FileNotFoundException {
        Scanner scn = new Scanner(new File(path));
        int c=0, tree = 0;
        while (scn.hasNextLine()) {
            String line = scn.nextLine();
            if (line.charAt(c) == '#') {
                tree++;
            }
            c += 3;
            if (c >= line.length()) {
                c -= line.length();
            }
        }
        System.out.println(tree);
    }

    public static void part2() throws FileNotFoundException {
        long[] total = new long[5];
        total[0] = checkSlope(1,1);
        total[1] = checkSlope(3,1);
        total[2] = checkSlope(5,1);
        total[3] = checkSlope(7,1);
        total[4] = checkSlope(1,2);
        System.out.println(total[0]*total[1]*total[2]*total[3]*total[4]);
    }

    public static long checkSlope(int cCount, int rCount) throws FileNotFoundException {
        Scanner scn = new Scanner(new File(path));
        int c=0;
        long tree = 0;
        while(scn.hasNextLine()) {
            String line = scn.nextLine();
            if(line.charAt(c) == '#') {
                tree++;
            }
            c += cCount;
            if(c >= line.length()){
                c -= line.length();
            }
            for(int i=1; i<rCount && scn.hasNextLine(); i++) {
                scn.nextLine();
            }
        }
        return tree;
    }
}