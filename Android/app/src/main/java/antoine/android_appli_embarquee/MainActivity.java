package antoine.android_appli_embarquee;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.webkit.WebView;

import io.github.controlwear.virtual.joystick.android.JoystickView;

public class MainActivity extends AppCompatActivity {
    public static int currentAngle;
    public static int currentStrength;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        int TIMEOUT = 10; //seconds

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
        try{
            new AsyncJoystickCommands().execute();
        }catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    public void onPause() {
        super.onPause();
        AsyncJoystickCommands.activityIsDestroyed=true; // Stop the infinite loop
    }


}
