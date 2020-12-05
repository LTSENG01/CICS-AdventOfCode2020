import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class zzuo {
    public static void main(String[] args) throws FileNotFoundException {
        String path = "input5.txt"; // input file full path
        part1(new Scanner(new File(path)));
        part2(new Scanner(new File(path)));
    }

    public static void part1(Scanner scn) {
        int highestID = 0;
        while(scn.hasNextLine()) {
            int currID = getSeat(scn.nextLine());
            if(currID > highestID) {
                highestID = currID;
            }
        }
        System.out.println("Highest seat id is : "+highestID);
    }

    public static void part2(Scanner scn) {
        ArrayList<Integer> seats = new ArrayList<>();
        while(scn.hasNextLine()) {
            seats.add(getSeat(scn.nextLine()));
        }
        Collections.sort(seats);
        int prev = 0;
        for(Integer i : seats) {
            if(i == (prev + 2)){
                System.out.println("Id of your seat is : " + (prev + 1));
            }
            prev = i;
        }
    }

    public static int getSeat(String binary) {
        int currID = 0, low = 0, high = 127;
        for(int i=0; i<7; i++) {
            if(binary.charAt(i) == 'F') { // front
                high = (low+high)/2;
            } else { // back
                low = (int) Math.ceil((low+high)/2.0);
            }
        }
        currID += 8 * low;
        low = 0;
        high = 7;
        for(int i=7; i<10; i++) {
            if(binary.charAt(i) == 'L') { // left
                high = (low+high)/2;
            } else { // right
                low = (int) Math.ceil((low+high)/2.0);
            }
        }
        currID += low;
        return currID;
    }
}