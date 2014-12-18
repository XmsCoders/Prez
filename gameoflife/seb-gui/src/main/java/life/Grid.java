package life;

import java.util.Random;

import org.eclipse.swt.SWT;
import org.eclipse.swt.widgets.Button;
import org.eclipse.swt.widgets.Shell;

public class Grid {

    Button[][] buttons;
    boolean[][] buttonsState;
    Random random = new Random();
    int size;
    Shell shell;
    
    public Grid(int size, Shell shell) {
        this.size = size;
        this.shell = shell;
        buttons = new Button[size][size];
        buttonsState = new boolean[size][size];
        for (int i = 0; i < this.buttons.length; i++) {
            for (int j = 0; j < this.buttons[i].length; j++) {
                this.buttons[i][j] = new Button(shell, SWT.CHECK);
                this.buttonsState[i][j] = random.nextBoolean();
                this.buttons[i][j].setSelection(buttonsState[i][j]);
            }
        }
    }

    public void printGrid() {
        for (int i = 0; i < this.buttonsState.length; i++) {
            for (int j = 0; j < this.buttonsState[i].length; j++) {
                System.out.print(this.buttonsState[i][j] ? 1 : 0);
            }
            System.out.println();
        }
        System.out.println();
    }
    
    public void computNextGrid() {
        boolean[][] nextRoundState = new boolean[size][size];
        for (int i = 0; i < this.buttonsState.length; i++) {
            for (int j = 0; j < this.buttonsState[i].length; j++) {
                int nb = getNeighboursCount(i, j);
                if (this.buttonsState[i][j]) {  // si alive
                    nextRoundState[i][j] = (nb == 2) || (nb == 3);
                } else { // si dead
                    nextRoundState[i][j] = nb == 3;
                }
            }
        }
        for (int i = 0; i < this.buttons.length; i++) {
            for (int j = 0; j < this.buttons[i].length; j++) {
                buttons[i][j].setSelection(nextRoundState[i][j]);
            }
        }
        buttonsState = nextRoundState;
        printGrid();
    }
    
    public int getNeighboursCount(int i, int j) {
        int result = 0;
        if (i>0 && j>0 &&buttonsState[i-1][j-1]) result++;
        if (j>0 && buttonsState[i][j-1]) result++;
        if (i<size-1 && j>0 && buttonsState[i+1][j-1]) result++;
        if (i>0 && buttonsState[i-1][j]) result++;
        if (i<size-1 && buttonsState[i+1][j]) result++;
        if (j<size-1  && i>0 && buttonsState[i-1][j+1]) result++;
        if (j<size-1 && buttonsState[i][j+1]) result++;
        if (i<size-1 && j<size-1 && buttonsState[i+1][j+1]) result++;
        return result;
    }

}
