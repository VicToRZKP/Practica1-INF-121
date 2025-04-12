package eje1;

public class VideoJuego {
	private String nombre, plataforma;
	private int cantJugadores;
	
	public VideoJuego() {
		nombre="clash royale";
		plataforma ="super cell";
		cantJugadores=1;
	}
	 public VideoJuego( String n,String p, int cj) {
		 nombre=n;
		 plataforma=p;
		 cantJugadores=cj;
	 }
	 
	 public VideoJuego( String n) {
		 nombre=n;
		 plataforma="android";
		 cantJugadores=3;
			 
	 }
	 public void mostrar() {
		 System.out.println("---------videojuego---------");
		 System.out.println("nombre: "+nombre);
		 System.out.println("plataforma: "+plataforma );
		 System.out.println("cantJugadores: "+cantJugadores);
	 }
	 
	 public int agregarJugador() {
		 cantJugadores = cantJugadores+1;
		 System.out.println("se agrego un jugador");
		 System.out.println("cantidad actual de jugadores: "+cantJugadores);
		 return cantJugadores;
	 }
	 
	 public int agregarJugador(int x) {
		 cantJugadores=cantJugadores+x;
		 System.out.println("se agrego "+x+" jugadores");
		 System.out.println("cantidad actual de jugadores: "+cantJugadores);
		 return cantJugadores;
	 }
}
