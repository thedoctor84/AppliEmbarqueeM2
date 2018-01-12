package antoine.android_appli_embarquee;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.view.Window;
import android.webkit.WebView;
import android.widget.ImageButton;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

import io.github.controlwear.virtual.joystick.android.JoystickView;

public class MainActivity extends AppCompatActivity {
    public static int currentAngle;
    public static int currentStrength;

    ImageButton imageButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        addListenerOnButton();

        WebView camera = (WebView) findViewById(R.id.camera);
        camera.loadUrl("http://192.168.137.199/html/cam_pic_new.php");

        JoystickView joystick = (JoystickView) findViewById(R.id.joystickView);
        joystick.setOnMoveListener(new JoystickView.OnMoveListener() {
            @Override
            public void onMove(int angle, int strength) {
                currentAngle = angle;
                currentStrength = strength;
            }
        });
    }

    @Override
    public void onResume() {
        super.onResume();
        try {
            new AsyncJoystickCommands().execute();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    public void onPause() {
        super.onPause();
        AsyncJoystickCommands.activityIsDestroyed = true; // Stop the infinite loop
    }

    public void addListenerOnButton() {

        imageButton = (ImageButton) findViewById(R.id.cameraButton);

        imageButton.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View arg0) {
                try {
                    URL url = new URL("http://192.168.137.199/html/call-classifier.php");
                    HttpURLConnection conn = (HttpURLConnection) url.openConnection();
                    String line;
                    StringBuilder objetDetecte = new StringBuilder();
                    BufferedReader br = new BufferedReader(new InputStreamReader(conn.getInputStream(), "UTF-8"));
                    if ((line=br.readLine()) != null) {
                        objetDetecte.append(line);
                    }
                    br.close();
                    Toast.makeText(MainActivity.this,objetDetecte.toString(), Toast.LENGTH_SHORT).show();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
    }
}
