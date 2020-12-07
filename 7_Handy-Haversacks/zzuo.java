import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class zzuo {

    public static void main(String[] args) throws FileNotFoundException {
        String path = "input7.txt"; // full file path to input file
        part1(new Scanner(new File(path)));
        part2(new Scanner(new File(path)));
    }

    public static void part1(Scanner scn) {
        ArrayList<Bag> bags = new ArrayList<>();
        while(scn.hasNextLine()) {
            bags.add(parseBag(scn.nextLine()));
        }
        HashSet<String> bagList = new HashSet<>(); // contains list of outer bag (no duplicate)
        findOuter(bags,bagList,"shiny gold");
        System.out.println("# of bags that contains at least 1 shiny gold bag = "+bagList.size());
    }

    // recursively find all outer bags and store in bagList
    public static void findOuter(ArrayList<Bag> bags,HashSet<String> bagList,  String name) {
        for(Bag b : bags) {
            if (b.contents.containsKey(name)) {
                bagList.add(b.name);
                findOuter(bags, bagList, b.name);
            }
        }
    }

    public static void part2(Scanner scn) {
        ArrayList<Bag> bags = new ArrayList<>();
        while(scn.hasNextLine()) {
            bags.add(parseBag(scn.nextLine()));
        }
        System.out.println("# of inner bags of a shiny gold bag = "+countInner(bags, "shiny gold"));
    }

    // return the number of inner bags (recursive)
    public static int countInner(ArrayList<Bag> bags, String target) {
        int count = 0;
        for(Bag b : bags) {
            if (b.name.equals(target)) { // find the target bag based on color
                for (Map.Entry<String, Integer> innerBag : b.contents.entrySet()) {
                    // # of each inner bag * (itself(1) + its inner bags)
                    count += innerBag.getValue() * (countInner(bags, innerBag.getKey()) + 1);
                }
                break;
            }
        }
        return count;
    }

    // parse each line of bag and return a Bag object
    // Sample s: "muted coral bags contain 1 bright magenta bag, 1 dim aqua bag."
    /*
    * Bag {
    *   String name: "muted coral";
    *   HashMap<String, Integer> content: {
    *       {"bright magenta", 1};
    *       {"dim aqua", 1};
    *   };
    * }
    * */
    public static Bag parseBag (String s) {
        ArrayList<String> buffer = new ArrayList<>();
        int bagInd = s.indexOf("bags");
        String name = s.substring(0, bagInd-1); // first bag name (muted coral)
        HashMap<String, Integer> contents = new HashMap<>();
        if(s.contains("no other bags")) { // content is empty
            return new Bag(name, contents);
        }
        Scanner scn = new Scanner(s.substring(bagInd));
        scn.next(); // bags
        scn.next(); // contain
        while(scn.hasNext()) {
            String next = scn.next();
            if(next.contains("bag")) {
                StringBuilder innerBagName = new StringBuilder();
                for(int i=1; i<buffer.size(); i++) {
                    innerBagName.append(buffer.get(i)).append(" ");
                }
                contents.put(innerBagName.substring(0,innerBagName.length()-1), Integer.parseInt(buffer.get(0)));
                buffer.clear();
            }else {
                buffer.add(next);
            }
        }
        return new Bag(name, contents);
    }

    // a Bag has a name and content (inner bags) (count, color)
     static class Bag {
        public String name;
        public HashMap<String, Integer> contents;
        public Bag(String name, HashMap<String, Integer> contents) {
            this.name = name;
            this.contents = contents;
        }
    }

}