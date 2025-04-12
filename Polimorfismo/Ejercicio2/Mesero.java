package eje3;

public class Mesero {
	private String nombre;
	private int sueldoMes,horasExtra;
	private float sueldoHora, propina;
	
	public Mesero() {
		nombre="carlos";
		sueldoMes=1110;
		horasExtra= 12;
		sueldoHora= 14;
		propina=100;
	}
	public Mesero( String n,int sm,int he,float sh,float p) {
		nombre=n;
		sueldoMes=sm;
		horasExtra= he;
		sueldoHora= sh;
		propina=p;
	}
	public double sueldoTotal() {
		double st=sueldoMes+propina+(horasExtra*sueldoHora);
		return st;
	}
	public void mostrar() {
		System.out.println("--------mesero:-------");
		System.out.println("nombre:"+nombre);
		System.out.println("sueldo mes:"+sueldoMes);
		System.out.println("hrs extra: "+horasExtra);
		System.out.println("sueldo hora:"+sueldoHora);
		System.out.println("sueldo total: "+sueldoTotal());
	}
	public void mostrar(float x) {
		if (sueldoMes==x) {
			System.out.println("--------el mesero con sueldo igual a x es:-------");
			System.out.println("nombre:"+nombre);
			System.out.println("sueldo mes:"+sueldoMes);
			System.out.println("hrs extra: "+horasExtra);
			System.out.println("sueldo hora:"+sueldoHora);
			System.out.println("sueldo total: "+sueldoTotal());
		}
		else {
			System.out.println("no se encontro ningun mesero que tenga el sueldo igual a "+x);
		}
	}
}
