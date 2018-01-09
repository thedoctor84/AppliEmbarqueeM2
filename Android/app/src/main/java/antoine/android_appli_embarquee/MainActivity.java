package antoine.android_appli_embarquee;

import android.os.Handler;
import android.os.Looper;
import android.os.StrictMode;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

import com.github.niqdev.mjpeg.DisplayMode;
import com.github.niqdev.mjpeg.Mjpeg;
import com.github.niqdev.mjpeg.MjpegView;

import java.io.BufferedWriter;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Arrays;

import io.github.controlwear.virtual.joystick.android.JoystickView;

public class MainActivity extends AppCompatActivity {

    MjpegView mjpegView;

    private Socket socket;
    public static int currentAngle;
    public static int currentStrength;

    private static final int SERVERPORT = 2010;
    private static final String SERVER_IP = "192.168.137.199";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        if (android.os.Build.VERSION.SDK_INT > 9)
        {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }

        try{
            new AsyncJoystickCommands().execute();

        }catch (Exception e) {
            e.printStackTrace();
        }

        //new Thread(new ClientThread()).start();
        int TIMEOUT = 10; //seconds

        mjpegView = findViewById(R.id.camera);

        Mjpeg.newInstance()
                .open("http://192.168.137.199/html/cam_pic_new.php", TIMEOUT)
                .subscribe(inputStream -> {
                    mjpegView.setSource(inputStream);
                    mjpegView.setDisplayMode(DisplayMode.FULLSCREEN);
                    mjpegView.showFps(true);
                });
        JoystickView joystick = (JoystickView) findViewById(R.id.joystickView);
        joystick.setOnMoveListener(new JoystickView.OnMoveListener() {
            @Override
            public void onMove(int angle, int strength) {
                currentAngle = angle;
                currentStrength = strength;
                /*try {
                    String result = angle+";"+strength;
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
                    //dout.close();
                    //socket.close();
                } catch (UnknownHostException e1) {
                    e1.printStackTrace();
                } catch (IOException e1) {
                    e1.printStackTrace();
                }*/
            }
        });
    }

    @Override
    public void onPause() {
        super.onPause();
        AsyncJoystickCommands.activityIsDestroyed=true; // Stop the infinite loop
    }

    /*class ClientThread implements Runnable {

        @Override
        public void run() {
            try {
                InetAddress serverAddr = InetAddress.getByName(SERVER_IP);
                socket = new Socket(serverAddr, SERVERPORT);
                while (!Thread.currentThread().isInterrupted()) {
                    try {
                        String result = currentAngle+";"+currentStrength;
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
                        wait(250);
                    } catch (InterruptedException ex) {
                        Thread.currentThread().interrupt();
                    }
                }
            } catch (UnknownHostException e1) {
                e1.printStackTrace();
            } catch (IOException e1) {
                e1.printStackTrace();
            }

        }

    }*/
}
