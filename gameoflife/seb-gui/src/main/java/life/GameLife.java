package life;

import java.io.IOException;

import org.eclipse.swt.layout.GridLayout;
import org.eclipse.swt.widgets.Display;
import org.eclipse.swt.widgets.Shell;

public class GameLife {

    private static final int WIDTH = 30;

    public static void main(String[] args) throws IOException {

        Display display = new Display();
        Shell shell = new Shell(display);
        shell.setLayout(new GridLayout(WIDTH, true));

        final Grid grid = new Grid(WIDTH, shell);
        shell.open();
        shell.pack();

        new Thread(() -> {
            for (int k = 0; k < 300; k++) {
                try {
                    Thread.sleep(500);
                } catch (InterruptedException exn) {
                }
                display.asyncExec(() -> grid.computNextGrid());
            }
        }).start();

        while (!shell.isDisposed())
            if (!display.readAndDispatch())
                display.sleep();
        display.dispose();
    }
}
