import java.util.ArrayList;

public class Switch  implements SujetoObservado{

    private ArrayList<Observer> observadores;
    public Switch(){
        observadores = new ArrayList<Observer>();
    }
    public void subirSwitch(){
        notificar();
    }
    public void unirObservaodres(Observer a){
        observadores.add(a);

    }
    @Override
    public void notificar() {
        for(Observer a:observadores){a.update();
        }
    }
}
