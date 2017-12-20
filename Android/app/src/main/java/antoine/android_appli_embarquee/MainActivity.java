package antoine.android_appli_embarquee;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.github.niqdev.mjpeg.DisplayMode;
import com.github.niqdev.mjpeg.Mjpeg;
import com.github.niqdev.mjpeg.MjpegView;

import io.github.controlwear.virtual.joystick.android.JoystickView;

public class MainActivity extends AppCompatActivity {

    MjpegView mjpegView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        int TIMEOUT = 10; //seconds

        mjpegView = findViewById(R.id.camera);

        Mjpeg.newInstance()
                .open("http://192.168.137.199/html/cam_pic_new.php", TIMEOUT)
                .subscribe(inputStream -> {
                    mjpegView.setSource(inputStream);
                    mjpegView.setDisplayMode(DisplayMode.BEST_FIT);
                    mjpegView.showFps(true);
                });
        /*JoystickView joystick = (JoystickView) findViewById(R.id.joystickView);
        joystick.setOnMoveListener(new JoystickView.OnMoveListener() {
            @Override
            public void onMove(int angle, int strength) {
                System.out.println("ANGLE = "+angle);
                System.out.println("strength = "+strength);
            }
        });*/

    }


}
