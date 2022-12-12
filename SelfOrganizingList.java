/**
 * Experiment to compare heuristics for self-organizing list. Can choose
 * move-to-front or move-up-one heuristics. Starts with a fixed order and
 * then generates requests according to a fixed probability distribution,
 * or swtiches distribution half way through if switchDist is set.
 */

import java.util.Random;

public class SelfOrganizingList {

  public static void main(String[] args) {
    long seed = 77;
    int k;
    // boolean moveToFront = true;
    boolean moveToFront = false;
    // boolean switchDist = true;
    boolean switchDist = false;

    // boolean moveRandom = true;
    boolean moveRandom = false;

    // boolean moveHalf = true;
    boolean moveHalf = false;
    int iterations = 10_000_000;
    int REPS = 1;

    Random rng = new Random(seed);
    int N = 1000;
    int[] list = new int[N];

    int heuristic_selector = 0;
    double AveragePosition = 0;
    System.out.println("Using " + iterations + " iterations.");

    while (heuristic_selector <= 3) {
      switch (heuristic_selector) {
        case 0: // Move to front
          moveToFront = true;
          moveRandom = false;
          moveHalf = false;
          break;
        case 1: // Move random
          moveToFront = false;
          moveRandom = true;
          moveHalf = false;
          break;
        case 2: // Move half
          moveToFront = false;
          moveRandom = false;
          moveHalf = true;
          break;
        case 3: // Move up one
          moveToFront = false;
          moveRandom = false;
          moveHalf = false;
          break;
      }
      AveragePosition = 0.0;
      list = new int[N];
      for (int i = 0; i < N; ++i) {
        list[i] = i;
      }
      if (moveToFront) System.out.print(
        "Using move to front heuristic.\t"
      ); else if (moveRandom) System.out.print(
        "Using move random heuristic.\t"
      ); else if (moveHalf) System.out.print(
        "Using move half heuristic.\t"
      ); else System.out.print("Using move up one heuristic.\t");

      double x = 0;
      for (int rep = 0; rep < iterations; ++rep) {
        // System.out.println("rep "+rep);
        //k = rng.nextInt(N); // for uniform dist. on requests
        //prtList(list);
        do {
          if ((switchDist) && (rep > iterations / 2)) {
            x = rng.nextGaussian() * Math.sqrt(1.1 * N) + 0.66 * N;
          } else x = rng.nextGaussian() * Math.sqrt(1.1 * N) + 0.33 * N;
          k = (int) x;
        } while ((k < 0) || (k >= N));
        //System.out.println("getting "+k);
        // int i = list.indexOf(k); // search time is here
        int i = 0;
        for (int j = 0; j < N; ++j) {
          if (list[j] == k) {
            i = j;
            break;
          }
        }
        if ((i < 0) || (i >= N)) {
          System.out.println("Bad index.");
          System.exit(3);
        }
        AveragePosition += i;
        // System.out.println("AveragePosition = "+(AveragePosition)+" rep= "+rep);
        //if(rep>0) System.out.println("Avg pos = "+(1.0*AveragePosition/rep));
        //   if (rep > 0) System.out.println(
        //     "Avg pos = " + (1.0 * AveragePosition / (rep + 1.0))
        //   );
        if (moveToFront) { // move-to-front heuristic
          int tmp = list[i];
          for (int m = i; m > 0; m--) list[m] = list[m - 1];
          list[0] = tmp;
        } else if (moveRandom) { // move-random heuristic
          int tmp = list[i];
          // System.out.print(rep + "\t" + i + "\t");
          int m = rng.nextInt(i + 1); // ensure non-zero #
          for (int j = i; j > m; j--) list[j] = list[j - 1];
          list[m] = tmp;
        } else if (moveHalf) { // move-half heuristic
          // move list[i] to i/2
          int tmp = list[i];
          int m = i / 2;
          for (int j = i; j > m; j--) list[j] = list[j - 1];
          list[m] = tmp;
        } else { // move-up-one heuristic
          if (i > 0) {
            int tmp = list[i - 1];
            list[i - 1] = list[i];
            list[i] = tmp;
          }
        }
      }
      System.out.println("Average position: " + (AveragePosition / iterations));
      heuristic_selector++;
    }
  }

  //   System.out.println("Average position: " + (AveragePosition / iterations));
  public static void prtList(int[] l) {
    for (int i = 0; i < l.length; ++i) System.out.print(l[i] + " ");
    System.out.println();
  }
}
