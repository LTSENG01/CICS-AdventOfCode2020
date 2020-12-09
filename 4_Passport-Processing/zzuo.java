import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class zzuo {

    public static void main(String[] args) throws FileNotFoundException {
        String path = "input4.txt"; // full path of input file
        part1(new Scanner(new File(path)));
        part2(new Scanner(new File(path)));
    }

    public static void part1(Scanner scn){
        int valid = 0, count = 0;
        while(scn.hasNextLine()) {
            String curr = scn.nextLine();
            if(curr.isEmpty()){
                if(count >= 7) {valid++;}
                count = 0;
            }
            Scanner sc = new Scanner(curr);
            while(sc.hasNext()) {
                String curr1 = sc.next();
                curr1 = curr1.substring(0, curr1.indexOf(":"));
                if(!curr1.equals("cid")) {
                    count++;
                }
            }
            sc.close();
        }
        if(count >= 7) {valid++;}
        scn.close();
        System.out.println("Part1 answer is : "+valid);
    }

    public static void part2(Scanner scn) {
        int valid = 0, count = 0;
        while(scn.hasNextLine()) {
            String curr = scn.nextLine();
            if(curr.isEmpty()){
                if(count >= 7) {valid++;}
                count = 0;
            }
            Scanner sc = new Scanner(curr);
            while(sc.hasNext()) {
                String curr1 = sc.next();
                String field = curr1.substring(0, curr1.indexOf(":"));
                String data = curr1.substring(curr1.indexOf(":")+1);
                // start checking each fields by specific case
                switch (field) {
                    case "byr":
                        int byr = Integer.parseInt(data);
                        if (byr >= 1920 && byr <= 2002) {
                            count++;
                        }
                        break;
                    case "iyr":
                        int iyr = Integer.parseInt(data);
                        if (iyr >= 2010 && iyr <= 2020) {
                            count++;
                        }
                        break;
                    case "eyr":
                        int eyr = Integer.parseInt(data);
                        if (eyr >= 2020 && eyr <= 2030) {
                            count++;
                        }
                        break;
                    case "hgt":
                        int index, hgt;
                        if ((index = data.indexOf("cm")) != -1) {
                            data = data.substring(0, index);
                            hgt = Integer.parseInt(data.substring(0, index));
                            if (hgt >= 150 && hgt <= 193) {
                                count++;
                            }
                        } else if ((index = data.indexOf("in")) != -1) {
                            data = data.substring(0, index);
                            hgt = Integer.parseInt(data.substring(0, index));
                            if (hgt >= 59 && hgt <= 76) {
                                count++;
                            }
                        }
                        break;
                    case "hcl":
                        if (data.length() == 7) {
                            int vcount = 0;
                            for (int i = 1; i < 7; i++) {
                                char c = data.charAt(i);
                                if ((c >= '0' && c <= '9') || (c >= 'a' && c <= 'f')) {
                                    vcount++;
                                }
                            }
                            if (vcount == 6) {
                                count++;
                            }
                        }
                        break;
                    case "ecl":
                        //amb blu brn gry grn hzl oth
                        if (data.equals("amb") || data.equals("blu") || data.equals("brn") || data.equals("gry") || data.equals("grn") || data.equals("hzl") || data.equals("oth")) {
                            count++;
                        }
                        break;
                    case "pid":
                        if (data.length() == 9) {
                            int vcount = 0;
                            for (int i = 0; i < 9; i++) {
                                char c = data.charAt(i);
                                if (c >= '0' && c <= '9') {
                                    vcount++;
                                }
                            }
                            if (vcount == 9) {
                                count++;
                            }
                        }
                        break;
                }
            }
            sc.close();
        }
        if(count >= 7) {valid++;}
        scn.close();
        System.out.println("Part2 answer is : "+valid);
    }
}