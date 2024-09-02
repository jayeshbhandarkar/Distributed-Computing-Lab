import java.io.*;
import java.net.*;
import java.util.*;

public class client {
    public static void main(String[] args) {
        Scanner userinput = new Scanner(System.in);
        try{
            Socket s = new Socket("localhost", 6666);
            DataOutputStream dout = new DataOutputStream(s.getOutputStream());
            System.out.println("Enter 1st No: ");
            int x = userinput.nextInt();

            System.out.println("Enter 2nd No: ");
            int y = userinput.nextInt();

            dout.writeInt(x);
            dout.writeInt(y);

            s.close();

        } catch (Exception e) {
            System.out.println(e);
        }
    }
}