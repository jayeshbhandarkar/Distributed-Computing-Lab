import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class BerkeleyAlgorithm {
    private static final long MILLIS_PER_SECOND = 1000;

    public static void berkeleyAlgo(String servertime, String time1, String time2) {
        System.out.println("Server Clock = " + servertime);
        System.out.println("Client Clock = " + time1);
        System.out.println("Client clock 2 = " + time2);

        SimpleDateFormat sdf = new SimpleDateFormat("mm:ss");
        try {
            long s = sdf.parse(servertime).getTime();
            long t1 = sdf.parse(time1).getTime();
            long t2 = sdf.parse(time2).getTime();

            long st1 = t1 - s;
            System.out.println("t1 - s  = " + st1 / 1000);

            long st2 = t2 - s;
            System.out.println("t2 - s  = " + st2 / 1000);

            long aveg = ((st1 + st2) / 1000);
            System.out.println("(st1 + st2) / 2 = " + aveg / 2);

            long adjserver = (aveg / 2) * 1000 + s;
            long adj_t1 = (aveg / 2) * 1000 - st1;
            long adj_t2 = (aveg / 2) * 1000 - st2;

            System.out.println("t1 adjustment = " + adj_t1 / 1000);
            System.out.println("t2 adjustment = " + adj_t2 / 1000);

            System.out.println("Synchronized Server Clock = " + sdf.format(new Date(adjserver)));
            System.out.println("Synchronized Client 1 Clock = " + sdf.format(new Date(t1 + adj_t1)));
            System.out.println("Synchronized Client 2 Clock = " + sdf.format(new Date(t2 + adj_t2)));

        } catch (ParseException e) {
            System.err.println("Error parsing time: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        berkeleyAlgo("10:00", "10:05", "10:03");
    }
}