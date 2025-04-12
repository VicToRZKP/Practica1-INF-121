package ejercicio3;

public class Coche {
	private String marca,modelo;
	private double velocidad;
	public Coche(String ma,String mo,double v) {
		marca=ma;
		modelo=mo;
		velocidad=v;
	}
	
	//METODOS
	public void mostrar() {
		System.out.println("------coche-----");
		System.out.println("marca: "+marca);
		System.out.println("modelo: "+modelo);
		System.out.println("velocidad: "+velocidad);
	}
	
	public void acelerar() {
		double aceleracion=velocidad+10.0;
		System.out.println("la aceleracion es"+aceleracion);
	}
	public void frenar() {
		double frenar=velocidad-5.0;
		System.out.println("disminucion de velocidad es: "+frenar);
	}
	
}
