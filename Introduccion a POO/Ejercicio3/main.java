package ejercicio3;

public class main {

	public static void main(String[] args) {
		Coche a=new Coche("toyota","hilux",56.98);
		a.mostrar();
		a.acelerar();
		a.frenar();
		Coche b=new Coche("nissan","panthfinder",20.98);
		b.mostrar();
		b.acelerar();
		b.frenar();
	}

}
