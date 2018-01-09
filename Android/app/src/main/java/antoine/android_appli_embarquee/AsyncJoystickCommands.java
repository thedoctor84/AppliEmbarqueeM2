package antoine.android_appli_embarquee;

import android.os.AsyncTask;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Arrays;

/**
 * Created by antoine on 09/01/2018.
 */

public class AsyncJoystickCommands extends AsyncTask<String, Void, String> {
    private Socket socket;
    private static final int SERVERPORT = 2015;
    private static final String SERVER_IP = "192.168.137.199";
    public static boolean activityIsDestroyed;
    protected String doInBackground(String... args) {

        InetAddress serverAddr = null;
        try {
            serverAddr = InetAddress.getByName(SERVER_IP);
            socket = new Socket(serverAddr, SERVERPORT);
        } catch (UnknownHostException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }

        try {
            while(!activityIsDestroyed) {
                String result = MainActivity.currentAngle+";"+MainActivity.currentStrength;
                byte[] utf8Bytes = result.getBytes("UTF-8");
                int numberOfSpaces = 7 - utf8Bytes.length;
                byte[] bytesToSend = new byte[7];
                Arrays.fill(bytesToSend, 0, numberOfSpaces, (byte) 32);
                System.arraycopy(utf8Bytes, 0, bytesToSend, numberOfSpaces, utf8Bytes.length);
                String message = new String(bytesToSend, "UTF-8");
                System.out.println("MESSAGE="+message);
                PrintWriter out = new PrintWriter(new BufferedWriter(
                        new OutputStreamWriter(socket.getOutputStream(),"UTF-8")),true);
                out.println(message);
                try {
                    Thread.sleep(250);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
            if(activityIsDestroyed) {
                String message = "stop!!!";
                System.out.println("MESSAGE="+message);
                PrintWriter out = new PrintWriter(new BufferedWriter(
                        new OutputStreamWriter(socket.getOutputStream(),"UTF-8")),true);
                out.println(message);
            }
        } catch (UnknownHostException e1) {
            e1.printStackTrace();
        } catch (IOException e1) {
            e1.printStackTrace();
        }
        return null;//returns what you want to pass to the onPostExecute()
    }
}
