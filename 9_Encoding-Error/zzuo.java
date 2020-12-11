import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class zzuo {
    public static void main(String[] args) throws FileNotFoundException{
        String path = "input9.txt"; // full input file path
        part1(new Scanner(new File(path)));
        part2(new Scanner(new File(path)));
    }

    private static void part1(Scanner scn) {
        LinkedList<Long> fifo = new LinkedList<>();
        for(int i=0; i<25; i++) {
            fifo.add(Long.parseLong(scn.nextLine()));
        }
        long curr = Long.parseLong(scn.nextLine());
        while(valid(fifo, curr)) {
            fifo.remove();
            fifo.add(curr);
            curr = Integer.parseInt(scn.nextLine());
        }
        System.out.println("The first number that does not have this property is "+curr);
    }

    public static boolean valid(LinkedList<Long> list, long target) {
        HashSet<Long> hs = new HashSet<>();
        for (int i = 0; i < list.size(); hs.add(list.get(i++)))
            if (hs.contains(target - list.get(i)))
                return true;
        return false;
    }

    private static void part2(Scanner scn) {
        long target = 138879426, sum = 0;
        ArrayList<Long> list = new ArrayList<>();
        LinkedList<Long> numSet = new LinkedList<>();
        while(scn.hasNextLine()) { list.add(Long.parseLong(scn.nextLine()));}
        for(int i=0; i<list.size(); i++) {
            for(int j=i; sum<target; j++) {
                numSet.add(list.get(j));
                sum += list.get(j);
            }
            if(sum == target) {break;}
            else {sum = 0; numSet.clear();}
        }
        System.out.println("The encryption weakness is " + (Collections.max(numSet) + Collections.min(numSet)));
    }
}