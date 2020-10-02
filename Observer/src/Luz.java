public class Luz implements Observer {
    @Override
    public void update() {
        System.out.println("Se prendió la luz");
    }
}
