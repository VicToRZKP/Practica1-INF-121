package eje3;

public class Administrativo {
	private String nombre,cargo;
	private float sueldoMes;
	
	public Administrativo() {
		nombre="ana";
		sueldoMes=1500;
		cargo="gerente";
	}
	public Administrativo(String n,float sm,String c) {
		nombre=n;
		sueldoMes=sm;
		cargo=c;
	}
	public double sueldoTotal() {
		return sueldoMes;
	}
	public void mostrar() {
		System.out.println("--------administrativo:-------");
		System.out.println("nombre:"+nombre);
		System.out.println("sueldo mes:"+sueldoMes);
		System.out.println("sueldo total: "+sueldoTotal());
	}
	public void mostrar(float x) {
		if (sueldoMes==x) {
			System.out.println("--------el admistrtativo con sueldo igual a x es:-------");
			System.out.println("nombre:"+nombre);
			System.out.println("sueldo mes:"+sueldoMes);
			System.out.println("sueldo total: "+sueldoTotal());
		}
	}
}
