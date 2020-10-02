public class Main {
    public static void main(String[] args) {

        Luz bombillo = new Luz();
        Switch cuarto = new Switch();
        cuarto.unirObservaodres(bombillo);
        cuarto.subirSwitch();
    }
}