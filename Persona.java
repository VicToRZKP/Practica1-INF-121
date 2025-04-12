package ejercicio1;
public class Persona {
	private String nombre, ciudad;
	private int edad;
	public Persona(String n,String c,int e) {
		nombre=n;
		ciudad=c;
		edad=e;}
	public void saludo() {
		System.out.println("Hola soy "+ nombre+", de "+ciudad);}
	public boolean mayordeEdad() {
		if (edad>=18){
			return true;}
		else{
			return false;}
	}
}
