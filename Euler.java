import java.util.*;

public class Euler
{
    final SIZE = 20;
    public static void main(String[] args)
    {

    }

    public static boolean rWall(Point p)
    {
        return p.getX() >= SIZE;
    }

    public static boolean dWall(Point p)
    {
        return p.getY() >= SIZE;
    }
}
