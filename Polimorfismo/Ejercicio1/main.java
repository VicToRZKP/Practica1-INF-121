package eje1;

public class main {

	public static void main(String[] args) {
		VideoJuego a=new VideoJuego();
		a.mostrar();
		a.agregarJugador();
		a.agregarJugador(5);
		a.mostrar();
		
		VideoJuego b=new VideoJuego("super mario"," nintendo",2);
		b.mostrar();
		b.agregarJugador();
		b.agregarJugador(3);
		b.mostrar();
		
		VideoJuego c=new VideoJuego("bonsqua");
		c.mostrar();
		c.agregarJugador();
		c.agregarJugador(4);
		c.mostrar();
	}

}
